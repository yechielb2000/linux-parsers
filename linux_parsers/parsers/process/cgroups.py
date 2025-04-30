import re

from typing import List, Dict, Any


def parse_proc_cgroups_file(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/proc/cgroups` file"""
    pattern = re.compile(r"(?P<subsys_name>\S+)\s+(?P<hierarchy>\d+)\s+(?P<num_cgroups>\d+)\s+(?P<enabled>\d+)")
    return [i.groupdict() for i in pattern.finditer(command_output)]


def parse_proc_pid_cgroups_file(command_output: str) -> List[Dict[str, Any]]:
    """Parse `/proc/<pid>/cgroups` file"""
    pattern = re.compile(r"^(?P<hierarchy>\d*):(?P<controllers>[^:]*):(?P<path>.*)$", re.MULTILINE)
    return [i.groupdict() for i in pattern.finditer(command_output)]


def parse_cgroup_pid_list(command_output: str) -> List[str]:
    """Parse `cat /sys/fs/cgroup/<controller>/<cgroup_path>/cgroup.procs` file."""
    return command_output.splitlines()


def parse_systemd_cgls(command_output: str) -> Dict[Any, Any]:
    """Parse `systemd-cgls [-al]`"""
    lines = command_output.splitlines()
    stack = []
    parsed_command = {}
    while lines:
        line = lines.pop(0)
        if not line.strip():
            continue

        # Remove control group line
        regex_result = re.match(r"[Cc][\w\s]+/:", line)
        if regex_result:
            continue

        # Detect indent and clean line
        indent = len(line) - len(line.lstrip("│├└ "))
        line = line.strip("│├└─ ")

        # Extract PID and command if present
        regex_result = re.search(r"(\d+)\s+(.*)", line)
        if regex_result:
            pid, cmd = regex_result.groups()
            entry = {pid: cmd}
        else:
            entry = {line: {}}

        # Navigate stack
        while stack and stack[-1][0] >= indent:
            stack.pop()

        if not stack:
            parent = parsed_command
        else:
            parent = stack[-1][1]

        key = next(iter(entry))
        parent[key] = entry[key]

        # Only push dicts (not PID/command leaves) to stack
        if isinstance(entry[key], dict):
            stack.append((indent, entry[key]))

    return parsed_command
