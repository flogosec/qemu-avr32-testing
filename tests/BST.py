

TEST = """
    mov r0, 0x1
    sub r0, 0x2
    
    bst r2, 0x4
    bst r3, 0x0
    bst r4, 0x1
    
    bst r5, 0x10
    bst r6, 0x18
    bst r7, 0x1F
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0xffffffff,
    "r1": 0,
    "r2": 0x10,
    "r3": 0x1,
    "r4": 0x2,
    "r5": 0x00010000,
    "r6": 0x01000000,
    "r7": 0x80000000,
    "r8": 0,
    "r9": 0,
    "r10": 0,
    "r11": 0,
    "r12": 0,
    "sregC": 1,
    "sregZ": 0,
    "sregN": 1,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
