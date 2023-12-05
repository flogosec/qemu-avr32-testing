

TEST = """
    # r12 = -1, n-flag
    mov lr, 0x3333
    
    mov r1, 0x1
    bld r1, 0x0
    
    mov r2, 0x1234
    
    retlo lr

"""

EXPECTED_RESULTS = {
    "PC": 0x3333,
    "r0": 0,
    "r1": 0x1,
    "r2": 0x1234,
    "r3": 0,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0,
    "r11": 0,
    "r12": 0xffffffff,
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
