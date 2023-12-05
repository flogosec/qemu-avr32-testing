

TEST = """

    mov r0, 0x1234
    bral point1
    
    # rjmp target
    mov r1, 0x1234
        
    
    mov r2, 0x1234
    bral point2
    
    mov r3, 0x1234
    
    point1:
    rjmp -0x10
    point2:
    mov r4, 0x1234
    rjmp 0x6
    mov r5, 0x1234
    mov r6, 0x1234

"""

EXPECTED_RESULTS = {
    "r0": 0x1234,
    "r1": 0x1234,
    "r2": 0x1234,
    "r3": 0,
    "r4": 0x1234,
    "r5": 0,
    "r6": 0x1234,
    "r7": 0,
    "r8": 0,
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
