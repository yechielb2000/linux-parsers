from linux_parsers.parsers.network.ping import parse_ping


def test_ping():
    command_output = """
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=15.4 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=15.1 ms
Request timeout for icmp_seq=3
64 bytes from 8.8.8.8: icmp_seq=4 ttl=118 time=14.9 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=118 time=15.2 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 4 received, 20% packet loss, time 4001ms
rtt min/avg/max/mdev = 14.9/15.15/15.4/0.2 ms
    """
    parsed_result = parse_ping(command_output)

    assert parsed_result['target'] == '8.8.8.8'
    assert parsed_result['payloadSize'] == '56'
    assert parsed_result['totalPacketSize'] == '84'
    assert len(parsed_result['records']) == 4
    assert parsed_result['records'][0] == {'replaySize': '64', 'from': '8.8.8.8', 'icmpSeq': '1', 'ttl': '118'}
    assert parsed_result['rtt']['avg'] == '15.15'