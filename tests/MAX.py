

TEST = """
    mov r0, 0x10
    mov r1, 0x2
    
    mov r2, -0x1
    
    max r9, r1, r0
    max r10, r0, r1 
    
    max r11, r1, r2
    max r12, r2, r1
"""

EXPECTED_RESULTS = {
    "r0": 0x10,
    "r1": 0x2,
    "r2": 0xffffffff,
    "r3": 0,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0x10,
    "r10": 0x10,
    "r11": 0x2,
    "r12": 0x2,
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
