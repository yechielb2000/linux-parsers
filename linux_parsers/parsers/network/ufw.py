import re

from typing import List, Dict, Any


def parse_ufw_app_list(command_output: str) -> List[str]:
    """Parse `ufw app list` command output."""
    return command_output.splitlines()


def parse_ufw_status(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ufw status` command output."""
    record_pattern = re.compile("(?P<To>\S+(?:\s\(v6\))?)\s+(?P<Action>[A-Z]+)\s+(?P<From>\w+(?:\s\(v6\))?)")
    return [i.groupdict() for i in record_pattern.finditer(command_output)]
