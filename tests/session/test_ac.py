from linux_parsers.parsers.session.ac import parse_ac_p


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
