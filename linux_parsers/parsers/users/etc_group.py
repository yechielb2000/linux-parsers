import re


def parse_etc_group_file(command_output: str) -> list[dict[str, any]]:
    """Parse `/etc/group` file output."""
    pattern = re.compile(r'^(?P<group_name>[^:]+):(?P<password>[^:]*):(?P<gid>\d+):(?P<members>[^:]*)$', re.MULTILINE)
    return [i.groupdict() for i in pattern.finditer(command_output)]
