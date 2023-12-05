

TEST = """
    # n-flag
    movh r4, 0x8000
    movh r5, 0x8020    
    and r6, r4, r5  >> 0
    
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0,
    "r1": 0,
    "r2": 0,
    "r3": 0,
    "r4": 0x80000000,
    "r5": 0x80200000,
    "r6": 0x80000000,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0,
    "r11": 0,
    "r12": 0,
    "sregC": 0,
    "sregZ": 0,
    "sregN": 1,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
