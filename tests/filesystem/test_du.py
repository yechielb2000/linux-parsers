from linux_parsers.parsers.filesystem.du import parse_du


def test_du():
    command_output = """
0       /var/logs/btmp
0       /var/logs/lastlog
0       /var/logs/runit/ssh
0       /var/logs/runit
0       /var/logs/bootstrap.logs
0       /var/logs/journal
77788   /var/logs/apt/term.logs
13606   /var/logs/apt/history.logs
20016   /var/logs/apt/eipp.logs.xz
111410  /var/logs/apt
du: cannot read directory '/var/logs/private': Permission denied
0       /var/logs/private
0       /var/logs/wtmp
39      /var/logs/README
140214  /var/logs/dpkg.logs
7711    /var/logs/alternatives.logs
61747   /var/logs/docker.logs
321121  /var/logs
"""
    parsed_command = parse_du(command_output)
    assert len(parsed_command) == 17
    assert parsed_command[0]["path"] == "/var/logs/btmp"
    assert parsed_command[1]["path"] == "/var/logs/lastlog"
    assert parsed_command[2]["path"] == "/var/logs/runit/ssh"
    assert parsed_command[0]["sizeBytes"] == "0"
    assert parsed_command[1]["sizeBytes"] == "0"
    assert parsed_command[6]["sizeBytes"] == "77788"
