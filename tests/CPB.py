

TEST = """
    mov r1, 0x0000000F
    cp.b r1, r2

    # n-flag
    mov r0, 0x000000FF
    cp.b r0, r10

    
"""

EXPECTED_RESULTS = {
    "r0": 0x000000FF,
    "r1": 0x0000000F,
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
    "sregN": 1,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
