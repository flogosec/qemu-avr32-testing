

TEST = """
    # no flags are set
    mov r1, 0xFFFF
    mov r2, 0xF
    
    sub r0, r1, r2 << 0
    
"""

EXPECTED_RESULTS = {
    "r0": 0xFFF0,
    "r1": 0xFFFF,
    "r2": 0xF,
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
