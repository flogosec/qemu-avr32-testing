

TEST = """
   mov r0, 0xA
   mov r1, 0x5
   divu r2, r0, r1
   
   mov r4, -0xC
   mov r5, 0x5
   divu r5, r4, r5

    mov r7, 0xC
    mov r8, -0x5
    divu r9, r7, r8
    
    divu r11, r4, r8

"""

EXPECTED_RESULTS = {
    "r0": 0xA,
    "r1": 0x5,
    "r2": 0x2,
    "r3": 0x0,
    "r4": 0xfffffff4,
    "r5": 0x33333330,
    "r6": 0x00000004,
    "r7": 0x0000000c,
    "r8": 0xfffffffb,
    "r9": 0,
    "r10": 0x0000000c,
    "r11": 0,
    "r12": 0xfffffff4,
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
