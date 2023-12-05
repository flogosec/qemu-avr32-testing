

TEST = """
    # Format 2
    mov r0, -0x12345 
    mov r1, 0x12345
    
    mov r2, r0
    mov r3, r1
"""

EXPECTED_RESULTS = {
    "r0": 0xfffedcbb,
    "r1": 0x12345,
    "r2": 0xfffedcbb,
    "r3": 0x12345,
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
