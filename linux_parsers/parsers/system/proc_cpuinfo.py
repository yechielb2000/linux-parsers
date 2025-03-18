from typing import List, Dict


def parse_proc_cpuinfo_file(command_output: str) -> List[Dict[str, str]]:
    """Parse `/proc/cpuinfo` file."""
    parsed_output = []
    processors = command_output.split("\n\n")
    for processor in processors:
        lines = processor.splitlines()
        parsed_processor = {}
        for line in lines:
            key, value = line.split(":")
            parsed_processor[key.strip()] = value.strip()
        parsed_output.append(parsed_processor)
    return parsed_output
