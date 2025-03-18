from linux_parsers.parsers.network.iptables import parse_iptables


def test_iptables():
    command_output = """
Chain INPUT (policy ACCEPT 1000 packets, 200K bytes)
    pkts      bytes target     prot opt in     out     source               destination         
   15000   3000000 ACCEPT     all  --  *      *       192.168.1.0/24        0.0.0.0/0            
   2000    4000000 ACCEPT     tcp  --  *      *       10.0.0.0/8            0.0.0.0/0            tcp dpt:22
   500     1000000 DROP       all  --  *      *       172.16.0.0/12         0.0.0.0/0            
   0       0          LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0            LOG level warning
   10000   2000000 ACCEPT     icmp --  *      *       0.0.0.0/0            0.0.0.0/0            icmp echo-request

Chain FORWARD (policy ACCEPT 500 packets, 100K bytes)
    pkts      bytes target     prot opt in     out     source               destination         
   3000    6000000 ACCEPT     all  --  *      *       0.0.0.0/0            10.10.10.0/24        
   0       0          REJECT     all  --  *      *       0.0.0.0/0            172.16.0.0/12        reject-with icmp-port-unreachable
   0       0          LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0            LOG level info

Chain OUTPUT (policy ACCEPT 2000 packets, 300K bytes)
    pkts      bytes target     prot opt in     out     source               destination         
   5000    10000000 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            
   1000    2000000 ACCEPT     tcp  --  *      *       0.0.0.0/0            192.168.1.100        tcp dpt:80
   0       0          REJECT     icmp --  *      *       0.0.0.0/0            0.0.0.0/0            icmp echo-reply
   100     200000    LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0            LOG level debug

Chain DOCKER (policy ACCEPT 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
   100     50000  ACCEPT     tcp  --  *      *       172.17.0.0/16         0.0.0.0/0            tcp dpt:8080
   0       0        ACCEPT     udp  --  *      *       172.17.0.0/16         0.0.0.0/0            udp dpt:53
   50      25000  DROP       all  --  *      *       192.168.0.0/16         0.0.0.0/0            
    """
    parsed_command = parse_iptables(command_output)
    assert list(parsed_command.keys()) == ["INPUT", "FORWARD", "OUTPUT", "DOCKER"]
    assert len(parsed_command["FORWARD"]) == 2
    assert len(parsed_command["OUTPUT"]) == 2
    assert len(parsed_command["DOCKER"]) == 2
    assert parsed_command["FORWARD"][0]["target"] == "REJECT"
    assert parsed_command["FORWARD"][1]["target"] == "LOG"
    assert parsed_command["FORWARD"][1]["rule"] == "LOG level info"
