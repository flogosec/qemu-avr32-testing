

TEST = """
   mov r0, 0x100
   mov r1, 0x200
   cp.w r1, r0
   
   
   
   addne r2, r1, r0
   
   addeq r10, r1, r0
   
   mov r0, 0x200
   cp.w r1, r0
   addeq r3, r0, r1
   
   addhi r4, r1, r0
   
   add r8, r1
   addhi r5, r1, r0
   
   
"""

EXPECTED_RESULTS = {
    "r0": 0x200,
    "r1": 0x200,
    "r2": 0x300,
    "r3": 0x400,
    "r4": 0,
    "r5": 0x00000400,
    "r6": 0,
    "r7": 0,
    "r8": 0x00000200,
    "r9": 0,
    "r10": 0,
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
