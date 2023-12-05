
TEST = """
    # cc, not c-flag. No branch.
    ssrf 0x0
    brhs point2

    point1:
    mov r0, 0x1234

    point2:
    mov r1, 0x1111

    point3:

"""

EXPECTED_RESULTS = {
    "r0": 0x1234,
    "r1": 0x1111,
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
    "sregN": 0,
    "sregV": 0,
    "sregQ": 0,
    "sregL": 0,
    "sreg6": 0,
    "sreg7": 0,
    "sreg8": 0
}
