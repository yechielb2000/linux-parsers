import re

from typing import List, Dict, Any


def parse_ss_tulnap(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ss -tulnap` command output."""
    record_pattern = re.compile(
        "(?P<State>[-_A-Z]+)\s+"
        "(?P<RecvQ>\d+)\s+"
        "(?P<SendQ>\d+)\s+"
        "(?P<LocalAddress_Port>\S+:\S+)\s+"
        "(?P<PeerAddress_Port>\S+:\S+)\s+"
        "(?:(?P<Process>.+))?"
    )
    return [record.groupdict() for record in record_pattern.finditer(command_output)]


def parse_ss_s(command_output: str) -> Dict[str, Any]:
    """Parse `ss -s` command output."""
    lines = [i.strip() for i in command_output.splitlines() if i.strip()]
    parsed_command = re.search(r"\w+:\s+(?P<total>\d+)\s\(\w+\s+(?P<kernel>\d+)\)", lines.pop(0)).groupdict()
    tcp_total, estab, closed, orphaned, synrecv, timewait, can_handle = re.findall(r"\d+", lines.pop(0))
    parsed_command["TCP"] = {
        "tcp_total": tcp_total,
        "estab": estab,
        "closed": closed,
        "orphaned": orphaned,
        "synrecv": synrecv,
        "timewait": {"waiting": timewait, "can_handle": can_handle},
    }
    line = lines.pop(0)
    while not line.startswith("Transport Total"):
        protocol, protocol_total_transport = line.split(":")
        parsed_command[protocol] = protocol_total_transport.strip()
        line = lines.pop(0)
    parsed_command["transports"] = []
    while lines:
        regex_result = re.search("(?P<protocol>\w+)\s+(?P<total>\d+)\s+(?P<ip>\d+)\s+(?P<ipv6>\d+)", line)
        if regex_result:
            parsed_command["transports"].append(regex_result.groupdict())
        line = lines.pop(0)
    return parsed_command
