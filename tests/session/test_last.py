from linux_parsers.parsers.session.last import parse_last


def test_last():
    command_output = """
alice    tty1         :0               Sun Mar 16 14:03   still logged in
bob      pts/0        192.168.1.100    Sun Mar 16 13:50   gone - no logout
charlie  pts/1        -                Sun Mar 16 13:45   still logged in
dave     pts/2        10.0.0.2         Sun Mar 16 12:30   gone - no logout
eve      tty2         :1               Sun Mar 16 10:00   still logged in
frank    pts/3        192.168.1.101    Sat Mar 15 18:25 - 19:30  (01:05)
george   ttyS0        -                Sat Mar 15 17:00 - 18:00  (01:00)
henry    pts/4        172.16.0.5       Sat Mar 15 16:00 - 16:45  (00:45)
irene    pts/5        fe80::1a2b:3c4d  Fri Mar 14 22:15 - 23:00  (00:45)
jack     tty1         :0               Fri Mar 14 21:00   still logged in
kate     pts/6        192.168.0.3      Thu Mar 13 20:15 - 21:00  (00:45)
leo      ttyS1        -                Thu Mar 13 19:00 - 19:30  (00:30)
mike     pts/7        192.168.1.102    Wed Mar 12 18:00 - 18:30  (00:30)
nancy    ttyS2        -                Wed Mar 12 17:00 - 17:45  (00:45)
"""
    parsed_output = parse_last(command_output)
    assert len(parsed_output) == 14
    assert parsed_output[0] == {
        "date": "Sun Mar 16 14:03",
        "end": None,
        "start": None,
        "status": "still logged in",
        "tty": "tty1",
        "event": "alice",
    }
    assert parsed_output[11] == {
        "date": "Thu Mar 13 19:00",
        "end": "00:30",
        "start": "19:30",
        "status": None,
        "tty": "ttyS1",
        "event": "leo",
    }
