import re


def parse_lsipc(command_output: str):
    """Parse `lsipc` command output."""
    pattern = re.compile(r"(?P<RESOURCE>\S+)\s+(?P<DESCRIPTION>.+)\s\s+(?P<LIMIT>\S+)\s+(?P<USED>\S+)\s+(?P<USE>\S+)")
    return [i.groupdict() for i in pattern.finditer(command_output)]
