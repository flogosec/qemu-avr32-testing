

TEST = """
    # c-flag 1
    
    mov r0, 0x1
    bld r0, 0x0
    
    movh r1, 0x8000
    sub r1, -0xFFFF
    
    sbc r2, r0, r1
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0x1,
    "r1": 0x8000ffff,
    "r2": 0x7fff0001,
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
