

TEST = """
    movh r0, 0x8F00
    sub r0, -0x1234
    mtsr 0x0, r5    # clear c-flag
    
    mov r1, 0x20
    
    mulu.d r2, r0, r1
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0x8f001234,
    "r1": 0x00000020,
    "r2": 0xe0024680,
    "r3": 0x00000011,
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
