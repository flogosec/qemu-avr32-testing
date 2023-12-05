

TEST = """        
    # c-flag
    mov r2, 0xC
    mov r10, 0x2
    asr r0, r2, r10    
"""

EXPECTED_RESULTS = {
    "r0": 0x0000003,
    "r1": 0,
    "r2": 0xC,
    "r3": 0,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0x2,
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
