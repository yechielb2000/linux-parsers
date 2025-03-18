from linux_parsers.parsers.system.mpstat import parse_mpstat


def test_mpstat():
    command_output = """
Linux 5.15.167.4-microsoft-standard-WSL2 (a)    03/11/2025      _x86_64_        (8 CPU)

10:54:43 PM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
10:54:43 PM    3    0.05    0.00    0.10    0.00    0.00    0.01    0.00    0.00    0.00   99.85
10:54:43 PM    4    0.06    0.00    0.12    0.01    0.00    0.00    0.00    0.00    0.00   99.81
10:54:43 PM    5    0.03    0.00    0.11    0.00    0.00    0.00    0.00    0.00    0.00   99.86
10:54:43 PM    6    0.05    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.84
10:54:43 PM    7    0.03    0.00    0.08    0.00    0.00    0.00    0.00    0.00    0.00   99.89
08:00:01     all     2.40    0.00    1.20     0.50   0.00    0.10     0.00     0.00     0.00    95.80    

"""
    parsed_command = parse_mpstat(command_output)
    assert parsed_command["hostname"] == "a"
    assert parsed_command["os"] == "Linux 5.15.167.4-microsoft-standard-WSL2"
    assert len(parsed_command["statistics"]) == 6
    assert parsed_command["statistics"][0]["time"] == "10:54:43 PM"
    assert parsed_command["statistics"][1]["cpu"] == "4"
    assert parsed_command["statistics"][2]["nice"] == "0.00"
    assert parsed_command["statistics"][3]["idle"] == "99.84"
