import re
from typing import Dict, Any


def parse_iostat(command_output: str) -> Dict[str, Any]:
    """Parse `iostat -x` command output."""
    avg_cpu_pattern = re.compile(r"(\d+\.\d+)")
    metadata_pattern = re.compile(
        r"(?P<os>[\s\S]+)\s\((?P<hostname>.+)\)\s+(?P<execute_date>\d+/\d+/\d+)"
        r"\s+(?P<architecture>\S+)\s+\((?P<available_cpu>\d+).+\)"
    )
    io_statistics_pattern = re.compile(
        r"(?P<Device>\w+)\s+(?P<tps>\S+)\s+"
        r"(?P<kB_read_s>\S+)\s+(?P<kB_wrtn_s>\S+)\s+(?P<kB_dscd_s>\S+)\s+"
        r"(?P<kB_read>\d+)\s+(?P<kB_wrtn>\d+)\s+(?P<kB_dscd>\d+)"
    )

    lines = [i.strip() for i in command_output.splitlines() if i.strip()]
    parsed_output = metadata_pattern.search(lines.pop(0)).groupdict()
    parsed_output["statistics"] = []
    while lines:
        line = lines.pop(0)
        if line.startswith("avg-cpu:"):
            user, nice, system, iowait, steal, idle = avg_cpu_pattern.findall(lines.pop(0))
            parsed_output["avg_cpu"] = {
                "user": user,
                "nice": nice,
                "system": system,
                "iowait": iowait,
                "steal": steal,
                "idle": idle,
            }
        else:
            regex_result = io_statistics_pattern.search(line)
            if regex_result:
                parsed_output["statistics"].append(regex_result.groupdict())
    return parsed_output
