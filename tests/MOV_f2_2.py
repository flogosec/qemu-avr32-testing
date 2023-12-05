

TEST = """
    # Format 2
    mov r0, -0x1
    mov r1, -0x2
    mov r2, 0x1
    
    mov r3, 0xFFFFF
    
    mov r4, 0xE0000
    mov r5, 0xF0000
"""

EXPECTED_RESULTS = {
    "r0": 0xffffffff,
    "r1": 0xfffffffe,
    "r2": 0x1,
    "r3": 0xFFFFF,
    "r4": 0xE0000,
    "r5": 0x000f0000,
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