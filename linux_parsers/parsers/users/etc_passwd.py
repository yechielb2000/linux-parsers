import re

from typing import List, Dict, Any


def parse_etc_passwd_file(command_output: str) -> List[Dict[str, Any]]:
    """Parse `cat /etc/passwd` command output"""
    pattern = re.compile(
        r"^\b(?P<username>[^:]+)"
        r":(?P<password>[^:]*)"
        r":(?P<uid>[0-9]+)"
        r":(?P<gid>[0-9]+)"
        r":(?P<comment>[^:]*)"
        r":(?P<home>[^:]+)"
        r":(?P<shell>[^:]*)$",
        re.MULTILINE,
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
