import re
from typing import List, Dict, Any


def parse_var_log_cron(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/var/log/cron` output file."""
    pattern = re.compile(
        r"(?P<month>\w{3})\s+"
        r"(?P<day>\d{1,2})\s+"
        r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
        r"(?P<host>\S+)\s+CROND\["
        r"(?P<pid>\d+)]:\s+\("
        r"(?P<user>[^)]+)\)\s+CMD\s+\("
        r"(?P<command>.+)\)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
