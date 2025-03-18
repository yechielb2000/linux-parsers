import re

from typing import Dict, Any


def parse_top(command_output: str) -> Dict[str, Any]:
    """Parse `top` command output."""
    parsed_command = {}
    lines = [i.strip() for i in command_output.splitlines() if i.strip()]
    system_pattern = re.compile(
        r"top\s-\s(?P<system_time>\d+:\d+:\d+)\D+(?P<uptime>.+),\s+(?P<users>\d+)\s+users?\D+"
        r"(?P<avg_1_min>[^,]+),\s(?P<avg_5_min>[^,]+),\s(?P<avg_15_min>.+)"
    )
    process_record_pattern = re.compile(
        r"(?P<pid>\d+)\s+(?P<user>\S+)\s+(?P<pr>\d+)\s+(?P<ni>\d+)\s+(?P<virt>\d+)\s+(?P<res>\d+)\s+"
        r"(?P<shr>\d+)\s+(?P<s>\w+)\s+(?P<cpu>[\d.]+)\s+(?P<mem>[\d.]+)\s+(?P<time>[\d.:]+)\s+(?P<command>.+)"
    )
    parsed_command["process_list"] = []
    while lines:
        line = lines.pop(0)
        if line.startswith("top"):
            parsed_command["system"] = system_pattern.search(line).groupdict()
        elif line.startswith("Tasks:"):
            to, ru, sl, st, zo = re.findall(r"(\d+)", line)
            parsed_command["tasks"] = dict(total=to, running=ru, sleeping=sl, stopped=st, zombie=zo)
        elif line.startswith("%Cpu"):
            us, sy, ni, id_, wa, hi, si, st = re.findall(r"(\d+.\d+)", line)
            parsed_command["cpu"] = dict(us=us, sy=sy, ni=ni, id=id_, wa=wa, hi=hi, si=si, st=st)
        elif line.startswith("MiB Mem"):
            to, fr, us, ca = re.findall(r"(\d+.\d+)", line)
            parsed_command["mem"] = dict(total=to, free=fr, used=us, cache=ca)
        elif line.startswith("MiB Swap"):
            to, fr, us, av = re.findall(r"(\d+.\d+)", line)
            parsed_command["swap"] = dict(total=to, free=fr, used=us, avail_mem=av)
        else:
            regex_result = process_record_pattern.search(line)
            if regex_result:
                parsed_command["process_list"].append(regex_result.groupdict())
    return parsed_command
