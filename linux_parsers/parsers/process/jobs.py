import re


def parse_jobs(command_output: str) -> list[dict[str, str | None]]:
    """Parse `jobs` command output."""
    pattern = re.compile(r"\[\d](?P<priority>[-+]?)\s(?P<job>.+)")
    return [i.groupdict() for i in pattern.finditer(command_output)]
