

TEST = """
    # c-flag 1
    mov r0, 0x1
    movh r1, 0x4007
    sub r2, r0, r1 << 1
    
"""

EXPECTED_RESULTS = {
    "r0": 0x1,
    "r1": 0x40070000,
    "r2": 0x7ff20001,
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
