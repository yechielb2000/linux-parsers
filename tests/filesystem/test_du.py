from linux_parsers.parsers.filesystem.df import parse_df
from linux_parsers.parsers.filesystem.du import parse_du


def test_du():
    command_output = """
0       /var/log/btmp
0       /var/log/lastlog
0       /var/log/runit/ssh
0       /var/log/runit
0       /var/log/bootstrap.log
0       /var/log/journal
77788   /var/log/apt/term.log
13606   /var/log/apt/history.log
20016   /var/log/apt/eipp.log.xz
111410  /var/log/apt
du: cannot read directory '/var/log/private': Permission denied
0       /var/log/private
0       /var/log/wtmp
39      /var/log/README
140214  /var/log/dpkg.log
7711    /var/log/alternatives.log
61747   /var/log/docker.log
321121  /var/log
"""
    parsed_command = parse_du(command_output)
    assert len(parsed_command) == 17
    assert parsed_command[0]['path'] == '/var/log/btmp'
    assert parsed_command[1]['path'] == '/var/log/lastlog'
    assert parsed_command[2]['path'] == '/var/log/runit/ssh'
    assert parsed_command[0]['sizeBytes'] == '0'
    assert parsed_command[1]['sizeBytes'] == '0'
    assert parsed_command[6]['sizeBytes'] == '77788'
