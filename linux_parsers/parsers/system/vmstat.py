import re

from typing import Dict, List, Any


def parse_vmstat(command_output: str) -> List[Dict[str, Dict]]:
    """Parse `vmstat` command output."""
    pattern = re.compile(
        r"\s+(?P<r>\d+)\s+(?P<b>\d+)\s+(?P<swpd>\d+)\s+(?P<free>\d+)\s+(?P<buff>\d+)\s+"
        r"(?P<cache>\d+)\s+(?P<si>\d+)\s+(?P<so>\d+)\s+(?P<bi>\d+)\s+(?P<bo>\d+)\s+"
        r"(?P<in>\d+)\s+(?P<cs>\d+)\s+(?P<us>\d+)\s+(?P<sy>\d+)\s+(?P<id>\d+)\s+"
        r"(?P<wa>\d+)\s+(?P<st>\d+)\s+(?P<gu>\d+)"
    )
    parsed_command = []
    for record in pattern.finditer(command_output):
        record = record.groupdict()
        parsed_command.append(
            {
                "procs": {"r": record["r"], "b": record["b"]},
                "memory": {
                    "swpd": record["swpd"],
                    "free": record["free"],
                    "buff": record["buff"],
                    "cache": record["cache"],
                },
                "swap": {"si": record["si"], "so": record["so"]},
                "io": {"bi": record["bi"], "bo": record["bo"]},
                "system": {"in": record["in"], "cs": record["cs"]},
                "cpu": {
                    "us": record["us"],
                    "sy": record["sy"],
                    "id": record["id"],
                    "wa": record["wa"],
                    "st": record["st"],
                    "gu": record["gu"],
                },
            }
        )
    return parsed_command


def parse_vmstat_adt(command_output: str) -> Dict[str, Any]:
    """Parse `vmstat -adt` command output."""
    pattern = re.compile(
        r"(?P<disk>\S+)\s+"
        r"(?P<r_total>\d+)\s+(?P<r_merged>\d+)\s+(?P<r_sectors>\d+)\s+(?P<r_ms>\d+)\s+"
        r"(?P<w_total>\d+)\s+(?P<w_merged>\d+)\s+(?P<w_sectors>\d+)\s+(?P<w_ms>\d+)\s+"
        r"(?P<cur>\d+)\s+(?P<sec>\d+)\s+"
        r"(?P<ist>.+)"
    )
    parsed_command = {}

    for record in pattern.finditer(command_output):
        record = record.groupdict()
        parsed_command[record["disk"]] = {
            "reads": {
                "total": record["r_total"],
                "merged": record["r_merged"],
                "sectors": record["r_sectors"],
                "ms": record["w_ms"],
            },
            "writes": {
                "total": record["w_total"],
                "merged": record["w_merged"],
                "sectors": record["w_sectors"],
                "ms": record["w_ms"],
            },
            "io": {
                "cur": record["cur"],
                "sec": record["sec"],
            },
            "timestamp": record["ist"],
        }
    return parsed_command
