from linux_parsers.parsers.users.shadow import parse_etc_shadow_file


def test_shadow():
    command_output = """
user1:$6$randomsalt$2tEZaTxsJGHnkmwPzXsjRVD41DXbNxyk6OYd2XpckFgXG0QbXX1XUfnj5Qsq.y7AkJ5XyffwzKQgxE3lfrP8F/:18144:0:99999:7:::
user2:$6$anotherSalt$1yXnd6Dwv5js.zBhSmqzRo5P4fpPBRXmcYp8vZPOEVSH8wODmPZg6XUq48SXiSY2iHb2FNDR9fmksqLOz2jwQ/:18144:0:99999:7:::
user3:$6$thirdSalt$7bbCmMmUr61JYgtlxhRI5x25jp93oLTx6FTz6usIrKMKdLfZZBjs7xyhU5tNuvlTn0kvlzQfe8ghhv1jz5e8gH/:18144:0:99999:7:::
"""
    parsed_output = parse_etc_shadow_file(command_output)
    assert len(parsed_output) == 3
    assert parsed_output[0] == {
        'expiration_date': '',
        'inactive_days': '',
        'last_change': '18144',
        'max_days': '99999',
        'min_days': '0',
        'password_hash': '2tEZaTxsJGHnkmwPzXsjRVD41DXbNxyk6OYd2XpckFgXG0QbXX1XUfnj5Qsq.y7AkJ5XyffwzKQgxE3lfrP8F/',
        'reserved': '',
        'salt': 'randomsalt',
        'username': 'user1',
        'warning_days': '7'
    }
