

TEST = """
    # r12 = 0, z-flag
    mov lr, 0x3333
    
    mov r1, 0x1
    
    mov r2, 0x1234
    
    rethi sp

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
    "r12": 0,
    "sregC": 0,
    "sregZ": 1,
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
