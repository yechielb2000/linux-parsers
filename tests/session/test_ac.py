from linux_parsers.parsers.session.ac import parse_ac_p, parse_ac_d, parse_ac_pd


def test_ac_p():
    command_output = """
    user1                             15.75
    user2                              0.12

    total                             96.78
"""
    parsed_command = parse_ac_p(command_output)
    users = parsed_command["users"]
    total = parsed_command["total"]
    assert len(users) == 2
    assert users[0]["user"] == "user1"
    assert users[1]["time"] == "0.12"
    assert total == "96.78"


def test_ac_d():
    command_output = """
Mar 29   total      0.00
Mar 30   total      3.25
Mar 31   total     12.80
Apr 01   total     24.50
"""
    parsed_command = parse_ac_d(command_output)
    assert len(parsed_command) == 4
    assert parsed_command[0]["date"] == "Mar 29"
    assert parsed_command[0]["total"] == "0.00"
    assert parsed_command[3]["date"] == "Apr 01"
    assert parsed_command[3]["total"] == "24.50"


def test_ac_pd():
    command_output = """
Mar 30:
    user1           1.20
    intern          2.05
    total           3.25

Mar 31:
    user1           5.00
    developer       7.80
    total          12.80
    
"""
    parsed_output = parse_ac_pd(command_output)
    assert parsed_output
    assert len(parsed_output) == 2
    assert parsed_output["Mar 30"] is not None
    assert parsed_output["Mar 30"]["user1"] == "1.20"
    assert parsed_output["Mar 30"]["intern"] == "2.05"
