import re
from typing import List, Dict, Any


def parse_var_log_syslog(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/var/log/syslog` file content."""

    pattern = re.compile(
        r"(?P<month>\w+)\s+"
        r"(?P<day>\d+)\s"
        r"(?P<time>\d+:\d+:\d+)\s"
        r"(?P<host>\S+)\s"
        r"(?P<process>[^\s\[]+)"
        r"(?:\[(?P<pid>\d+)])?:\s+"
        r"(?P<message>.*)$",
        flags=re.MULTILINE,
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
