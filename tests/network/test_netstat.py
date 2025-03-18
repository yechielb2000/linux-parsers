from linux_parsers.parsers.network.netstat import parse_netstat


def test_netstat():
    command_output = """
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 192.168.1.10:22         0.0.0.0:*               LISTEN      1234/sshd
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      5678/mysqld
tcp        0      0 192.168.1.10:443        203.0.113.5:52314       ESTABLISHED 9012/nginx
udp        0      0 0.0.0.0:68              0.0.0.0:*                           3456/dhclient
udp        0      0 192.168.1.10:123        0.0.0.0:*                           6789/ntpd
tcp        0      0 10.255.255.254:53       0.0.0.0:*               LISTEN      -
udp        0      0 10.255.255.254:53       0.0.0.0:*                           -
udp        0      0 127.0.0.1:323           0.0.0.0:*                           -
udp6       0      0 ::1:323                 :::*                                -    
"""

    parsed_result = parse_netstat(command_output)
    assert len(parsed_result) == 9
    assert parsed_result[0]["Proto"] == "tcp"
    assert parsed_result[0]["State"] == "LISTEN"
    assert parsed_result[5]["LocalAddress"] == "10.255.255.254:53"
    assert parsed_result[5]["ForeignAddress"] == "0.0.0.0:*"
