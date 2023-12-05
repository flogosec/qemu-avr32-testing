

TEST = """
    # v-flag 2, c-flag 1-3
    mov r0, 0x1
    bld r0, 0x0
    
    movh r1, 0x8000
    
    mov r0, 0x1234
    
    sbc r2, r0, r1
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0x00001234,
    "r1": 0x80000000,
    "r2": 0x80001233,
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
    "sregN": 1,
    "sregV": 1,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
