

TEST = """
    mov r0, 0x1
    bld r0, 0x0
    
    moveq r4, -0x1
    movne r5, 0x12
    movhs r6, 0x12
    movlo r7, -0x7F
    movge r8, 0x12
    movlt r9, 0x12
    movls r10, 0xA
    movle r11, 0xB
    movhi r12, 0xC
"""

EXPECTED_RESULTS = {
    "r0": 0x1,
    "r1": 0,
    "r2": 0,
    "r3": 0,
    "r4": 0xFFFFFFFF,
    "r5": 0,
    "r6": 0,
    "r7": 0xffffff81,
    "r8": 0x12,
    "r9": 0,
    "r10": 0xA,
    "r11": 0xB,
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
