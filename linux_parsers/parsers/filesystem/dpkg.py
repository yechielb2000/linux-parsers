import re


def parse_dpkg_l(command_output: str) -> list[dict[str, any]]:
    """Parse `dpkg -l` command output."""
    pattern = re.compile(r'ii\s+(?P<name>\S+)\s+(?P<version>\S+)\s+(?P<arch>\S+)\s+(?P<description>.+)', re.MULTILINE)
    return [i.groupdict() for i in pattern.finditer(command_output)]
