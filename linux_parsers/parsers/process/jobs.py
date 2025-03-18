import re

from typing import List, Dict, Optional


def parse_jobs(command_output: str) -> List[Dict[str, Optional[str]]]:
    """Parse `jobs` command output."""
    pattern = re.compile(r"\[\d](?P<priority>[-+]?)\s(?P<job>.+)")
    return [i.groupdict() for i in pattern.finditer(command_output)]
