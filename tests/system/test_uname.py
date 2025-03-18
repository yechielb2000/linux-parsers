from linux_parsers.parsers.system.uname import parse_uname_a


def test_uname_a():
    command_output = "Linux hst 5.15.167.4-microsoft-standard-WSL2 #1 SMP Tue Nov 5 00:21:55 UTC 2024 x86_64 GNU/Linux"
    parsed_output = parse_uname_a(command_output)
    assert parsed_output["kernel"] == "Linux"
    assert parsed_output["hostname"] == "hst"
    assert parsed_output["smp"] == "SMP"
    assert parsed_output["os"] == "GNU/Linux"
