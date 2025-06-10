from linux_parsers.parsers.logs.var_log_syslog import parse_var_log_syslog


def test_var_log_syslog():
    command_output = """
Jun 10 10:15:01 mymachine CRON[1234]: (root) CMD (echo 'Hello world')
Jun 10 10:15:02 mymachine systemd[1]: Starting Daily apt download activities...
Jun 10 10:16:12 mymachine kernel: [12345.678901] eth0: Link is Up - 1Gbps/Full - flow control rx/tx
Jun 10 10:16:20 mymachine sshd[2456]: Accepted password for user1 from 192.168.1.101 port 53421 ssh2
Jun 10 10:16:21 mymachine sshd[2456]: pam_unix(sshd:session): session opened for user user1 by (uid=0)
Jun 10 10:17:00 mymachine sudo:    user1 : TTY=pts/0 ; PWD=/home/user1 ; USER=root ; COMMAND=/bin/ls
Jun 10 10:17:01 mymachine sudo: pam_unix(sudo:session): session opened for user root by user1(uid=0)
Jun 10 10:17:30 mymachine systemd[1]: Starting Clean php session files...
"""
    parsed_output = parse_var_log_syslog(command_output)
    assert parsed_output[1] == {
        "day": "10",
        "host": "mymachine",
        "message": "Starting Daily apt download activities...",
        "month": "Jun",
        "pid": "1",
        "process": "systemd",
        "time": "10:15:02",
    }

    assert parsed_output[5] == {
        "day": "10",
        "host": "mymachine",
        "message": "user1 : TTY=pts/0 ; PWD=/home/user1 ; USER=root ; COMMAND=/bin/ls",
        "month": "Jun",
        "pid": None,
        "process": "sudo",
        "time": "10:17:00",
    }
