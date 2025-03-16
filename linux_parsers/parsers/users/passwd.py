import re


def parse_etc_passwd_file(command_output: str) -> list[dict[str, any]]:
    """Parse `cat /etc/passwd` command output"""
    pattern = re.compile(
        r"^\b(?P<username>[^:]+)"
        r":(?P<password>[^:]*)"
        r":(?P<uid>[0-9]+)"
        r":(?P<gid>[0-9]+)"
        r":(?P<comment>[^:]*)"
        r":(?P<home>[^:]+)"
        r":(?P<shell>[^:]*)$",
        re.MULTILINE
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
