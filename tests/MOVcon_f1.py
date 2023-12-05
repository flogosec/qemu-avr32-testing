

TEST = """
    mov r0, 0x1
    bld r0, 0x0
    
    mov r2, 0x1234
    
    moveq r4, r2
    movne r5, r2
    movhs r6, r2
    movlo r7, r2
    movge r8, r2
    movlt r9, r2
    movls r10, r2
    movle r11, r2
    movhi r12, r2
"""

EXPECTED_RESULTS = {
    "r0": 0x1,
    "r1": 0x0,
    "r2": 0x1234,
    "r3": 0,
    "r4": 0x1234,
    "r5": 0,
    "r6": 0,
    "r7": 0x1234,
    "r8": 0x1234,
    "r9": 0,
    "r10": 0x1234,
    "r11": 0x1234,
    "r12": 0,
    "sregC": 1,
    "sregZ": 1,
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
