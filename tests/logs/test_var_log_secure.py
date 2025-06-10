from linux_parsers.parsers.logs.var_log_secure import parse_var_log_secure


def test_var_log_secure():
    command_output = """
Apr 30 17:52:14 servername sshd[1042]: Accepted password for root from 192.168.1.100 port 54321 ssh2
Apr 30 17:52:14 servername sshd[1042]: pam_unix(sshd:session): session opened for event root by (uid=0)
Apr 30 18:05:43 servername systemd-logind[750]: New session 14 of event alice.
Apr 30 18:20:17 servername sudo:    bob : TTY=pts/1 ; PWD=/home/bob ; USER=root ; COMMAND=/bin/systemctl restart nginx
Apr 30 18:20:17 servername sudo: pam_unix(sudo:session): session opened for event root by bob(uid=0)
Apr 30 18:45:12 servername sshd[1167]: Disconnected from event root 192.168.1.100 port 54321
"""
    parsed_output = parse_var_log_secure(command_output)
    assert parsed_output[0] == {
        "hostname": "servername",
        "message": "Accepted password for root from 192.168.1.100 port 54321 ssh2",
        "process": "sshd[1042]",
        "timestamp": "Apr 30 17:52:14",
    }
    assert parsed_output[3] == {
        "hostname": "servername",
        "message": "bob : TTY=pts/1 ; PWD=/home/bob ; USER=root ; COMMAND=/bin/systemctl restart nginx",
        "process": "sudo",
        "timestamp": "Apr 30 18:20:17",
    }
