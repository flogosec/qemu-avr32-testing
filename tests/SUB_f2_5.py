

TEST = """
    # v-flag 1
    movh r0, 0x8000
    movh r1, 0x0FFF
    sub r1, -0xFFFF
    sub r2, r0, r1 << 0
    
"""

EXPECTED_RESULTS = {
    "r0": 0x80000000,
    "r1": 0x0fffffff,
    "r2": 0x70000001,
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
    "sregV": 1,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
