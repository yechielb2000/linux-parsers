from linux_parsers.parsers.session.w import parse_w


def test_w():
    command_output = """
     16:25:11 up  2:35,  4 users,  load average: 0.21, 0.19, 0.14
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
alice    pts/0    192.168.1.100    14:03    1:25   0.20s  0.10s bash
alice    pts/1    192.168.1.101    14:30    0.00s  0.05s  0.02s vim file.txt
"""
    parsed_output = parse_w(command_output)
    assert len(parsed_output["records"]) == 2
    assert parsed_output["metadata"] == {
        "load1": "0.21",
        "load2": "0.19",
        "load3": "0.14",
        "time": "16:25:11",
        "uptime": "2:35",
        "users": "4",
    }
    assert parsed_output["records"][1] == {
        "command": "vim file.txt",
        "from": "192.168.1.101",
        "idle": "0.00s",
        "jcpu": "0.05s",
        "login": "14:30",
        "pcpu": "0.02s",
        "tty": "pts/1",
        "event": "alice",
    }
