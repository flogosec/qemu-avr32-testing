

TEST = """
    mov r3, 0xB16B
    bfexts r4, r3, 0x3, 0x5
"""

EXPECTED_RESULTS = {
    "r0": 0,
    "r1": 0,
    "r2": 0,
    "r3": 0xB16B,
    "r4": 0x0000000d,
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
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
