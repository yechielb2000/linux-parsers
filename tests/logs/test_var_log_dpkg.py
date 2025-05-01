from linux_parsers.parsers.logs.var_log_dpkg import parse_var_log_dpkg


def test_var_log_dpkg():
    command_output = """
2025-04-05 19:57:23 status installed libc-bin:amd64 2.40-3
2025-04-05 20:05:56 startup archives unpack
2025-04-05 20:05:56 install acct:amd64 <none> 6.6.4-5+b3
2025-04-05 20:05:56 status half-installed acct:amd64 6.6.4-5+b3
2025-04-05 20:05:56 status unpacked acct:amd64 6.6.4-5+b3
2025-04-05 20:05:57 startup packages configure
2025-04-05 20:05:57 configure acct:amd64 6.6.4-5+b3 <none>
2025-04-05 20:05:57 status unpacked acct:amd64 6.6.4-5+b3
2025-04-05 20:05:57 status half-configured acct:amd64 6.6.4-5+b3
2025-04-05 20:05:57 status installed acct:amd64 6.6.4-5+b3
"""
    parsed_output = parse_var_log_dpkg(command_output)
    assert parsed_output[0] == {
        "action": "status",
        "date": "2025-04-05",
        "package": "installed",
        "status": "libc-bin:amd64",
        "time": "19:57:23",
        "version": "2.40-3",
    }
    assert parsed_output[2] == {
        "action": "install",
        "date": "2025-04-05",
        "new_version": "6.6.4-5+b3",
        "old_version": "<none>",
        "package": "acct:amd64",
        "time": "20:05:56",
    }
    assert parsed_output[7] == {
        "action": "status",
        "date": "2025-04-05",
        "package": "unpacked",
        "status": "acct:amd64",
        "time": "20:05:57",
        "version": "6.6.4-5+b3",
    }
