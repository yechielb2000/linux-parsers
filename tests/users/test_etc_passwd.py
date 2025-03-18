from linux_parsers.parsers.users.etc_passwd import parse_etc_passwd_file


def test_passwd():
    command_output = """
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
messagebus:x:100:102::/nonexistent:/usr/sbin/nologin
tcpdump:x:101:103::/nonexistent:/usr/sbin/nologin
sshd:x:102:65534::/run/sshd:
a:x:1000:1000:,,,:/home/a:/bin/bash

"""
    parsed_output = parse_etc_passwd_file(command_output)
    assert len(parsed_output) == 5
    assert parsed_output[0]["username"] == "systemd-network"
    assert parsed_output[0]["password"] == "x"
    assert parsed_output[1]["username"] == "messagebus"
    assert parsed_output[1]["shell"] == "/usr/sbin/nologin"
