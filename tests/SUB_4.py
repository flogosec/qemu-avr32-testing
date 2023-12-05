

TEST = """
    # format 2
    mov r0, 0x10
    mov r1, 0x4
    sub r2, r0, r1<<1
    
    
    # format 4
    mov r3, 0x4
    sub r4, r3, 0x5
"""

EXPECTED_RESULTS = {
    "r0": 0x10,
    "r1": 0x4,
    "r2": 0x8,
    "r3": 0x4,
    "r4": 0xffffffff,
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
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
