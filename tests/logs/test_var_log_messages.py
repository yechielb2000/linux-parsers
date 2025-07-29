from linux_parsers.parsers.logs.var_log_messages import parse_var_log_messages


def test_parse_var_log_messages():
    command_output = """
Jul 29 18:31:45 myhost kernel: [12345.678901] usb 1-2: new high-speed USB device number 2 using xhci_hcd
Jul 29 18:31:47 myhost sshd[1234]: Accepted password for root from 192.168.0.10 port 54321 ssh2
Jul 29 18:32:00 myhost CRON[4321]: (root) CMD (run-parts /etc/cron.hourly)
Jul 29 18:32:05 myhost systemd: Starting Daily Cleanup of Temporary Directories...
"""
    parsed_output = parse_var_log_messages(command_output)
    assert parsed_output[0] == {
        "host": "myhost",
        "message": "[12345.678901] usb 1-2: new high-speed USB device number 2 using xhci_hcd",
        "pid": None,
        "process": "kernel",
        "timestamp": "Jul 29 18:31:45",
    }
