from linux_parsers.parsers.network.etc_resolve_conf import parse_etc_resolve_conf_file


def test_etc_resolve_conf():
    command_output = """
# Primary DNS servers for public internet
nameserver 8.8.8.8
nameserver 8.8.4.4

# Secondary DNS servers for internal network
nameserver 192.168.1.1
nameserver 192.168.1.2

# Search domain for the main company network
search company.com

# Additional search domains for the testing network
search dev.company.com staging.company.com

# Resolver options to customize DNS query behavior
options timeout:5 attempts:2

# Resolver options for a specific subnetwork with multiple dot (ndots)
options ndots:3

# Additional security settings for DNS resolution
options edns0

# Search domains for VPN connection
search vpn.example.com

# Search domain for a local intranet
search intranet.local

# Specific resolver options for a higher priority DNS server
options rotate

# Performance options to control DNS query retries and timeouts
options timeout:10 attempts:5

# Experimental options for DNS resolution
options single-request    
"""
    parsed_output = parse_etc_resolve_conf_file(command_output)
    assert parsed_output["nameservers"] == [
        "8.8.8.8",
        "8.8.4.4",
        "192.168.1.1",
        "192.168.1.2",
    ]
    assert parsed_output["search_domains"] == [
        "company.com",
        "dev.company.com",
        "staging.company.com",
        "vpn.example.com",
        "intranet.local",
    ]
    assert parsed_output["options"] == [
        "timeout:5",
        "attempts:2",
        "ndots:3",
        "edns0",
        "rotate",
        "timeout:10",
        "attempts:5",
        "single-request",
    ]
