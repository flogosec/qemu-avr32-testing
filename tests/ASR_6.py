

TEST = """
    # n-flag
    mov r5, 0x8000
    lsl r5, 0x10
    sub r5, -0x1234
    mov r10, 0x5
    asr r0, r5, r10
    
"""

EXPECTED_RESULTS = {
    "r0": 0xfc000091,
    "r1": 0,
    "r2": 0,
    "r3": 0,
    "r4": 0,
    "r5": 0x80001234,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0x5,
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
