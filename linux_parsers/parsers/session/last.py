import re


def parse_last(command_output: str) -> list[dict[str, any]]:
    """Parse `last` command output."""
    pattern = re.compile(
        r'(?P<user>\S+)\s+(?P<tty>\S+)\s+(\S+)\s+(?P<date>\w+\s\w+\s\d+\s\S+)\s+'
        r'(?:-\s(?P<start>\S+)\s+\((?P<end>\S+)\))?(?P<status>.+)?'
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
