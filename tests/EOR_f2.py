

TEST = """
    
    mov r0, 0xAA
    mov r1, 0xFA
    eor r2, r0, r1 << 0
    
    
    mov r4, 0xAA00
    mov r5, 0xAA
    eor r6, r4, r5 << 8
    
    mov r7, 0xFFFF
    lsl r7, 0x10
    mov r8, 0x00FF
    lsl r8, 0x8
    
    eor r9, r8, r7 << 8
    
    
    
"""

EXPECTED_RESULTS = {
    "r0": 0xaa,
    "r1": 0xfa,
    "r2": 0x50,
    "r3": 0,
    "r4": 0x0000aa00,
    "r5": 0x000000aa,
    "r6": 0,
    "r7": 0xffff0000,
    "r8": 0x0000ff00,
    "r9": 0xff00ff00,
    "r10": 0,
    "r11": 0,
    "r12": 0,
    "sregC": 0,
    "sregZ": 0,
    "sregN": 1,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
