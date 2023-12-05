

TEST = """
    movh r4, 0x1111
    sub r4, -0x1111
    
    movh r0, 0x2222
    sub r0, -0x2222
    mov r1, 0x2
    
    macs.d r4, r0, r1
    csrf 0
"""

EXPECTED_RESULTS = {
    "r0": 0x22222222,
    "r1": 0x2,
    "r2": 0,
    "r3": 0,
    "r4": 0x55555555,
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
