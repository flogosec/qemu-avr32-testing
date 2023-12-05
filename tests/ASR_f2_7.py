

TEST = """
    # no flags set
    movh r0, 0x7FFF
    ssrf 0x0 # set c-flag
    asr r0, 0x10 # c-flag should be cleared
    
"""

EXPECTED_RESULTS = {
    "r0": 0x7FFF,
    "r1": 0,
    "r2": 0,
    "r3": 0,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0,
    "r11": 0,
    "r12": 0,
    "sregC": 0,
    "sregZ": 0,
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0,
}
