

TEST = """
    mov r0, 0x1020
    satu r0 >> 8, 0
    
    mov r2, 0x1020
    lsl r2, 0x10
    sub r2, -0x1020
    
    satu r2 >> 16, 8
    
    
    mov r4, 0x8040
    lsl r4, 0x10
    sub r4, -0x1020
    
    mtsr 0x0, r5
    
    satu r4 >> 0, 8
"""

EXPECTED_RESULTS = {
    "r0": 0x10,
    "r1": 0,
    "r2": 0x1ff,
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
    "sregQ": 1,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
