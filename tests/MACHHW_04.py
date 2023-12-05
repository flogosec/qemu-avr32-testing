

TEST = """
    mov r0, 0x2222
    movh r1, 0x2
    movh r2, 0x1111
    
    machh.w r2, r0:b, r1:t
"""

EXPECTED_RESULTS = {
    "r0": 0x2222,
    "r1": 0x00020000,
    "r2": 0x11114444,
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
    "sreg8": 0
}
