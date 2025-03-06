import re
from typing import Any


def parse_ss(command_output: str) -> list[dict[str, str | Any]]:
    """Parse `ss -tulnap` command output."""
    record_pattern = re.compile(
        "(?P<State>[-_A-Z]+)\s+"
        "(?P<RecvQ>\d+)\s+"
        "(?P<SendQ>\d+)\s+"
        "(?P<LocalAddress_Port>\S+:\S+)\s+"
        "(?P<PeerAddress_Port>\S+:\S+)\s+"
        "(?:(?P<Process>.+))?"
    )
    return [record.groupdict() for record in record_pattern.finditer(command_output)]
