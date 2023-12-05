

TEST = """
    mov r0, 0x0000FFFF
    cbr r0, 0x0
    cbr r0, 0x4
    mov r1, 0x0000FFFF
    cbr r1, 0x8
    mov r2, 0x0000FFFF
    cbr r2, 0xE
    
    # z-flag
    mov r3, 0x50
    cbr r3, 0x4
    cbr r3, 0x6
"""

EXPECTED_RESULTS = {
    "r0": 0x0000FFEE,
    "r1": 0x0000FEFF,
    "r2": 0x0000BFFF,
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
