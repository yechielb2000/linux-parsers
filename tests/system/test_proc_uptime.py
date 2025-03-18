from linux_parsers.parsers.system.proc_uptime import parse_proc_uptime_file


def test_proc_uptime():
    command_output = "17208.89 137256.50"
    parsed_output = parse_proc_uptime_file(command_output)
    assert parsed_output["uptime"] == "17208.89"
    assert parsed_output["idle_time"] == "137256.50"
