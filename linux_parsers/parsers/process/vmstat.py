import re


def parse_vmstat(command_output: str) -> list[dict[str, str]]:
    """Parse `vmstat` command output."""
    pattern = re.compile(
        r"\s+(?P<r>\d+)\s+(?P<b>\d+)\s+(?P<swpd>\d+)\s+(?P<free>\d+)\s+(?P<buff>\d+)\s+"
        r"(?P<cache>\d+)\s+(?P<si>\d+)\s+(?P<so>\d+)\s+(?P<bi>\d+)\s+(?P<bo>\d+)\s+"
        r"(?P<in>\d+)\s+(?P<cs>\d+)\s+(?P<us>\d+)\s+(?P<sy>\d+)\s+(?P<id>\d+)\s+"
        r"(?P<wa>\d+)\s+(?P<st>\d+)\s+(?P<gu>\d+)"
    )
    return [i.groupdict() for i in pattern.finditer(command_output)]
