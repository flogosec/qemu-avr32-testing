

TEST = """
    # c-flag
    mov r0, 0xBF34
    lsl r1, r0, 0x11
    

"""

EXPECTED_RESULTS = {
    "r0": 0xBF34,
    "r1": 0x7E680000,
    "r2": 0,
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
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
