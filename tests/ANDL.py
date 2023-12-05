

TEST = """
    #r0: 0x1
    movh r0, 0x1234
    sub r0, -0xFF01
    andl r0, 0x0010
    
    
    #r1: 0x0, z-flag
    mov r1, 0x0001
    andl r1, 0x0010
    
    # r2: 0x10001
    mov r2, 0x10001
    andl r2, 0x0001
"""

EXPECTED_RESULTS = {
    "r0": 0x12340000,
    "r1": 0,
    "r2": 0x10001,
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
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
