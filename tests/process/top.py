from linux_parsers.parsers.process.top import parse_top


def test_top():
    command_output = """
top - 15:42:54 up  1:42,  0 user,  load average: 0.00, 0.00, 0.00
Tasks:   9 total,   1 running,   8 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  0.2 sy,  0.0 ni, 99.5 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
MiB Mem :   7886.0 total,   7479.7 free,    486.9 used,     98.0 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   7399.1 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   10 a         20   0   32700   5736   4720 S   0.7   0.1   0:19.83 ijent
    1 root      20   0    2616   1748   1636 S   0.0   0.0   0:00.02 init(kali-linux
    5 root      20   0    2616      4      0 S   0.0   0.0   0:00.00 init
    8 root      20   0    2624    120      0 S   0.0   0.0   0:00.00 SessionLeader
    9 root      20   0    2624    128      0 S   0.0   0.0   0:00.00 Relay(10)
 5950 root      20   0    2624    120      0 S   0.0   0.0   0:00.00 SessionLeader
 5951 root      20   0    2624    128      0 S   0.0   0.0   0:00.11 Relay(5952)
 5952 a         20   0    7544   4284   3444 S   0.0   0.1   0:00.17 bash
13450 a         20   0    9168   4712   2632 R   0.0   0.1   0:00.01 top

    
"""
    parsed_command = parse_top(command_output)
    assert parsed_command