from linux_parsers.parsers.process.proc_modules import parse_proc_modules


def test_proc_modules():
    command_output = """
nvidia_uvm 860160 0 - Live 0xffffffffc1e00000
nvidia_drm 57344 2 - Live 0xffffffffc0e00000
nvidia_modeset 1114112 1 nvidia_drm, Live 0xffffffffc1400000
nvidia 20643840 86 nvidia_uvm,nvidia_modeset, Live 0xffffffffc0000000
i915 2957312 3 - Live 0xffffffffc0200000
drm_kms_helper 253952 1 i915, Live 0xffffffffc0a00000
drm 634880 6 drm_kms_helper,nvidia_drm,i915, Live 0xffffffffc0800000
"""
    parsed_command = parse_proc_modules(command_output)
    assert parsed_command[0] == {
        "address": "0xffffffffc1e00000",
        "dependencies": [],
        "instances": 0,
        "name": "nvidia_uvm",
        "size": 860160,
        "state": "Live",
    }
    assert parsed_command[1] == {
        "address": "0xffffffffc0e00000",
        "dependencies": [],
        "instances": 2,
        "name": "nvidia_drm",
        "size": 57344,
        "state": "Live",
    }
    assert parsed_command[6] == {
        "address": "0xffffffffc0800000",
        "dependencies": ["drm_kms_helper", "nvidia_drm", "i915"],
        "instances": 6,
        "name": "drm",
        "size": 634880,
        "state": "Live",
    }
