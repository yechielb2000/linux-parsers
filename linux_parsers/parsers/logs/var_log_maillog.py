import re
from typing import List, Dict, Any


def parse_var_log_maillog(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/var/log/maillog` output file."""
    pattern = re.compile(
        r"(?P<month>\w+)\s"
        r"(?P<day>\d+)\s+"
        r"(?P<time>\d+:\d+:\d+)\s+"
        r"(?P<hostname>\S+)\s"
        r"(?P<process>[^\[]+)(?:\[(?P<pid>\d+)])?:\s+"
        r"(?P<message>.+)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
