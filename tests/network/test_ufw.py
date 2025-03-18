from linux_parsers.parsers.network.ufw import parse_ufw_status


def test_ufw_status():
    command_output = """
Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere
80                         ALLOW       Anywhere
443                        ALLOW       Anywhere
3306                       DENY        Anywhere
22 (v6)                    ALLOW       Anywhere (v6)
80 (v6)                    ALLOW       Anywhere (v6)
443 (v6)                   ALLOW       Anywhere (v6)
3306 (v6)                  DENY        Anywhere (v6)    
"""
    parsed_command = parse_ufw_status(command_output)
    assert len(parsed_command) == 8
    assert parsed_command[5]["To"] == "80 (v6)"
    assert parsed_command[6]["Action"] == "ALLOW"
    assert parsed_command[7]["From"] == "Anywhere (v6)"
