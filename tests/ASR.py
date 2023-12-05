

TEST = """
    # c-flag
    mov r0, 0x00000003
    mov r10, 0x1
    asr r2, r0, r10    
"""

EXPECTED_RESULTS = {
    "r0": 0x0000003,
    "r1": 0,
    "r2": 0x1,
    "r3": 0,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0x1,
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
