from linux_parsers.parsers.logs.var_log_auth import parse_var_log_auth


def test_var_log_auth():
    command_output = """
Apr 30 14:22:01 myhostname CRON[1234]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Apr 30 14:40:12 myhostname sshd[2345]: pam_unix(sshd:session): session closed for user user1
Apr 30 14:42:50 myhostname sudo:   user1 : TTY=pts/0 ; PWD=/home/user1 ; USER=root ; COMMAND=/bin/ls
Apr 30 15:01:33 myhostname sshd[2456]: Failed password for invalid user admin from 203.0.113.55 port 43821 ssh2
"""
    parsed_output = parse_var_log_auth(command_output)
    assert parsed_output[1] == {
        "event": "sshd[2345]",
        "hostname": "myhostname",
        "message": "pam_unix(sshd:session): session closed for user user1",
        "timestamp": "Apr 30 14:40:12",
    }
    assert parsed_output[2] == {
        "event": "sudo",
        "hostname": "myhostname",
        "message": "user1 : TTY=pts/0 ; PWD=/home/user1 ; USER=root ; COMMAND=/bin/ls",
        "timestamp": "Apr 30 14:42:50",
    }
