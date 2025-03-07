from linux_parsers.parsers.process.ps import parse_ps_aux, parse_ps_ax, parse_ps_caweL


def test_ps_aux():
    command_output = """
root         1  0.0  0.0   2616  1748 hvc0     Sl+  14:00   0:00 /init
root         5  0.0  0.0   2616     4 hvc0     Sl+  14:00   0:00 plan9 --control-socket 5 --log-level 4 --server-fd 6 --pipe-fd 8 --log-truncate
root         8  0.0  0.0   2624   120 ?        Ss   14:00   0:00 /init
root         9  0.0  0.0   2624   128 ?        S    14:00   0:00 /init
a           10  0.3  0.0  32700  5732 pts/0    Ssl+ 14:00   0:14 /tmp/tmp.ozjZDppcnK/ijent grpc-stdio-server --log-level info --self-delete-on-exit
root      5950  0.0  0.0   2624   120 ?        Ss   14:45   0:00 /init
root      5951  0.0  0.0   2624   128 ?        S    14:45   0:00 /init
a         5952  0.0  0.0   7544  4280 pts/1    Ss   14:45   0:00 -bash
a        10119  0.0  0.0   8164  3664 pts/1    R+   15:16   0:00 ps aux   
    """
    parsed_command = parse_ps_aux(command_output)
    assert len(parsed_command) == 9
    assert parsed_command[0]['rss'] == '1748'
    assert parsed_command[0]['time'] == '0:00'
    assert parsed_command[0]['start'] == '14:00'
    assert parsed_command[2]['mem'] == '0.0'
    assert parsed_command[2]['cpu'] == '0.0'
    assert parsed_command[7]['command'] == '-bash'
    assert parsed_command[7]['stat'] == 'Ss'


def test_ps_ax():
    command_output = """
  PID TTY      STAT   TIME COMMAND
   10 pts/0    Ssl+   0:08 /tmp/tmp.ozjZDppcnK/ijent grpc-stdio-server --log-level info --self-delete-on-exit
 5952 pts/1    Ss     0:00 -bash
 6715 pts/1    R+     0:00 ps -x
    """
    parsed_command = parse_ps_ax(command_output)
    assert len(parsed_command) == 3
    assert parsed_command[0]['pid'] == '10'
    assert parsed_command[1]['stat'] == 'Ss'
    assert parsed_command[1]['time'] == '0:00'
    assert parsed_command[2]['tty'] == 'pts/1'
    assert parsed_command[2]['command'] == 'ps -x'


def test_ps_caweL():
    command_output = """
  PID   LWP CLS PRI TTY          TIME CMD
    1     1 TS   19 hvc0     00:00:00 init(kali-linux
    1     7 TS   19 hvc0     00:00:00 Interop
    5     5 TS   19 hvc0     00:00:00 init
    5     6 TS   19 hvc0     00:00:00 init
    8     8 TS   19 ?        00:00:00 SessionLeader
    9     9 TS   19 ?        00:00:00 Relay(10)
   10    10 TS   19 pts/0    00:00:00 ijent
   10    22 TS   19 pts/0    00:00:00 tokio-runtime-w
   10    23 TS   19 pts/0    00:00:02 tokio-runtime-w
   10    24 TS   19 pts/0    00:00:00 tokio-runtime-w
   10    25 TS   19 pts/0    00:00:00 tokio-runtime-w
   10    26 TS   19 pts/0    00:00:00 tokio-runtime-w
   10    27 TS   19 pts/0    00:00:02 tokio-runtime-w
   10    28 TS   19 pts/0    00:00:01 tokio-runtime-w
   10    29 TS   19 pts/0    00:00:00 tokio-runtime-w
   10    31 TS   19 pts/0    00:00:04 tokio-runtime-w
   10    52 TS   19 pts/0    00:00:00 tokio-runtime-w
   10  8863 TS   19 pts/0    00:00:00 tokio-runtime-w
 5950  5950 TS   19 ?        00:00:00 SessionLeader
 5951  5951 TS   19 ?        00:00:00 Relay(5952)
 5952  5952 TS   19 pts/1    00:00:00 bash
 8884  8884 TS   19 pts/1    00:00:00 ps
    """
    parsed_command = parse_ps_caweL(command_output)
    assert len(parsed_command) == 22
    assert parsed_command[0]['cls'] == 'TS'
    assert parsed_command[0]['cmd'] == 'init(kali-linux'
    assert parsed_command[2]['cmd'] == 'init'
    assert parsed_command[2]['tty'] == 'hvc0'
    assert parsed_command[9]['time'] == '00:00:00'
    assert parsed_command[9]['tty'] == 'pts/0'
