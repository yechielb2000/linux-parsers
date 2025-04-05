from linux_parsers.parsers.process.lsipc import parse_lsipc


def test_lsipc():
    command_output = """
RESOURCE DESCRIPTION                                              LIMIT USED  USE%
MSGMNI   Number of message queues                                 32000    0 0.00%
MSGMAX   Max size of message (bytes)                                 8K    -     -
MSGMNB   Default max size of queue (bytes)                          16K    -     -
SHMMNI   Shared memory segments                                    4096    0 0.00%
SHMALL   Shared memory pages                       18446744073692774399    0 0.00%    
"""
    parsed_command = parse_lsipc(command_output)
    assert len(parsed_command) == 5
    assert parsed_command[0]["resource"] == "MSGMNI"
    assert parsed_command[0]["limit"] == "32000"
    assert parsed_command[0]["used"] == "0"
    assert parsed_command[0]["use_percentage"] == "0.00%"
