from linux_parsers.parsers.process.cgroups import parse_proc_cgroups_file, parse_proc_pid_cgroups_file


def test_proc_cgroups_file():
    command_output = """
#subsys_name    hierarchy       num_cgroups     enabled
cpuset  1       1       1
cpu     2       1       1
cpuacct 3       1       1
blkio   4       1       1
memory  5       1       1
devices 6       1       1
freezer 7       1       1
net_cls 8       1       1
perf_event      9       1       1
net_prio        10      1       1
hugetlb 11      1       1
pids    12      1       1
rdma    13      1       1
misc    14      1       1
    """
    parsed_output = parse_proc_cgroups_file(command_output)
    assert len(parsed_output) == 14
    assert parsed_output[0] == {'enabled': '1', 'hierarchy': '1', 'num_cgroups': '1', 'subsys_name': 'cpuset'}
    assert parsed_output[1] == {'enabled': '1', 'hierarchy': '2', 'num_cgroups': '1', 'subsys_name': 'cpu'}


def test_proc_pid_cgroups_file():
    command_output = """
14:misc:/
13:rdma:/
12:pids:/
11:hugetlb:/
10:net_prio:/
9:perf_event:/
8:net_cls:/
7:freezer:/
6:devices:/
5:memory:/
4:blkio:/
3:cpuacct:/
2:cpu:/
1:cpuset:/
0::/
"""
    parsed_output = parse_proc_pid_cgroups_file(command_output)
    assert len(parsed_output) == 15
    assert parsed_output[0]['controllers'] == 'misc'
    assert parsed_output[1]['controllers'] == 'rdma'
    assert parsed_output[2]['controllers'] == 'pids'
    assert parsed_output[3]['hierarchy'] == '11'
    assert parsed_output[4]['hierarchy'] == '10'