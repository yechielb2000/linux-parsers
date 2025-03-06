from linux_parsers.parsers.network.arp import parse_arp


def test_arp_i():
    output = """
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.1.1              ether   00:1a:2b:3c:4d:5e   C                     eth0
192.168.1.100            ether   11:22:33:44:55:66   C                     eth0
192.168.1.101            ether   aa:bb:cc:dd:ee:ff   C                     eth0
    """
    result = parse_arp(output)
    expected = [
        {
            'Address': '192.168.1.1', 'FlagsMask': 'C', 'HWaddress': '00:1a:2b:3c:4d:5e', 'HWtype': 'ether',
            'Iface': 'eth0'
        },
        {
            'Address': '192.168.1.100', 'FlagsMask': 'C', 'HWaddress': '11:22:33:44:55:66', 'HWtype': 'ether',
            'Iface': 'eth0'
        },
        {
            'Address': '192.168.1.101', 'FlagsMask': 'C', 'HWaddress': 'aa:bb:cc:dd:ee:ff', 'HWtype': 'ether',
            'Iface': 'eth0'
        }
    ]
    assert result == expected

