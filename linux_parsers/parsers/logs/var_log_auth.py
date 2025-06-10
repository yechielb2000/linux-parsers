import re
from typing import List, Dict


def parse_var_log_auth(command_output: str) -> List[Dict[str, str]]:
    """Parse `/var/log/auth.log` output file."""
    pattern = re.compile(
        r"(?P<timestamp>\w{3}\s\d+\s\d+:\d+:\d+)\s+"
        r"(?P<hostname>\S+)\s+"
        r"(?P<event>[^:]+):\s+"
        r"(?P<message>.+)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
