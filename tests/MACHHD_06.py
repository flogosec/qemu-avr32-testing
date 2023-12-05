

TEST = """
    # Adding a null multiplication
    mov r0, 0x0002
    mov r1, 0x0002    
    
    movh r4, 0x1111
    sub r4, -0x1111
    movh r5, 0x1111
    sub r5, -0x1111
    machh.d r4, r0:t, r1:b
    csrf 0
"""

EXPECTED_RESULTS = {
    "r0": 0x00000002,
    "r1": 0x00000002,
    "r2": 0,
    "r3": 0,
    "r4": 0x11110000,
    "r5": 0x11111111,
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
