

TEST = """
    #set v flag 2
    movh r0, 0x7FFF
   
    movh r1, 0x7FFF
   
    adc r2, r0, r1
"""

EXPECTED_RESULTS = {
    "r0": 0x7fff0000,
    "r1": 0x7fff0000,
    "r2": 0xfffe0000,
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
    "sregV": 1,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
