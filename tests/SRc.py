

TEST = """
    
    srhi r0
    srne r1
    
    srlo r10
    ssrf 0x0
    srlo r2
    
    sreq r11
    
    ssrf 0x3
    srle r12
    
    ssrf 0x1
    sreq r3    
    
"""

EXPECTED_RESULTS = {
    "r0": 0x1,
    "r1": 0x1,
    "r2": 0x1,
    "r3": 0x1,
    "r4": 0,
    "r5": 0,
    "r6": 0,
    "r7": 0,
    "r8": 0,
    "r9": 0,
    "r10": 0,
    "r11": 0,
    "r12": 0x1,
    "sregC": 1,
    "sregZ": 1,
    "sregN": 0,
    "sregV": 1,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
