import re

from typing import List, Dict, Any


def parse_netstat(command_output: str) -> List[Dict[str, Any]]:
    """Parse `netstat -tulpan` command output."""
    record_pattern = re.compile(
        r"(?P<Proto>\w+)\s+"
        r"(?P<RecvQ>\d+)\s+"
        r"(?P<SendQ>\d+)\s+"
        r"(?P<LocalAddress>\S+:\S+)\s+"
        r"(?P<ForeignAddress>\S+:\S+)\s+"
        r"(?:(?P<State>[-_A-Z]+))?\s+"
        r"(?:(?P<PID>\d+)/(?P<ProgramName>\w+))?"
    )
    return [record.groupdict() for record in record_pattern.finditer(command_output)]
