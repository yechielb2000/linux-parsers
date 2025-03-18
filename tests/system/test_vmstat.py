from linux_parsers.parsers.system.vmstat import parse_vmstat, parse_vmstat_adt


def test_vmstat():
    command_output = """
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 1  0      0 7641168   1196 104604    0    0    23     4   48    0  0  0 100  0  0  0    
"""
    parsed_command = parse_vmstat(command_output)
    assert len(parsed_command) == 1
    assert parsed_command[0]["procs"] == {"b": "0", "r": "1"}
    assert parsed_command[0]["io"] == {"bi": "23", "bo": "4"}
    assert parsed_command[0]["cpu"] == {
        "gu": "0",
        "id": "100",
        "st": "0",
        "sy": "0",
        "us": "0",
        "wa": "0",
    }
    assert parsed_command[0]["system"] == {"cs": "0", "in": "48"}


def test_vmstat_adt():
    command_output = """
disk- ------------reads------------ ------------writes----------- -----IO------ -----timestamp-----
       total merged sectors      ms  total merged sectors      ms    cur    sec                 IST
ram0       0      0       0       0      0      0       0       0      0      0 2025-03-09 00:37:47
ram1       0      0       0       0      0      0       0       0      0      0 2025-03-09 00:37:47
ram2       0      0       0       0      0      0       0       0      0      0 2025-03-09 00:37:47
ram5       0      0       0       0      0      0       0       0      0      0 2025-03-09 00:37:47
    """
    parsed_command = parse_vmstat_adt(command_output)
    assert parsed_command["ram0"]["reads"]["total"] == "0"
    assert parsed_command["ram0"]["writes"]["merged"] == "0"
    assert parsed_command["ram1"]["reads"]["total"] == "0"
    assert parsed_command["ram1"]["writes"]["merged"] == "0"
