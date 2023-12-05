

TEST = """
    # z-flag, c-flag 2
    ssrf 0x1 # z
    ssrf 0x0 # c
    
    mov r0, -0x1
   
    adc r2, r0, r1
   
"""

EXPECTED_RESULTS = {
    "r0": 0xFFFFFFFF,
    "r1": 0,
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
