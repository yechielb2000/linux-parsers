from linux_parsers.parsers.process.jobs import parse_jobs


def test_jobs():
    command_output = """
[1] nano report.txt &
[2]- vim logs.txt &
[3]+ htop &
"""
    parsed_command = parse_jobs(command_output)
    assert len(parsed_command) == 3
    assert parsed_command[0]["job"] == "nano report.txt &"
    assert parsed_command[1]["job"] == "vim logs.txt &"
    assert parsed_command[2]["job"] == "htop &"
    assert parsed_command[2]["priority"] == "+"
