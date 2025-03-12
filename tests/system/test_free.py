from linux_parsers.parsers.system.free import parse_free_btlv


def test_btlv():
    command_output = """
               total        used        free      shared  buff/cache   available
Mem:      8269094912   540090368  7779119104     2588672   171544576  7729004544
Low:      8269094912   489975808  7779119104
High:              0           0           0
Swap:     2147483648           0  2147483648
Total:   10416578560   540090368  9926602752
Comm:     6282031104   417738752  5864292352

"""
    parsed_output = parse_free_btlv(command_output)
    assert parsed_output['High'] == {'available': None, 'cache': None, 'free': '0',
                                    'shared': None, 'total': '0', 'used': '0'}
    assert parsed_output['Swap'] == {'available': None, 'cache': None, 'free': '2147483648',
                                     'shared': None, 'total': '2147483648', 'used': '0'}
    assert parsed_output['Comm'] == {'available': None, 'cache': None, 'free': '5864292352',
                                      'shared': None, 'total': '6282031104', 'used': '417738752'}
