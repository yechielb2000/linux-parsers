import re

from typing import Dict, Any


def parse_fdisk(command_output: str) -> Dict[str, Any]:
    """Parse `fdisk -l` command output."""
    partition_entry_pattern = re.compile(
        "(?P<partition>/dev/\S+)\s+"
        "(?P<start>[\d*]+)\s+"
        "(?P<end>\d+)\s+"
        "(?P<total>\d+)\s+"
        "(?P<size>\S+)\s+"
        "(?P<filesystem>.+)"
    )
    disk_blocks = re.split(r"(?=Disk /dev/)", command_output.strip())
    disk_blocks = list(filter(str.strip, disk_blocks))
    parsed_disks = {}
    for disk in disk_blocks:
        lines = list(filter(str.strip, disk.splitlines()))
        line = lines.pop(0)
        disk_info = re.search(r"Disk\s(/\S+):\s(.+),\s(.+),\s(.+)", line)
        name, size, in_bytes, in_sectors = disk_info.groups()
        size_value, size_name = size.split()
        parsed_disks[name] = {
            "info": {
                "name": name,
                size_name: size_value,
                "bytes": in_bytes.split()[0],
                "sectors": in_sectors.split()[0],
            },
            "notes": [],
            "partition_entries": [],
        }
        while lines:
            line = lines.pop(0).strip()
            if line.startswith("Disk model:"):
                parsed_disks[name]["model"] = line.split(":")[1].strip()
            elif line.startswith("Units:"):
                parsed_disks[name]["units"] = line.split(":")[1].strip()
            elif line.startswith("Sector size"):
                parsed_disks[name]["sector_size"] = line.split(":")[1].strip()
            elif line.startswith("I/O size"):
                parsed_disks[name]["io_size"] = line.split(":")[1].strip()
            elif line.startswith("Disklabel type:"):
                parsed_disks[name]["label_type"] = line.split(":")[1].strip()
            elif line.startswith("Disk identifier:"):
                parsed_disks[name]["identifier"] = line.split(":")[1].strip()
            elif line.startswith("**Warning") or line.startswith("**Error"):
                parsed_disks[name]["notes"].append(line)
            else:
                regex_result = partition_entry_pattern.search(line)
                if regex_result:
                    parsed_disks[name]["partition_entries"].append(regex_result.groupdict())
    return parsed_disks
