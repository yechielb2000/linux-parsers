import re

from typing import List, Dict, Any


def parse_dpkg_l(command_output: str) -> List[Dict[str, Any]]:
    """Parse `dpkg -l` command output."""
    pattern = re.compile(
        r"ii\s+(?P<name>\S+)\s+(?P<version>\S+)\s+(?P<arch>\S+)\s+(?P<description>.+)",
        flags=re.MULTILINE,
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
