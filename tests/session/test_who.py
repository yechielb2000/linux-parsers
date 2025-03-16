from linux_parsers.parsers.session.who import parse_who_a


def test_who():
    command_output = """
alice    tty1         2025-03-16 14:03 (:0)
bob      pts/0        2025-03-16 13:50 (192.168.1.100)
charlie  pts/1        2025-03-16 13:45 (fe80::a00:27ff:fe8f:9fd0)
dave     tty2         2025-03-16 12:30 (:1)
eve      pts/2        2025-03-16 10:00 (192.168.1.102)
run-level 3  2025-03-16 09:30
system boot  2025-03-16 09:00
shutdown   2025-03-16 08:30
reboot     2025-03-16 08:15
"""
    parsed_output = parse_who_a(command_output)
    assert len(parsed_output['users_records']) == 5
    assert parsed_output['users_records'][0]['user'] == 'alice'
    assert parsed_output['users_records'][1]['user'] == 'bob'
    assert parsed_output['users_records'][2]['from'] == 'fe80::a00:27ff:fe8f:9fd0'
    assert parsed_output['system_records']['system boot']['date'] == '2025-03-16'
    assert parsed_output['system_records']['system boot']['time'] == '09:00'
    assert parsed_output['system_records']['shutdown']['date'] == '2025-03-16'