from linux_parsers.parsers.users.chage import parse_chage_l


def test_chage():
    command_output = """
Last password change                                    : Aug 31, 2024
Password expires                                        : never
Password inactive                                       : never
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 99999
Number of days of warning before password expires       : 7

"""
    parsed_output = parse_chage_l(command_output)
    assert parsed_output['Last password change'] == 'Aug 31, 2024'
    assert parsed_output['Password expires'] == 'never'
    assert parsed_output['Password inactive'] == 'never'
    assert parsed_output['Account expires'] == 'never'
    assert parsed_output['Minimum number of days between password change'] == '0'
    assert parsed_output['Maximum number of days between password change'] == '99999'
    assert parsed_output['Number of days of warning before password expires'] == '7'