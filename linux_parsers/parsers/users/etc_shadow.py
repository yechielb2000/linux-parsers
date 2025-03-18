import re
from typing import List, Dict, Any


def parse_etc_shadow_file(command_output: str) -> List[Dict[str, Any]]:
    """Parse /etc/shadow file"""
    pattern = re.compile(
        r"(?P<username>[a-zA-Z0-9_]+):\$6\$(?P<salt>[^$]+)\$(?P<password_hash>[^:]+):"
        r"(?P<last_change>\d+):(?P<min_days>\d*):(?P<max_days>\d+):(?P<warning_days>\d+):"
        r"(?P<inactive_days>\d*):(?P<expiration_date>\d*):(?P<reserved>.*)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
