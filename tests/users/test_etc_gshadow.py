from linux_parsers.parsers.users.etc_gshadow import parse_etc_gshadow_file


def test_etc_gshadow_file():
    command_output = """plugdev:*::a
staff:*::
games:*::
users:*::a
nogroup:*::
systemd-journal:!*::
systemd-network:!*::
crontab:!*::
input:!*::
sgx:!*::
kvm:!*::
render:!*::
netdev:!::
messagebus:!::"""
    parsed_output = parse_etc_gshadow_file(command_output)
    assert parsed_output is not None
    assert len(parsed_output) == 14
    assert parsed_output[0] == {'encrypted_password': '*', 'group_id': '', 'group_name': 'plugdev', 'users': 'a'}
    assert parsed_output[3] == {'encrypted_password': '*', 'group_id': '', 'group_name': 'users', 'users': 'a'}
