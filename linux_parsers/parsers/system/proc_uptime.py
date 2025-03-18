import re
from typing import Dict


def parse_proc_uptime_file(command_output: str) -> Dict[str, str]:
    """Parse `/proc/uptime` file output."""
    pattern = re.compile(r"^(?P<uptime>\d+\.\d+)\s+(?P<idle_time>\d+\.\d+)$")
    return pattern.search(command_output).groupdict()
