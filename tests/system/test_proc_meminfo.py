from linux_parsers.parsers.system.proc_meminfo import parse_proc_meminfo_file


def test_proc_meminfo():
    command_output = """MemTotal:        8075284 kB
MemFree:         7565888 kB
MemAvailable:    7523676 kB
Buffers:            9856 kB
Cached:           147924 kB
SwapCached:            0 kB
Active:            47056 kB
Inactive:         154732 kB
Active(anon):       2016 kB
Inactive(anon):    44560 kB
Active(file):      45040 kB
Inactive(file):   110172 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:       2097152 kB
SwapFree:        2097152 kB
Dirty:                 0 kB
Writeback:             0 kB
AnonPages:         44016 kB
Mapped:            78680 kB
Shmem:              2576 kB
KReclaimable:      23556 kB
Slab:              64276 kB
SReclaimable:      23556 kB
SUnreclaim:        40720 kB
KernelStack:        3008 kB
PageTables:         1752 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     6134792 kB
Committed_AS:     422796 kB
VmallocTotal:   34359738367 kB

"""
    parsed_output = parse_proc_meminfo_file(command_output)
    assert parsed_output['MemTotal'] == '8075284 kB'
    assert parsed_output['MemFree'] == '7565888 kB'
    assert parsed_output['MemAvailable'] == '7523676 kB'
    assert parsed_output['Buffers'] == '9856 kB'
    assert parsed_output['Cached'] == '147924 kB'
    assert parsed_output['SwapCached'] == '0 kB'