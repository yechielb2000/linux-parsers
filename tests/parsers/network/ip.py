from linux_parsers.parsers.network.ip import parse_ip_a, parse_ip_r


def test_ip():
    command_output = """
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:0c:94:bc brd ff:ff:ff:ff:ff:ff
    inet 172.22.240.176/20 brd 172.22.255.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fe0c:94bc/64 scope link
       valid_lft forever preferred_lft forever
    """
    parsed_result = parse_ip_a(command_output)
    expected_result = [
        {
            'inets': [
                {'brd': None, 'ip': '127.0.0.1/8', 'preferred_lft': 'forever', 'scope': 'host lo', 'type': 'inet',
                 'valid_lft': 'forever'},
                {'brd': '10.255.255.254', 'ip': '10.255.255.254/32', 'preferred_lft': 'forever', 'scope': 'global lo',
                 'type': 'inet', 'valid_lft': 'forever'},
                {'brd': None, 'ip': '::1/128', 'preferred_lft': 'forever', 'scope': 'host', 'type': 'inet6',
                 'valid_lft': 'forever'}],
            'info': {'flags': 'LOOPBACK,UP,LOWER_UP', 'group': 'default', 'mtu': '65536',
                     'qdisc': 'noqueue', 'qlen': '1000', 'state': 'UNKNOWN'},
            'link': {'brd': '00:00:00:00:00:00', 'ip': '00:00:00:00:00:00', 'link': 'loopback'}
        }
    ]
    assert parsed_result == expected_result


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
