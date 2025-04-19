from linux_parsers.parsers.system.ldd import parse_ldd, parse_ldd_version, parse_ldd_verbose


def test_ldd():
    command_output = """
linux-vdso.so.1 (0x00007ffc8d1dc000)
        libjemalloc.so.2 => /lib/x86_64-linux-gnu/libjemalloc.so.2 (0x00007f52f9c89000)
        libisc-9.20.0-Debian.so => /lib/x86_64-linux-gnu/libisc-9.20.0-Debian.so (0x00007f52f9bf8000)
        libdns-9.20.0-Debian.so => /lib/x86_64-linux-gnu/libdns-9.20.0-Debian.so (0x00007f52f99bc000)
        libisccfg-9.20.0-Debian.so => /lib/x86_64-linux-gnu/libisccfg-9.20.0-Debian.so (0x00007f52f996e000)    
"""
    parsed_output = parse_ldd(command_output)
    assert len(parsed_output) == 5
    assert parsed_output[0] == {"address": "0x00007ffc8d1dc000", "path": None, "program": "linux-vdso.so.1"}
    assert parsed_output[4] == {
        "address": "0x00007f52f996e000",
        "path": "/lib/x86_64-linux-gnu/libisccfg-9.20.0-Debian.so",
        "program": "libisccfg-9.20.0-Debian.so",
    }


def test_ldd_version():
    command_output = """
ldd (GNU libc) 2.31
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Written by Roland McGrath and Ulrich Drepper.
"""
    parsed_output = parse_ldd_version(command_output)
    assert parsed_output == "2.31"


def test_ldd_verbose():
    command_output = """
        linux-vdso.so.1 (0x00007fff31cd9000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fded7548000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fded7670000)

        Version information:
        /bin/awk:
                libm.so.6 (GLIBC_2.38) => /lib/x86_64-linux-gnu/libm.so.6
                libm.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libm.so.6
                libc.so.6 (GLIBC_2.3) => /lib/x86_64-linux-gnu/libc.so.6
        /lib/x86_64-linux-gnu/libm.so.6:
                ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
                libc.so.6 (GLIBC_PRIVATE) => /lib/x86_64-linux-gnu/libc.so.6
        /lib/x86_64-linux-gnu/libc.so.6:
                ld-linux-x86-64.so.2 (GLIBC_2.35) => /lib64/ld-linux-x86-64.so.2
"""
    parsed_output = parse_ldd_verbose(command_output)
    assert parsed_output["versions"]["/bin/awk"][0] == {
        "dependency": "libm.so.6",
        "resolved_path": "/lib/x86_64-linux-gnu/libm.so.6",
        "version": "2.38",
    }
    assert parsed_output["libraries"][0] == {
        "address": "0x00007fff31cd9000",
        "path": None,
        "program": "linux-vdso.so.1",
    }
