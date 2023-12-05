

TEST = """
    mov r0, 0x1234
    movh r1, 0x1234
    ssrf 0
    orcs r5, r0, r1
    
"""

EXPECTED_RESULTS = {
    "r0": 0x00001234,
    "r1": 0x12340000,
    "r2": 0,
    "r3": 0,
    "r4": 0,
    "r5": 0x12341234,
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
