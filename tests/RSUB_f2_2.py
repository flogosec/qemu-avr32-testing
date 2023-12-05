

TEST = """
    # v-flag 2, n-flag, c-flag 1
    movh r0, 0x8000
    
    rsub r1, r0, 0x1
    
"""

EXPECTED_RESULTS = {
    "r0": 0x80000000,
    "r1": 0x80000001,
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
    "sregC": 1,
    "sregZ": 0,
    "sregN": 1,
    "sregV": 1,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
