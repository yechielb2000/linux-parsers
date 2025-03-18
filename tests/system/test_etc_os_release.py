from linux_parsers.parsers.system.etc_os_release import parse_etc_os_release_file


def test_etc_os_release():
    command_output = """PRETTY_NAME="Kali GNU/Linux Rolling"
NAME="Kali GNU/Linux"
VERSION_ID="2024.3"
VERSION="2024.3"
VERSION_CODENAME=kali-rolling
ID=kali
ID_LIKE=debian
HOME_URL="https://www.kali.org/"
SUPPORT_URL="https://forums.kali.org/"
BUG_REPORT_URL="https://bugs.kali.org/"
ANSI_COLOR="1;31"
"""
    parsed_output = parse_etc_os_release_file(command_output)
    assert parsed_output == {
        "ANSI_COLOR": "1;31",
        "BUG_REPORT_URL": "https://bugs.kali.org/",
        "HOME_URL": "https://www.kali.org/",
        "ID": "kali",
        "ID_LIKE": "debian",
        "NAME": "Kali GNU/Linux",
        "PRETTY_NAME": "Kali GNU/Linux Rolling",
        "SUPPORT_URL": "https://forums.kali.org/",
        "VERSION": "2024.3",
        "VERSION_CODENAME": "kali-rolling",
        "VERSION_ID": "2024.3",
    }
