

TEST = """
    # no falgs set
    mov r1, 0x8
    mov r10, 0x3
    asr r0, r1, r10
    
"""

EXPECTED_RESULTS = {
    "r0": 0x0000001,
    "r1": 0x0000008,
    "r2": 0,
    "r3": 0,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0x3,
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
