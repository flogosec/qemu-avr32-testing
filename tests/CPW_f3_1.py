

TEST = """
    # v-flag 1
    movh r0, 0x8000
    cp.w r0, 0x05000
    
    mov r2, 0x5000
    sub r5, r0, r2
    
"""

EXPECTED_RESULTS = {
    "r0": 0x80000000,
    "r1": 0,
    "r2": 0x5000,
    "r3": 0,
    "r4": 0,
    "r5": 0x7fffb000,
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
