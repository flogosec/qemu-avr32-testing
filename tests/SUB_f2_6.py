

TEST = """
    # v-flag 2, c-flag
    movh r0, 0x7FFF
    sub r0, -0xFFFF
    mov r1, -0x1000
    sub r2, r0, r1 << 0
    
"""

EXPECTED_RESULTS = {
    "r0": 0x7fffffff,
    "r1": 0xfffff000,
    "r2": 0x80000fff,
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
