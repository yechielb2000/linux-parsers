import re


def parse_proc_cgroups_file(command_output: str) -> list[dict[str, any]]:
    """Parse `/proc/cgroups` file"""
    pattern = re.compile(r'(?P<subsys_name>\S+)\s+(?P<hierarchy>\d+)\s+(?P<num_cgroups>\d+)\s+(?P<enabled>\d+)')
    return [i.groupdict() for i in pattern.finditer(command_output)]


def parse_proc_pid_cgroups_file(command_output: str) -> list[dict[str, any]]:
    """Parse `/proc/<pid>/cgroups` file"""
    pattern = re.compile(r'^(?P<hierarchy>\d*):(?P<controllers>[^:]*):(?P<path>.*)$', re.MULTILINE)
    return [i.groupdict() for i in pattern.finditer(command_output)]
