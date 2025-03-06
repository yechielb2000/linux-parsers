from linux_parsers.parsers.network.ip import parse_ip_r, parse_ip_n, parse_ip_a


def test_ip_a():
    command_output = """
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever

2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:1a:2b:3c:4d:5e brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 86400sec preferred_lft 86400sec
    inet6 fe80::1a2b:3c4d:5e6f:7g8h/64 scope link 
       valid_lft forever preferred_lft forever

3: wlan0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether aa:bb:cc:dd:ee:ff brd ff:ff:ff:ff:ff:ff
    """
    parsed_result = parse_ip_a(command_output)
    assert parsed_result['1']['iface'] == 'lo'
    assert parsed_result['2']['mtu'] == '1500'
    assert len(parsed_result['2']['addresses']) == 2
    assert parsed_result['2']['addresses'][0]['valid_lft'] == '86400sec'
    assert parsed_result['2']['addresses'][0]['ip'] == '192.168.1.100/24'
    assert parsed_result['2']['addresses'][1]['ip'] == 'fe80::1a2b:3c4d:5e6f:7g8h/64'
    assert parsed_result['3']['iface'] == 'wlan0'
    assert parsed_result['3']['state'] == 'DOWN'
    assert len(parsed_result['3']['addresses']) == 0
    assert parsed_result['3']['link']['link'] == 'ether'
    assert parsed_result['3']['link']['ip'] == 'aa:bb:cc:dd:ee:ff'


def test_ip_r():
    command_output = """
    default via 192.168.1.1 dev eth0 proto dhcp metric 100
    192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
    10.0.0.0/8 via 192.168.1.254 dev eth0
    172.16.0.0/16 via 192.168.1.254 dev eth1 metric 200
    192.168.2.0/24 dev eth1 proto kernel scope link src 192.168.2.1
    192.168.3.0/24 via 192.168.2.254 dev eth1 metric 50
    192.168.4.0/24 dev eth2 proto static scope link src 192.168.4.1
    blackhole 192.168.5.0/24 proto static
    unreachable 192.168.6.0/24 proto static
    prohibit 192.168.7.0/24 proto static
    broadcast 192.168.1.255 dev eth0 proto kernel scope link src 192.168.1.100
    """
    parsed_command = parse_ip_r(command_output)
    expected_value = [{'dev': 'eth0', 'metric': '100', 'proto': 'dhcp', 'scope': None, 'src': None, 'type': 'default',
                       'via': '192.168.1.1'},
                      {'dev': 'eth0', 'metric': None, 'proto': 'kernel', 'scope': 'link', 'src': '192.168.1.100',
                       'type': '192.168.1.0/24', 'via': None},
                      {'dev': 'eth0', 'metric': None, 'proto': None, 'scope': None, 'src': None, 'type': '10.0.0.0/8',
                       'via': '192.168.1.254'},
                      {'dev': 'eth1', 'metric': '200', 'proto': None, 'scope': None, 'src': None,
                       'type': '172.16.0.0/16', 'via': '192.168.1.254'},
                      {'dev': 'eth1', 'metric': None, 'proto': 'kernel', 'scope': 'link', 'src': '192.168.2.1',
                       'type': '192.168.2.0/24', 'via': None},
                      {'dev': 'eth1', 'metric': '50', 'proto': None, 'scope': None, 'src': None,
                       'type': '192.168.3.0/24', 'via': '192.168.2.254'},
                      {'dev': 'eth2', 'metric': None, 'proto': 'static', 'scope': 'link', 'src': '192.168.4.1',
                       'type': '192.168.4.0/24', 'via': None},
                      {'dev': None, 'metric': None, 'proto': None, 'scope': None, 'src': None, 'type': 'blackhole',
                       'via': None}, {'dev': None, 'metric': None, 'proto': 'static', 'scope': None, 'src': None,
                                      'type': '192.168.5.0/24', 'via': None},
                      {'dev': None, 'metric': None, 'proto': None, 'scope': None, 'src': None, 'type': 'unreachable',
                       'via': None}, {'dev': None, 'metric': None, 'proto': 'static', 'scope': None, 'src': None,
                                      'type': '192.168.6.0/24', 'via': None},
                      {'dev': None, 'metric': None, 'proto': None, 'scope': None, 'src': None, 'type': 'prohibit',
                       'via': None}, {'dev': None, 'metric': None, 'proto': 'static', 'scope': None, 'src': None,
                                      'type': '192.168.7.0/24', 'via': None},
                      {'dev': None, 'metric': None, 'proto': None, 'scope': None, 'src': None, 'type': 'broadcast',
                       'via': None}]
    assert parsed_command == expected_value


def test_ip_n():
    command_output = """
192.168.1.1 dev eth0 lladdr 00:1a:2b:3c:4d:5e REACHABLE
10.0.0.254 dev wlan0 lladdr aa:bb:cc:dd:ee:ff STALE
172.16.0.100 dev eth1 FAILED
192.168.2.1 dev eth2 lladdr 11:22:33:44:55:66 DELAY
192.168.3.1 dev eth3 INCOMPLETE
2001:db8::1 dev eth0 lladdr 00:1a:2b:3c:4d:5f STALE
    """
    parsed_command = parse_ip_n(command_output)
    expected_value = [{'dev': 'eth0', 'ip': '192.168.1.1', 'lladdr': '00:1a:2b:3c:4d:5e', 'state': 'REACHABLE'},
                      {'dev': 'wlan0', 'ip': '10.0.0.254', 'lladdr': 'aa:bb:cc:dd:ee:ff', 'state': 'STALE'},
                      {'dev': 'eth1', 'ip': '172.16.0.100', 'lladdr': None, 'state': 'FAILED'},
                      {'dev': 'eth2', 'ip': '192.168.2.1', 'lladdr': '11:22:33:44:55:66', 'state': 'DELAY'},
                      {'dev': 'eth3', 'ip': '192.168.3.1', 'lladdr': None, 'state': 'INCOMPLETE'},
                      {'dev': 'eth0', 'ip': '2001:db8::1', 'lladdr': '00:1a:2b:3c:4d:5f', 'state': 'STALE'}]
    assert parsed_command == expected_value
