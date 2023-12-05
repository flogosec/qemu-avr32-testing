

TEST = """
    mov r1, 0x10001
    andh r1, 0x0001
    
    mov r2, 0x10001
    andh r2, 0x0001, coh
    
    # n-flag
    mov r4, 0x8005
    lsl r4, 0x10
    sub r4, -0xFFFF
    andh r4, 0x8005
    
    # n-flag
    mov r5, 0x8005
    lsl r5, 0x10
    sub r5, -0xFFFF
    andh r5, 0x8005, coh
    
"""

EXPECTED_RESULTS = {
    "r0": 0,
    "r1": 0x00010001,
    "r2": 0x00010000,
    "r3": 0,
    "r4": 0x8005ffff,
    "r5": 0x80050000,
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
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
