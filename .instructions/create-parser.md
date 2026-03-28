When asked for a new command parser, you should:
- check if the parser exists, if it is, then say it and do not create the parser
- if there is a file for the command (the new requested parser is with different command flags), write it in this file.
- if there is no file, the file should be created under the right group (logs, process, system etc...).
- the file should have the command name.
- the parser should only get `command_output: str`.
- the parser return type should be one of `str`/`list`/`dict`.
- the parser should be aligned with the best practices of python programming.
- the parser name should be `parse_<command>_<flags-used>`.
- the parser should have docs describing the flags it parses.
- the parser should have a unitest in the `tests` directory under the same group with the name `test_<command>`.
- the parser unitest should have a sample of the command output and then run the command and expect the right output.
- after creating the parser, please run it and see if everything is ok, if not, fix and run again. do it until it works.
- after making the parser, add the new parser to the CHANGELOG.md file.
- after that commit the new changes.


Here is an example: 
```python
def parse_hwinfo(command_output: str) -> List[Dict]:
    """Parse `hwinfo --<action>` command outputs.
    CPU	                 hwinfo --cpu
    Memory (RAM)	     hwinfo --memory
    Disks (HDD/SSD)	     hwinfo --disk
    Network Interfaces	 hwinfo --network
    USB Devices	         hwinfo --usb
    GPU (Graphics)	     hwinfo --gfxcard
    Bluetooth	         hwinfo --bluetooth
    """
    blocks = re.split(r"^\d+:", command_output, flags=re.MULTILINE)
    parsed_command = []
    for block in list(filter(str.strip, blocks)):
        fields = [i.strip() for i in block.splitlines() if i.strip()][2:]
        block_fields = {}
        for field in fields:
            key, value = field.split(":")
            block_fields[key.strip()] = value.strip()
        parsed_command.append(block_fields)
    return parsed_command
```
unitest example:
```python
def test_hwinfo():
    command_output = """
01: None 00.0: 10103 CPU
  [Created at cpu.465]
  Unique ID: rdCR.j8NaKXDZtZ6
  Hardware Class: cpu
  Arch: X86-64
  Vendor: "GenuineIntel"
  Model: 6.142.10 "Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz"
  Features: fpu,vme,de,pse,tsc,msr,pae,mce,cx8,apic,sep,mtrr,pge,mca,cmov,pat,pse36,clflush,mmx,fxsr,sse,sse2,ss,ht,syscall,nx,pdpe1gb,rdtscp,lm,constant_tsc,arch_perfmon,rep_good,nopl,xtopology,cpuid,pni,pclmulqdq,vmx,ssse3,fma,cx16,pdcm,pcid,sse4_1,sse4_2,movbe,popcnt,aes,xsave,avx,f16c,rdrand,hypervisor,lahf_lm,abm,3dnowprefetch,invpcid_single,pti,ssbd,ibrs,ibpb,stibp,tpr_shadow,vnmi,ept,vpid,ept_ad,fsgsbase,bmi1,avx2,smep,bmi2,erms,invpcid,rdseed,adx,smap,clflushopt,xsaveopt,xsavec,xgetbv1,xsaves,md_clear,flush_l1d,arch_capabilities
  Clock: 1992 MHz
  BogoMips: 3984.00
  Cache: 8192 kb
  Units/Processor: 8
  Config Status: cfg=new, avail=yes, need=no, active=unknown

02: None 01.0: 10103 CPU
  [Created at cpu.465]
  Unique ID: wkFv.j8NaKXDZtZ6
  Hardware Class: cpu
  Arch: X86-64
  Vendor: "GenuineIntel"
  Model: 6.142.10 "Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz"
  Features: fpu,vme,de,pse,tsc,msr,pae,mce,cx8,apic,sep,mtrr,pge,mca,cmov,pat,pse36,clflush,mmx,fxsr,sse,sse2,ss,ht,syscall,nx,pdpe1gb,rdtscp,lm,constant_tsc,arch_perfmon,rep_good,nopl,xtopology,cpuid,pni,pclmulqdq,vmx,ssse3,fma,cx16,pdcm,pcid,sse4_1,sse4_2,movbe,popcnt,aes,xsave,avx,f16c,rdrand,hypervisor,lahf_lm,abm,3dnowprefetch,invpcid_single,pti,ssbd,ibrs,ibpb,stibp,tpr_shadow,vnmi,ept,vpid,ept_ad,fsgsbase,bmi1,avx2,smep,bmi2,erms,invpcid,rdseed,adx,smap,clflushopt,xsaveopt,xsavec,xgetbv1,xsaves,md_clear,flush_l1d,arch_capabilities
  Clock: 1992 MHz
  BogoMips: 3984.00
  Cache: 8192 kb
  Units/Processor: 8
  Config Status: cfg=new, avail=yes, need=no, active=unknown

03: None 02.0: 10103 CPU
  [Created at cpu.465]
  Unique ID: +rIN.j8NaKXDZtZ6
  Hardware Class: cpu
  Arch: X86-64
  Vendor: "GenuineIntel"
  Model: 6.142.10 "Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz"
  Features: fpu,vme,de,pse,tsc,msr,pae,mce,cx8,apic,sep,mtrr,pge,mca,cmov,pat,pse36,clflush,mmx,fxsr,sse,sse2,ss,ht,syscall,nx,pdpe1gb,rdtscp,lm,constant_tsc,arch_perfmon,rep_good,nopl,xtopology,cpuid,pni,pclmulqdq,vmx,ssse3,fma,cx16,pdcm,pcid,sse4_1,sse4_2,movbe,popcnt,aes,xsave,avx,f16c,rdrand,hypervisor,lahf_lm,abm,3dnowprefetch,invpcid_single,pti,ssbd,ibrs,ibpb,stibp,tpr_shadow,vnmi,ept,vpid,ept_ad,fsgsbase,bmi1,avx2,smep,bmi2,erms,invpcid,rdseed,adx,smap,clflushopt,xsaveopt,xsavec,xgetbv1,xsaves,md_clear,flush_l1d,arch_capabilities
  Clock: 1992 MHz
  BogoMips: 3984.00
  Cache: 8192 kb
  Units/Processor: 8
  Config Status: cfg=new, avail=yes, need=no, active=unknown
    
"""
    parsed_command = parse_hwinfo(command_output)
    assert len(parsed_command) == 3
    assert parsed_command[0]["Arch"] == "X86-64"
    assert parsed_command[0]["Clock"] == "1992 MHz"
    assert parsed_command[1]["Config Status"] == "cfg=new, avail=yes, need=no, active=unknown"
    assert (
        parsed_command[1]["Features"]
        == "fpu,vme,de,pse,tsc,msr,pae,mce,cx8,apic,sep,mtrr,pge,mca,cmov,pat,pse36,clflush,mmx,fxsr,sse,sse2,ss,ht,syscall,nx,pdpe1gb,rdtscp,lm,constant_tsc,arch_perfmon,rep_good,nopl,xtopology,cpuid,pni,pclmulqdq,vmx,ssse3,fma,cx16,pdcm,pcid,sse4_1,sse4_2,movbe,popcnt,aes,xsave,avx,f16c,rdrand,hypervisor,lahf_lm,abm,3dnowprefetch,invpcid_single,pti,ssbd,ibrs,ibpb,stibp,tpr_shadow,vnmi,ept,vpid,ept_ad,fsgsbase,bmi1,avx2,smep,bmi2,erms,invpcid,rdseed,adx,smap,clflushopt,xsaveopt,xsavec,xgetbv1,xsaves,md_clear,flush_l1d,arch_capabilities"
    )
```
