import re

from typing import Dict, Any


def parse_stat(command_output: str) -> Dict[str, Any]:
    """Parse the output of `stat` command."""
    storage_pattern = re.compile(
        r"Size:\s(?P<size>\d+)\s+"
        r"Blocks:\s(?P<blocks>\d+)\s+"
        r"IO\sBlock:\s(?P<io_block>\d+)\s+"
        r"(?P<type>.+)"
    )
    metadata_pattern = re.compile(
        r"Device:\s(?P<device>\S+)\s+"
        r"Inode:\s(?P<inode>\d+)\s+"
        r"Links:\s(?P<links>\d+)"
    )
    permissions_pattern = re.compile(
        "Access:\s\((?P<octal>\d+)/(?P<symbolic>[-rwxd]+)\)\s+"
        "Uid:\s\(\s+(?P<uid>\d+)/\s+(?P<user>\S+)\)\s+"
        "Gid:\s\(\s+(?P<gid>\d+)/\s+(?P<group>\S+)\)"
    )
    time_pattern = re.compile(r"\w+:\s+(.+)")
    parsed_command = {}
    lines = [i.strip() for i in command_output.splitlines() if i.strip()]
    parsed_command["file"] = lines.pop(0).split(":")[1].strip()
    while lines:
        line = lines.pop(0)
        if line.startswith("Size:"):
            parsed_command.update(storage_pattern.search(line).groupdict())
        elif line.startswith("Device:"):
            parsed_command.update(metadata_pattern.search(line).groupdict())
        elif "Uid" in line:
            parsed_command["permissions"] = permissions_pattern.search(line).groupdict()
        elif line.startswith("Access:"):
            parsed_command["access"] = time_pattern.search(line).groups()[0]
        elif line.startswith("Modify:"):
            parsed_command["modify"] = time_pattern.search(line).groups()[0]
        elif line.startswith("Change:"):
            parsed_command["change"] = time_pattern.search(line).groups()[0]
        elif line.startswith("Birth:"):
            parsed_command["birth"] = time_pattern.search(line).groups()[0]
    return parsed_command
