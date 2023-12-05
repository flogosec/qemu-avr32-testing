

TEST = """
    
    mov r0, 0x1
    com r0
    
    mov r1, 0x2
    com r1
    
    mov r3, -0x2
    com r3
    
    # z-flag
    mov r4, -0x1
    com r4
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0xfffffffe,
    "r1": 0xfffffffd,
    "r2": 0,
    "r3": 0x1,
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
    "sregZ": 1,
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
