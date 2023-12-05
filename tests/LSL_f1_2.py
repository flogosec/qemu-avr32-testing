

TEST = """
    # n-flag
    mov r0, 0xFF34
    lsl r0, 0x8
    mov r1, 0x08
    lsl r2, r0, r1

"""

EXPECTED_RESULTS = {
    "r0": 0x00ff3400,
    "r1": 0x00000008,
    "r2": 0xff340000,
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
    "sregZ": 0,
    "sregN": 1,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
