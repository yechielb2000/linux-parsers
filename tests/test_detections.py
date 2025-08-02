from linux_parsers.command_detection import auto_parse_output, _parse_command_string, _find_matching_parser
from linux_parsers.parsers.network import ip
from tests.network.test_ip import IP_A_COMMAND_OUTPUT

CMD = "ip a"


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
