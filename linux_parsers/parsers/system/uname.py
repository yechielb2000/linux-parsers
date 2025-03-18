import re
from typing import Dict, Any


def parse_uname_a(command_output: str) -> Dict[str, Any]:
    """Parse `uname -a` command output."""
    pattern = re.compile(
        r"^(?P<kernel>\S+)\s(?P<hostname>\S+)\s(?P<kernel_version>\S+)"
        r"\s(?P<build_number>#\d+(?:-\S+)?)\s+(?P<smp>SMP)?\s*"
        r"(?P<build_date>.+UTC\s\d+)\s(?:(?P<machine>\S+)\s)?"
        r"(?:(?P<processor>\S+)\s)?(?:(?P<hardware>\S+)\s)?\b(?P<os>\S+)\b$"
    )
    return pattern.search(command_output).groupdict()
