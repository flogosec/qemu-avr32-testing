

TEST = """
    movh r0, 0x1020
    sub r0, -0x3040
    
    movh r1, 0x1
    sub r1, -0x1
    
    mulhh.w r2, r0:t, r1:t
    
"""

EXPECTED_RESULTS = {
    "r0": 0x10203040,
    "r1": 0x00010001,
    "r2": 0x00001020,
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
