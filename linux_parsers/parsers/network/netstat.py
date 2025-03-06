import re
from typing import Any

"Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name"


def parse_netstat(command_output: str) -> list[dict[str, str | Any]]:
    """Parse `netstat -tulpan` command output."""
    record_pattern = re.compile(
        "(?P<Proto>\w+)\s+"
        "(?P<RecvQ>\d+)\s+"
        "(?P<SendQ>\d+)\s+"
        "(?P<LocalAddress>\S+:\S+)\s+"
        "(?P<ForeignAddress>\S+:\S+)\s+"
        "(?:(?P<State>[-_A-Z]+))?\s+"
        "(?:(?P<PID>\d+)/(?P<ProgramName>\w+))?"
    )
    return [record.groupdict() for record in record_pattern.finditer(command_output)]
