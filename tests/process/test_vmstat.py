from linux_parsers.parsers.process.vmstat import parse_vmstat


def test_vmstat():
    command_output = """
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 1  0      0 7641168   1196 104604    0    0    23     4   48    0  0  0 100  0  0  0    
"""
    parsed_command = parse_vmstat(command_output)
    assert len(parsed_command) == 1
    assert parsed_command[0]['b'] == '0'
    assert parsed_command[0]['free'] == '7641168'
    assert parsed_command[0]['cs'] == '0'
    assert parsed_command[0]['cache'] == '104604'
