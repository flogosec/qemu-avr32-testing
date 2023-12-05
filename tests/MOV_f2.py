

TEST = """
    # Format 2
    mov r0, -0x12345 
    mov r1, 0x12345
    mov r2, -0xFFFEF
    mov r3, 0xFFFFF
    mov r4, -0x100000
"""

EXPECTED_RESULTS = {
    "r0": 0xfffedcbb,
    "r1": 0x12345,
    "r2": 0xfff00011,
    "r3": 0x000fffff,
    "r4": 0xfff00000,
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
