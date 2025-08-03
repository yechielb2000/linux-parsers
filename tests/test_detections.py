from linux_parsers.command_detection import auto_parse_output, _parse_command_string, _find_matching_parser
from linux_parsers.parsers.network import ip
from linux_parsers.parsers.session import ac
from tests.network.test_ip import IP_A_COMMAND_OUTPUT

CMD = "ip a"


def find_cmd_parsers(cmds):
    parsers = []
    for cmd in cmds:
        binary, sub_cmd, flags = _parse_command_string(cmd)
        binary_registry = _find_matching_parser(binary, sub_cmd, flags)
        parsers.append(binary_registry)
    return parsers


def test_network_detection():
    res = auto_parse_output(CMD, IP_A_COMMAND_OUTPUT)
    assert res is not None


def test_command_parser():
    binary, subcommand, flags = _parse_command_string(CMD)
    parser_func = _find_matching_parser(binary, subcommand, flags)
    assert binary == "ip"
    assert subcommand == "a"
    assert flags == set()
    assert parser_func is ip.parse_ip_a


def test_if_parsers_were_found():
    cmds = ["ac -dp", "ac -p", "ufw app list", "mpstat -P ALL", "ip a", "iptables -L -n -v", "hwinfo --cpu"]
    parsers = find_cmd_parsers(cmds)
    for parser in parsers:
        assert parser is not None


def test_if_parser_should_not_be_found():
    cmd = ["notexists -pd", "ac -xd", "hwinfo --cyber"]
    parsers = find_cmd_parsers(cmd)
    for parser in parsers:
        assert parser is None


def test_specific_cmds():
    cmds = ["ac -d", "ac -dp", "ac -p"]
    parsers = find_cmd_parsers(cmds)
    assert parsers[0] == ac.parse_ac_d
    assert parsers[1] == ac.parse_ac_pd
    assert parsers[2] == ac.parse_ac_p
