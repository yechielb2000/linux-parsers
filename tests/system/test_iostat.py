from linux_parsers.parsers.system.iostat import parse_iostat


def test_iostat():
    command_output = """

Linux 5.15.167.4-microsoft-standard-WSL2 (a)    03/11/2025      _x86_64_        (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.05    0.00    0.15    0.01    0.00   99.79

Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
sda               0.36        24.32         0.00         0.00      73113          0          0
sdb               0.02         0.39         0.00         0.00       1184          4          0
sdc               0.39         7.05         3.23         2.06      21189       9724       6200
    
"""
    parsed_command = parse_iostat(command_output)
    assert parsed_command["os"] == "Linux 5.15.167.4-microsoft-standard-WSL2"
    assert parsed_command["execute_date"] == "03/11/2025"
    assert parsed_command["architecture"] == "_x86_64_"
    assert len(parsed_command["statistics"]) == 3
    assert parsed_command["statistics"][0]["kB_read_s"] == "24.32"
    assert parsed_command["statistics"][0]["Device"] == "sda"
    assert parsed_command["avg_cpu"] == {
        "idle": "99.79",
        "iowait": "0.01",
        "nice": "0.00",
        "steal": "0.00",
        "system": "0.15",
        "user": "0.05",
    }
