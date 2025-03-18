from linux_parsers.parsers.network.ss import parse_ss_tulnap, parse_ss_s


def test_ss():
    command_output = """
State     Recv-Q    Send-Q    Local Address:Port     Peer Address:Port     Process
LISTEN    0         128       0.0.0.0:22             0.0.0.0:*             users:(("sshd",pid=1234,fd=3))
LISTEN    0         128       0.0.0.0:80             0.0.0.0:*             users:(("nginx",pid=5678,fd=6))
LISTEN    0         128       127.0.0.1:3306         0.0.0.0:*             users:(("mysqld",pid=9101,fd=10))
LISTEN    0         128       [::]:22                [::]:*                users:(("sshd",pid=1234,fd=4))
ESTAB     0         0         192.168.1.10:22        192.168.1.20:54321    users:(("sshd",pid=1234,fd=3))
ESTAB     0         0         192.168.1.10:443       203.0.113.5:52314     users:(("nginx",pid=5678,fd=8))
ESTAB     0         0         192.168.1.10:3306      192.168.1.25:65432    users:(("mysqld",pid=9101,fd=11))
TIME-WAIT 0         0         192.168.1.10:3306      192.168.1.25:65433    users:(("mysqld",pid=9101,fd=12))
CLOSE_WAIT 0        0         192.168.1.10:3306      192.168.1.25:65434    users:(("mysqld",pid=9101,fd=13))
SYN-SENT  0         0         192.168.1.10:445       203.0.113.5:54321     users:(("smbd",pid=4567,fd=4))
LISTEN    0         128       0.0.0.0:53             0.0.0.0:*             users:(("named",pid=2345,fd=7))
ESTAB     0         0         192.168.1.10:443       203.0.113.6:52314     users:(("nginx",pid=5678,fd=9))
LISTEN    0         128       192.168.1.10:8080      0.0.0.0:*             users:(("apache2",pid=1357,fd=5))
LISTEN    0         128       [::]:80                [::]:*                users:(("nginx",pid=5678,fd=11))
UDP       0         0         0.0.0.0:68             0.0.0.0:*             users:(("dhclient",pid=1122,fd=6))
UDP       0         0         192.168.1.10:123       0.0.0.0:*             users:(("ntpd",pid=3456,fd=7))
UDP       0         0         0.0.0.0:123            0.0.0.0:*             users:(("ntpd",pid=3456,fd=8))    
    """

    parsed_result = parse_ss_tulnap(command_output)
    assert len(parsed_result) == 17
    assert parsed_result[0]["PeerAddress_Port"] == "0.0.0.0:*"
    assert parsed_result[1]["Process"] == 'users:(("nginx",pid=5678,fd=6))'
    assert parsed_result[7]["State"] == "TIME-WAIT"
    assert parsed_result[8]["State"] == "CLOSE_WAIT"
    assert parsed_result[13]["LocalAddress_Port"] == "[::]:80"


def test_ss_s():
    command_output = """
Total: 3000 (kernel 3500)
TCP:   1524 (estab 985, closed 330, orphaned 23, synrecv 5, timewait 181/350)

UDP:   702
UDPLite: 0
RAW:   18
FRAG:  4

Transport Total     IP        IPv6
RAW       18        11        7
UDP       702       689       13
TCP       1524      1400      124
INET      2244      1800      444
FRAG      4         3         1
    """
    parsed_result = parse_ss_s(command_output)
    assert parsed_result["total"] == "3000"
    assert parsed_result["kernel"] == "3500"
    assert parsed_result["TCP"]["closed"] == "330"
    assert parsed_result["UDP"] == "702"
    assert parsed_result["RAW"] == "18"
    assert parsed_result["transports"][0]["total"] == "18"
