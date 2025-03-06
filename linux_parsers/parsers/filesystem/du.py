import re
from typing import Any


def parse_du(command_output: str) -> list[dict[str, str | Any]]:
    """Parse `du -ab <path>` command output."""
    pattern = re.compile(r"(?P<sizeBytes>\d+)\s+(?P<path>.+)")
    return [i.groupdict() for i in pattern.finditer(command_output)]
