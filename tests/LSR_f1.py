

TEST = """
    mov r0, 0xF234
    mov r1, 0x4
    lsr r2, r0, r1
    
    # z-flag
    lsr r3, r3, r1

"""

EXPECTED_RESULTS = {
    "r0": 0x0000f234,
    "r1": 0x4,
    "r2": 0x00000f23,
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
