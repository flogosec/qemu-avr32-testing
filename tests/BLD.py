

TEST = """
    

    # set and reset c and z flag 
    sub r1, 0x1 # sets n-flag
    bld r0, 0x4
    
    # set c and z flag
    mov r0, 0x00000010
    bld r0, 0x4
"""

EXPECTED_RESULTS = {
    "r0": 0x00000010,
    "r1": 0xffffffff,
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
    "sregN": 1,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
