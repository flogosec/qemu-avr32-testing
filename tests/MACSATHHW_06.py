

TEST = """
    # Overflow => Q set
    mov r0, 0x1
    mov r1, 0x1
    
    movh r4, 0x7fff
    sub r4, -0xffff
    csrf 0
    macsathh.w r4, r0:b, r1:b
"""

EXPECTED_RESULTS = {
    "r0": 0x00000001,
    "r1": 0x00000001,
    "r2": 0,
    "r3": 0,
    "r4": 0x7fffffff,
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
    "sregQ": 1,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
