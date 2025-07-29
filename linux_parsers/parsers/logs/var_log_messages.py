import re
from typing import List, Dict


def parse_var_log_messages(command_output: str) -> List[Dict[str, str]]:
    """Parse content of `/var/log/messages`."""
    log_pattern = re.compile(
        r"^(?P<timestamp>\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+"
        r"(?P<host>\S+)\s+"
        r"(?P<process>[^\[:]+)(?:\[(?P<pid>\d+)\])?:\s+"
        r"(?P<message>.+)$"
    )
    entries = []
    for line in command_output.strip().splitlines():
        match = log_pattern.match(line)
        if match:
            entries.append(match.groupdict())
    return entries
