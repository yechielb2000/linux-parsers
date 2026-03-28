import re
from typing import Dict, Any

from linux_parsers.parsers.exceptions import UnexpectedParseException


def parse_ping(command_output: str) -> Dict[str, Any]:
    """Parse `ping` command output."""
    rtt_pattern = re.compile(r".+=\s(?P<min>\S+)/(?P<avg>\S+)/(?P<max>\S+)/(?P<mdev>.+)")
    header_pattern = re.compile(
        r"PING\s(?P<target>\S+)\s\((?P<resolvedIp>\S+)\)\s(?P<payloadSize>\d+)\((?P<totalPacketSize>\d+)\).+"
    )
    record_pattern = re.compile(
        r"(:?(?P<replaySize>\d+)\sbytes\sfrom\s(?P<from>\S+):\s)?"
        r"icmp_seq=(?P<icmpSeq>\d+)"
        r"(?:\sttl=(?P<ttl>\d+)\stime=(.+))?"
    )
    statistics_pattern = re.compile(
        r"(?P<transmitted>\d+)\spackets\stransmitted,\s"
        r"(?P<received>\d+)\sreceived,\s"
        r"(?P<loss>\d+)%\spacket\sloss,\stime\s"
        r"(?P<time>\d+ms)"
    )
    lines = list(filter(lambda x: x.strip(), command_output.splitlines()))
    parsed_command = header_pattern.search(lines[0]).groupdict()
    parsed_command["records"] = []
    while lines:
        line = lines.pop(0)
        if "bytes from" in line:
            parsed_command["records"].append(record_pattern.search(line).groupdict())
        if "rtt" in line:
            regex_result = rtt_pattern.search(line)
            if not regex_result:
                raise UnexpectedParseException(f"rtt pattern failed: {rtt_pattern}\n{command_output}")
            parsed_command["rtt"] = regex_result.groupdict()
        if "packets transmitted" in line:
            regex_result = statistics_pattern.search(line)
            if not regex_result:
                raise UnexpectedParseException(f"statistics pattern failed: {statistics_pattern}\n{command_output}")
            parsed_command["statistics"] = regex_result.groupdict()
    return parsed_command
