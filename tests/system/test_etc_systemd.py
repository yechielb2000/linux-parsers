from linux_parsers.parsers.system.etc_systemd_file_conf import parse_etc_systemd_file_conf


def test_etc_systemd():
    command_output = """
# the /etc/systemd/networkd.conf.d/ directory. The latter is generally
# recommended.

[Network]
#SpeedMeter=no
SpeedMeterIntervalSec=10sec
UseDomains=no

[IPv6AcceptRA]
#UseDomains=

[DHCPv4]
#DUIDType=vendor
#DUIDRawData=
#UseDomains=

[DHCPv6]
#DUIDType=vendor
#DUIDRawData=
#UseDomains=

[DHCPServer]
#PersistLeases=yes    
"""
    parsed_output = parse_etc_systemd_file_conf(command_output)
    assert parsed_output["Network"]["SpeedMeterIntervalSec"] == "10sec"
    assert parsed_output["Network"]["UseDomains"] == "no"
    assert not parsed_output["IPv6AcceptRA"].get("UseDomains")
