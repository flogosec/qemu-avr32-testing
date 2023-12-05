

TEST = """
   mov r0, 0xA
   mov r1, 0x5
   divs r2, r0, r1
   
   mov r4, -0xE
   mov r5, 0x5
   divs r5, r4, r5

    mov r7, 0xC
    mov r8, -0x5
    divs r9, r7, r8
    
    divs r11, r4, r8
"""

EXPECTED_RESULTS = {
    "r0": 0xA,
    "r1": 0x5,
    "r2": 0x2,
    "r3": 0x0,
    "r4": 0xfffffff2,
    "r5": 0xfffffffe,
    "r6": 0xfffffffc,
    "r7": 0x0000000c,
    "r8": 0xfffffffb,
    "r9": 0xfffffffe,
    "r10": 0x00000002,
    "r11": 0x00000002,
    "r12": 0xfffffffc,
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
