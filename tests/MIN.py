

TEST = """
    mov r0, 0x10
    mov r1, 0x2
    
    mov r2, -0x10
    
    min r9, r1, r0 
    min r10, r0, r1 
    
    min r11, r1, r2
    min r12, r2, r1
    
"""

EXPECTED_RESULTS = {
    "r0": 0x10,
    "r1": 0x2,
    "r2": 0xfffffff0,
    "r3": 0,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0x2,
    "r10": 0x2,
    "r11": 0xfffffff0,
    "r12": 0xfffffff0,
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
