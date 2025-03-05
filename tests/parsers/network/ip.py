from linux_parsers.parsers.network.ip import parse_ip


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
    parsed_result = parse_ip(command_output)
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
