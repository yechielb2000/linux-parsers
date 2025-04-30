from linux_parsers.parsers.system.proc_version import parse_proc_version


def test_proc_version():
    command_output = "Linux version 5.15.167.4-microsoft-standard-WSL2 (root@f9c826d3017f) (gcc (GCC) 11.2.0, GNU ld (GNU Binutils) 2.37) #1 SMP Tue Nov 5 00:21:55 UTC 2024"
    parsed_command = parse_proc_version(command_output)
    assert parsed_command == {
        "build_date": "Tue Nov 5 00:21:55 UTC 2024",
        "build_info": "#1",
        "build_type": "SMP",
        "builder": "root@f9c826d3017f",
        "compiler": "gcc (GCC) 11.2.0",
        "kernel_version": "5.15.167.4-microsoft-standard-WSL2",
        "linker": "GNU ld (GNU Binutils) 2.37",
    }
