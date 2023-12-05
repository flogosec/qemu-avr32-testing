

TEST = """
    # n-flag, c-flag 1    
    mov r1, 0xFFFF
    lsl r1, 0x10
    
    mov r5, 0x1
    bld r5, 0x0
    
    cpc r0, r1
    
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0,
    "r1": 0xffff0000,
    "r2": 0,
    "r3": 0,
    "r4": 0,
    "r5": 1,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0,
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
