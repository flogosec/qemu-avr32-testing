

TEST = """
   mov r0, 0x100
   abs r0
   mov r1, -0x100
   abs r1
   mov r2, -0x579
   abs r2
   
   
   mov r4, 0x8000
   lsl r4, 0x10
   abs r4
   
   abs r3
"""

EXPECTED_RESULTS = {
    "r0": 0x100,
    "r1": 0x100,
    "r2": 0x579,
    "r3": 0,
    "r4": 0x80000000,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0,
    "r11": 0,
    "r12": 0,
    "sregC": 0,
    "sregZ": 1,
    "sregN": 1,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
