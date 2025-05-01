import re
from typing import List, Dict


def parse_var_log_dpkg(command_output: str) -> List[Dict[str, str]]:
    """Parse `/var/log/dpkg` file output."""
    pattern = re.compile(
        r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
        r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
        r"(?P<action>startup|install|configure|status)\s*"
        r"(?P<package>[^:\s]*:?[^ ]*)?\s*"
        r"(?P<dynamic_field1>[^ ]*)?\s*"
        r"(?P<dynamic_field2>[^ ]*)?"
    )
    parsed_command = []
    for line in command_output.splitlines():
        regex_result = re.match(pattern, line)
        if not regex_result:
            continue
        data = regex_result.groupdict()
        action = data["action"]

        parsed_log = {"date": data["date"], "time": data["time"], "action": action}

        if action == "startup":
            parsed_log["subsystem"] = data["package"]
            parsed_log["phase"] = data["dynamic_field1"]
        elif action == "install":
            parsed_log["package"] = data["package"]
            parsed_log["old_version"] = data["dynamic_field1"]
            parsed_log["new_version"] = data["dynamic_field2"]
        elif action == "configure":
            parsed_log["package"] = data["package"]
            parsed_log["version"] = data["dynamic_field1"]
            parsed_log["previous_version"] = data["dynamic_field2"]
        elif action == "status":
            parsed_log["status"] = data["dynamic_field1"]
            parsed_log["package"] = data["package"]
            parsed_log["version"] = data["dynamic_field2"]

        parsed_command.append(parsed_log)

    return parsed_command
