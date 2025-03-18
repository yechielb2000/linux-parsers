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
