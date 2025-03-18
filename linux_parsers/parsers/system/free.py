import re

from typing import Dict, Any


def parse_free_btlv(command_output: str) -> Dict[str, Dict[str, Any]]:
    """Parse `free -btlv` command output."""
    pattern = re.compile(
        r"\D+(?P<total>\d+)\s+(?P<used>\d+)\s+(?P<free>\d+)\s*(?P<shared>\d+)?\s*"
        r"(?P<cache>\d+)?\s*(?P<available>\d+)?\s*"
    )
    lines = [i.strip() for i in command_output.splitlines() if i.strip()][1:]
    return {
        "Mem": pattern.search(lines.pop(0)).groupdict(),
        "Low": pattern.search(lines.pop(0)).groupdict(),
        "High": pattern.search(lines.pop(0)).groupdict(),
        "Swap": pattern.search(lines.pop(0)).groupdict(),
        "Total": pattern.search(lines.pop(0)).groupdict(),
        "Comm": pattern.search(lines.pop(0)).groupdict(),
    }
