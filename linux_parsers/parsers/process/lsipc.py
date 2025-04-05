import re


def parse_lsipc(command_output: str):
    """Parse `lsipc` command output."""
    lsipc_records = []
    pattern = re.compile(
        r"(?P<resource>\S+)\s+"
        r"(?P<description>.+\S)\s+"
        r"(?P<limit>\d+\w*)\s+"
        r"(?P<used>\S+)\s+"
        r"(?P<use_percentage>\S+)$"
    )
    for line in command_output.strip().splitlines()[1:]:
        lsipc_records.append(pattern.search(line).groupdict())
    return lsipc_records
