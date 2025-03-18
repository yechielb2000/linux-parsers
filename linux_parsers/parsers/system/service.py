import re

from typing import List, Dict, Any


def parse_service(command_output: str) -> List[Dict[str, Any]]:
    """Parse `service --status-all` command output."""
    status_map = {"+": "running", "-": "stopped", "?": "unknown"}
    parsed_output = []
    pattern = re.compile(r"^\s*\[\s(?P<status>[?+-])\s]\s+(?P<service>\S+)$")
    for line in command_output.splitlines():
        regex_result = pattern.search(line)
        if regex_result:
            parsed_output.append(
                {
                    "service": regex_result.group("service"),
                    "status": status_map[regex_result.group("status")],
                }
            )
    return parsed_output
