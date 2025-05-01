from linux_parsers.parsers.logs.var_log_cron import parse_var_log_cron


def test_var_log_cron():
    command_output = """
May  1 06:01:01 server-name CROND[12345]: (root) CMD (/usr/lib64/sa/sa1 1 1)
May  1 06:10:01 server-name CROND[12367]: (alice) CMD (/home/alice/scripts/backup.sh)
May  1 07:00:01 server-name CROND[12389]: (bob) CMD (run-parts /etc/cron.hourly)
"""
    parsed_output = parse_var_log_cron(command_output)
    assert parsed_output[0] == {
        "command": "/usr/lib64/sa/sa1 1 1",
        "day": "1",
        "host": "server-name",
        "month": "May",
        "pid": "12345",
        "time": "06:01:01",
        "user": "root",
    }
    assert parsed_output[1] == {
        "command": "/home/alice/scripts/backup.sh",
        "day": "1",
        "host": "server-name",
        "month": "May",
        "pid": "12367",
        "time": "06:10:01",
        "user": "alice",
    }
