

TEST = """
    # v-flag 1
    mov r0, 0x1
    bld r0, 0x0
    
    movh r0, 0x8000
    
    mov r1, 0x1234
    
    sbc r2, r0, r1
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0x80000000,
    "r1": 0x00001234,
    "r2": 0x7fffedcb,
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
    "sregV": 1,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
