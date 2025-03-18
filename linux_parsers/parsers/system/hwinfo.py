import re

from typing import List, Dict


def parse_hwinfo(command_output: str) -> List[Dict]:
    """Parse `hwinfo --<action>` command outputs.
    CPU	                 hwinfo --cpu
    Memory (RAM)	     hwinfo --memory
    Disks (HDD/SSD)	     hwinfo --disk
    Network Interfaces	 hwinfo --network
    USB Devices	         hwinfo --usb
    GPU (Graphics)	     hwinfo --gfxcard
    Bluetooth	         hwinfo --bluetooth
    """
    blocks = re.split(r"^\d+:", command_output, flags=re.MULTILINE)
    parsed_command = []
    for block in list(filter(str.strip, blocks)):
        fields = [i.strip() for i in block.splitlines() if i.strip()][2:]
        block_fields = {}
        for field in fields:
            key, value = field.split(":")
            block_fields[key.strip()] = value.strip()
        parsed_command.append(block_fields)
    return parsed_command
