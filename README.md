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
```markdown
filesystem/
    ├── df.py
    ├── dpkg.py
    ├── du.py
    ├── fdisk.py
    ├── ls.py
    ├── mount.py
    ├── stat.py
monitors/
    ├── __init__.py
network/
    ├── arp.py
    ├── ip.py
    ├── iptables.py
    ├── netstat.py
    ├── ping.py
    ├── ss.py
    ├── ufw.py
process/
    ├── cgroups.py
    ├── jobs.py
    ├── ps.py
    ├── top.py
session/
    ├── last.py
    ├── w.py
    ├── who.py
system/
    ├── free.py
    ├── hwinfo.py
    ├── iostat.py
    ├── mpstat.py
    ├── service.py
    ├── uname.py
    ├── vmstat.py
users/
    ├── __init__.py
    ├── chage.py
    ├── passwd.py
    ├── shadow.py
    ├── useradd.py
virtualization/
    ├── __init__.py
```