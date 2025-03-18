import re

from typing import List, Dict, Any


def parse_df(command_output: str) -> List[Dict[str, Any]]:
    """Parse 'df' command output."""
    pattern = re.compile(
        r"(?P<Filesystem>\S+)\s+"
        r"(?P<Blocks>\d+)\s+"
        r"(?P<Used>\d+)\s+"
        r"(?P<Available>\d+)\s+"
        r"(?P<UsePercent>\d+)%\s+"
        r"(?P<Mounted>.+)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
