

TEST = """
    mov r0, 0x1234
    mov r1, 0x1234
    
    rcall 0x1000
    
"""

EXPECTED_RESULTS = {
    "PC": 0xd0001008,
    "LR": 0xd000000A,
    "r0": 0x1234,
    "r1": 0x1234,
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
