from linux_parsers.parsers.logs.var_log_maillog import parse_var_log_maillog


def test_var_log_maillog():
    command_output = """
Apr 30 10:15:01 mailserver postfix/smtpd[10234]: connect from unknown[203.0.113.45]
Apr 30 10:15:01 mailserver postfix/smtpd[10234]: 3F2A5C3D4E: client=unknown[203.0.113.45]
Apr 30 10:15:02 mailserver postfix/cleanup[10237]: 3F2A5C3D4E: message-id=<1234@example.com>
Apr 30 10:15:02 mailserver postfix/qmgr[2938]: 3F2A5C3D4E: from=<sender@example.com>, size=1234, nrcpt=1 (queue active)
Apr 30 10:15:03 mailserver postfix/smtp[10239]: 3F2A5C3D4E: to=<recipient@example.net>, relay=mail.example.net[198.51.100.23]:25, delay=1.5, delays=0.3/0.1/0.5/0.6, dsn=2.0.0, status=sent (250 2.0.0 Ok: queued as ABC123456)
Apr 30 10:15:03 mailserver postfix/qmgr[2938]: 3F2A5C3D4E: removed
Apr 30 10:15:04 mailserver dovecot: imap-login: Login: user=<recipient@example.net>, method=PLAIN, rip=192.0.2.55, lip=203.0.113.2, mpid=10241, TLS, session=<oABCD1234>
"""
    parsed_output = parse_var_log_maillog(command_output)
    assert parsed_output[0] == {
        "day": "30",
        "hostname": "mailserver",
        "message": "connect from unknown[203.0.113.45]",
        "month": "Apr",
        "pid": "10234",
        "process": "postfix/smtpd",
        "time": "10:15:01",
    }
    assert parsed_output[1] == {
        "day": "30",
        "hostname": "mailserver",
        "message": "3F2A5C3D4E: client=unknown[203.0.113.45]",
        "month": "Apr",
        "pid": "10234",
        "process": "postfix/smtpd",
        "time": "10:15:01",
    }
