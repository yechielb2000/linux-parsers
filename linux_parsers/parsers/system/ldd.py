import re
from typing import List, Dict, Any


def parse_ldd(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ldd <program>` command output."""
    pattern = re.compile(r"\s*(?P<program>\S+)\s+(?:=>\s(?P<path>\S+)\s+)?\((?P<address>\S+)\)")
    return [i.groupdict() for i in pattern.finditer(command_output)]


def parse_ldd_verbose(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ldd -v <program>` command output."""
    pass


def parse_ldd_version(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ldd --version` command output."""
    pass
