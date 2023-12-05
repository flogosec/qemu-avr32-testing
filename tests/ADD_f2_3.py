

TEST = """
   
    # v-flag 1, c-flag 1
    movh r3, 0x8000
    mov r4, 0x8000
    lsl r4, 0xE
    add r8, r3, r4 << 2    
    
"""

EXPECTED_RESULTS = {
    "r0": 0,
    "r1": 0,
    "r2": 0,
    "r3": 0x80000000,
    "r4": 0x20000000,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0,
    "r11": 0,
    "r12": 0,
    "sregC": 1,
    "sregZ": 1,
    "sregN": 0,
    "sregV": 1,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
