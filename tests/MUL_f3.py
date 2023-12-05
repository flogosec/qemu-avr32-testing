

TEST = """
    mov r0, 0x2
    
    mul r2, r0, 0x5
    mul r3, r0, 0x1
    
    mul r4, r0, 0x1F
    mul r5, r0, -0x1
    
"""

EXPECTED_RESULTS = {
    "r0": 0x2,
    "r1": 0,
    "r2": 0xa,
    "r3": 0x00000002,
    "r4": 0x0000003e,
    "r5": 0xfffffffe,
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