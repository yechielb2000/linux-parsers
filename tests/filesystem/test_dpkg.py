from linux_parsers.parsers.filesystem.dpkg import parse_dpkg_l


def test_dpkg_l():
    command_output = """
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version                                       Architecture Description
+++-===============================-=============================================-============-================================================================================
ii  ack                             3.7.0-1                                       all          grep-like program specifically for large source trees
ii  adduser                         3.137                                         all          add and remove users and groups
ii  apparmor                        3.1.7-1+b3                                    amd64        user-space parser utility for AppArmor
ii  apt                             2.9.5+kali1                                   amd64        commandline package manager    
"""
    parsed_output = parse_dpkg_l(command_output)
    assert len(parsed_output) == 4
    assert parsed_output[0] == {'arch': 'all', 'description': 'grep-like program specifically for large source trees',
                                'name': 'ack', 'version': '3.7.0-1'}
    assert parsed_output[1] == {'arch': 'all', 'description': 'add and remove users and groups',
                                'name': 'adduser', 'version': '3.137'}
