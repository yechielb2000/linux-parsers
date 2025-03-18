from linux_parsers.parsers.system.hwinfo import parse_hwinfo


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
