import re
from collections import defaultdict
from typing import List, Dict, Any, Union


def parse_ldd(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ldd <program>` command output."""
    pattern = re.compile(r"\s*(?P<program>\S+)\s+(?:=>\s(?P<path>\S+)\s+)?\((?P<address>\S+)\)")
    return [i.groupdict() for i in pattern.finditer(command_output)]


def parse_ldd_verbose(command_output: str) -> Dict[str, Union[List, Dict]]:
    """Parse `ldd -v <program>` command output."""
    library_pattern = re.compile(r"\s*(?P<program>\S+)\s+(?:=>\s(?P<path>\S+)\s+)?\((?P<address>\S+)\)")
    version_pattern = re.compile(r"\s*(?P<dependency>\S+)\s+\(GLIBC_(?P<version>\S+)\)\s+=>\s+(?P<resolved_path>.+)")
    lines = command_output.splitlines()
    parsing_versions = False
    current_lib = None
    parsed_output = {"libraries": [], "versions": defaultdict(list)}
    while lines:
        line = lines.pop(0)
        if line.strip() == "Version information:":
            parsing_versions = True
            continue
        if parsing_versions:
            match_lib = re.match(r"\s*(\S+):", line)
            if match_lib:
                current_lib = match_lib.group(1)
                continue
            regex_result = version_pattern.search(line)
            if regex_result:
                parsed_output["versions"][current_lib].append(regex_result.groupdict())
        else:
            regex_result = library_pattern.search(line)
            if regex_result:
                parsed_output["libraries"].append(regex_result.groupdict())
    return parsed_output


def parse_ldd_version(command_output: str) -> List[Dict[str, Any]]:
    """Parse `ldd --version` command output."""
    regex_result = re.search(r"(\d+\.\d+)", command_output)
    return regex_result.groups()[0] if regex_result else None
