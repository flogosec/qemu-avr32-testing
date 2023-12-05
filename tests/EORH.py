

TEST = """
    mov r0, 0xF234
    lsl r0, r0, 0x10
    mov r1, 0x5678
    add r0, r0, r1
    
    # n-flag
    eorh r0, 0x0230
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0xF0045678,
    "r1": 0x5678,
    "r2": 0,
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
    "sregN": 1,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
