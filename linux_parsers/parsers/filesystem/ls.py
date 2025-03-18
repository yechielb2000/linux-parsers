import re

from typing import List, Dict, Any


def parse_ls(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ls -la` command output."""
    pattern = re.compile(
        r"(?P<Permissions>\S+)\s+"
        r"(?P<HardLinks>\d+)\s"
        r"(?P<Owner>\S+)\s+"
        r"(?P<Group>\S+)\s+"
        r"(?P<Size>\d+)\s+"
        r"(?P<LastModified>\w{3}\s+\d+\s+\d+:\d+)\s+"
        r"(?P<File>.+)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
