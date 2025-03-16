# Linux Parsers

## 🤵‍♂️ 🐧 🤵‍♀️ 🐧 🤵 🐧

    ^________________________________________________________
    |                                                        |
    | Simplest library for parsing linux commands and files  |
    \________________________________________________________/

## How to use

Let's say you want to parse `ps aux` command to get the processes in a better form.

```python
import subprocess
from linux_parsers.parsers.process.ps import parse_ps_aux

# Run the ps aux command
completed_process_result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# Get the command result
ps_aux_command_output = completed_process_result.stdout
# parse the command
parsed_command_output = parse_ps_aux(ps_aux_command_output)
# Print the parsed command result
print(parsed_command_output)
```

## Hierarchy

#### Filesystem parsers

- [df.py](linux_parsers/parsers/filesystem/df.py) - parse commands: `df`.
- [dpkg.py](linux_parsers/parsers/filesystem/dpkg.py) - parse commands: `dpkg -l`.
- [du.py](linux_parsers/parsers/filesystem/du.py) - parse commands: `du -ab <path>`.
- [fdisk.py](linux_parsers/parsers/filesystem/fdisk.py) - parse commands: `fdisk -l`.
- [ls.py](linux_parsers/parsers/filesystem/ls.py) - parse commands: `ls -la`.
- [mount.py](linux_parsers/parsers/filesystem/mount.py) - parse file `/proc/mounts` or command `mount`.
- [stat.py](linux_parsers/parsers/filesystem/stat.py) - parse commands: `stat`.

#### Network parsers

- [arp.py](linux_parsers/parsers/network/arp.py) - parse commands: `arp -i <interface>`, `arp -en`, `arp -e`.
- [etc_resolve_conf.py](linux_parsers/parsers/network/etc_resolve_conf.py) - parse file: `/etc/resolve.conf`.
- [ip.py](linux_parsers/parsers/network/ip.py) - parse commands: `ip a`, `ip r`, `ip n`.
- [iptables.py](linux_parsers/parsers/network/iptables.py) - parse commands: `iptables -L -n -v`.
- [netstat.py](linux_parsers/parsers/network/netstat.py) - parse commands: `netstat -tulpan`.
- [ping.py](linux_parsers/parsers/network/ping.py) - parse commands: `ping <address>`.
- [ss.py](linux_parsers/parsers/network/ss.py) - parse commands: `ss -tulnap`, `ss -s`.
- [ufw.py](linux_parsers/parsers/network/ufw.py) - parse commands: `ufw app list`, `ufw status`.

#### Process parsers

- [cgroups.py](linux_parsers/parsers/process/cgroups.py) - parse files: `/proc/cgroups`, `/proc/<pid>/cgroups`.
- [jobs.py](linux_parsers/parsers/process/jobs.py) - parse commands: `jobs`.
- [ps.py](linux_parsers/parsers/process/ps.py) - parse commands: `ps aux`, `ps -ax`,`ps -caweL`, `ps -fadel`.
- [top.py](linux_parsers/parsers/process/top.py) - parse commands: `top`.

#### Session parsers

- [last.py](linux_parsers/parsers/session/last.py) - parse commands: `last`.
- [w.py](linux_parsers/parsers/session/w.py) - parse commands: `w`.
- [who.py](linux_parsers/parsers/session/who.py) - parse commands: `who -a`.

#### System parsers

- [etc_os_release.py](linux_parsers/parsers/system/etc_os_release.py) - parse file: `/etc/os-release`.
- [free.py](linux_parsers/parsers/system/free.py) - parse commands: `free -btlv`.
- [hwinfo.py](linux_parsers/parsers/system/hwinfo.py) - parse commands: `hwinfo --<action>`.
- [iostat.py](linux_parsers/parsers/system/iostat.py) - parse commands: `iostat -x`.
- [mpstat.py](linux_parsers/parsers/system/mpstat.py) - parse commands: `mpstat -P ALL`.
- [proc_cpuinfo.py](linux_parsers/parsers/system/proc_cpuinfo.py) - parse file: `/proc/cpuinfo`.
- [proc_meminfo.py](linux_parsers/parsers/system/proc_meminfo.py) - parse file: `/proc/meminfo`.
- [service.py](linux_parsers/parsers/system/service.py) - parse commands: `service --status-all`.
- [uname.py](linux_parsers/parsers/system/uname.py) - parse commands: `uname -a`.
- [vmstat.py](linux_parsers/parsers/system/vmstat.py) - parse commands: `vmstat`, `vmstat -adt`.

#### Users parsers

- [chage.py](linux_parsers/parsers/users/chage.py) - parse commands: `chage -l <username>`.
- [etc_group.py](linux_parsers/parsers/users/etc_group.py) - parse file: `/etc/group`.
- [etc_gshadow.py](linux_parsers/parsers/users/etc_gshadow.py) - parse file: `/etc/gshadow`.
- [etc_passwd.py](linux_parsers/parsers/users/etc_passwd.py) - parse file: `/etc/passwd`.
- [etc_shadow.py](linux_parsers/parsers/users/etc_shadow.py) - parse file: `/etc/shadow`.
- [useradd.py](linux_parsers/parsers/users/useradd.py) - parse commands: `useradd -D`.

## Contribute

If you'd like to add parsers, feel free to ask me, or you can fork the project and submit a pull request.  
