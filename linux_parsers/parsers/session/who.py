import re
from typing import Dict, Any


def parse_who_a(command_output: str) -> Dict[str, Any]:
    """Parse `who -a` command output."""
    user_record_pattern = re.compile(
        r"(?P<user>\S+)\s+(?P<tty>\S+)\s+(?P<date>\w+-\d+-\d+)\s(?P<time>\S+)\s+\((?P<from>.+)\)"
    )
    system_event_pattern = re.compile(r"(?P<event>.+)\b\s+(?P<date>\w+-\d+-\d+)\s(?P<time>\S+)")
    parsed_output = {"users_records": [], "system_records": {}}
    lines = command_output.splitlines()
    while lines:
        line = lines.pop(0)
        regex_result = user_record_pattern.search(line)
        if regex_result:
            parsed_output["users_records"].append(regex_result.groupdict())
            continue
        regex_result = system_event_pattern.search(line)
        if regex_result:
            event = regex_result.groupdict()
            parsed_output["system_records"][event["event"]] = event
    return parsed_output
