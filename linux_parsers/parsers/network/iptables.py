import re

from typing import Dict, List, Any


def parse_iptables(command_output: str) -> Dict[str, List[Any]]:
    """Parse `iptables -L -n -v` command output."""
    record_pattern = re.compile(
        r"^(?P<pkts>\d+)\s+"
        r"(?P<bytes>\d+)\s+"
        r"(?P<target>[A-Z]+)\s+"
        r"(?P<prot>\w+)\s+"
        r"(?P<opt>\S+)\s+"
        r"(?P<in>\S+)\s+"
        r"(?P<out>\S+)\s+"
        r"(?P<source>\S+/\d+)\s+"
        r"(?P<destination>\S+/\d+)\s+"
        r"(?P<rule>.+)?"
    )
    parsed_command = {}

    current_policy = None
    for line in command_output.splitlines():
        line = line.strip()
        if line.startswith("Chain"):
            policy = re.search(r"(?<=Chain\s)(\S+)", line).group()
            parsed_command[policy] = []
            current_policy = policy
            continue
        regex_result = re.search(record_pattern, line)
        if regex_result:
            parsed_command[current_policy].append(regex_result.groupdict())
    return parsed_command
