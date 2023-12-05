

TEST = """
    mov r0, 0x2
    mov r1, 0x5
    mov r2, 0x4
    
    mac r2, r0, r1
    
    
    mov r4, 0x1234
    lsl r4, -0x10
    
    mov r5, 0x100
    mov r6, 0x1000
    mac r6, r4, r5
"""

EXPECTED_RESULTS = {
    "r0": 0x2,
    "r1": 0x5,
    "r2": 0xE,
    "r3": 0,
    "r4": 0x12340000,
    "r5": 0x100,
    "r6": 0x34001000,
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
