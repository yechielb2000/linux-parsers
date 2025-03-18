import re

from typing import List, Dict, Any


def parse_mount(command_output: str) -> List[Dict[str, Any]]:
    """Parse command output of `cat /proc/mounts` or `mount`."""
    pattern = re.compile(
        r"(?P<device>\S+)\s+"
        r"(?P<mount_point>\S+)\s+"
        r"(?P<filesystem_type>\S+)\s+"
        r"(?P<mount_options>\S+)\s+"
        r"(?P<dump>\d+)\s+"
        r"(?P<pass>\d+)"
    )
    parsed_command = []
    for i in pattern.finditer(command_output):
        record = i.groupdict()
        record["mount_options"] = record["mount_options"].split(",")
        parsed_command.append(record)
    return parsed_command
