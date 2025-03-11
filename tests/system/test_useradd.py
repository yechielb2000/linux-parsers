from linux_parsers.parsers.system.useradd import parse_useradd_D


def test_useradd_D():
    command_output = """
GROUP=100
GROUPS=
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/sh
SKEL=/etc/skel
USRSKEL=/usr/etc/skel
CREATE_MAIL_SPOOL=no
LOG_INIT=yes
"""
    parsed_output = parse_useradd_D(command_output)
    assert parsed_output['GROUPS'] == '100'
    assert parsed_output['HOME'] == '/home'
    assert parsed_output['INACTIVE'] == '-1'
    assert parsed_output['CREATE_MAIL_SPOOL'] == 'no'
