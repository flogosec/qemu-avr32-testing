

TEST = """
    
    sbr r0, 0x3
    sbr r0, 0x1
    
    sbr r1, 0x5
    
    # set z-flag
    mov r5, 0x1
    bld r5, 0x0
    mov r5, 0x0
    
    sbr r1, 0xF
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0xa,
    "r1": 0x8020,
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
