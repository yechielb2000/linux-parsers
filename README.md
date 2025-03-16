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

```