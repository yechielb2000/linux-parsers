from linux_parsers.parsers.users.etc_group import parse_etc_group_file


def test_etc_group_file():
    command_output = """src:x:40:
shadow:x:42:
utmp:x:43:
plugdev:x:46:a
staff:x:50:
docker:x:106:a"""
    parsed_output = parse_etc_group_file(command_output)
    assert len(parsed_output) == 6
    assert parsed_output[0]['group_name'] == "src"
    assert parsed_output[2]['group_name'] == "utmp"
    assert parsed_output[3]['password'] == "x"
    assert parsed_output[5]['members'] == "a"