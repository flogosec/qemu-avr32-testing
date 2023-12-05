

TEST = """
    # NO flags
    movh r0, 0x7FFF
    sub r0, -0xFFFF
    mov r1, 0x10
    
    asr r2, r0, r1
    
"""

EXPECTED_RESULTS = {
    "r0": 0x7FFFFFFF,
    "r1": 0x10,
    "r2": 0x7FFF,
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
    "sregC": 1,
    "sregZ": 0,
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
