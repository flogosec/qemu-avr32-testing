

TEST = """
    # c-flag 2, n-flag, v-flag 2
    mov r0, 0x47FFF
    mov r1, 0x48FFE
    cp.h r0, r1
    
"""

EXPECTED_RESULTS = {
    "r0": 0x47FFF,
    "r1": 0x48FFE,
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
    "sregZ": 0,
    "sregN": 1,
    "sregV": 1,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
