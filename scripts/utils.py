def ROR(x, n, bits=32):
    mask = (2**n) -1
    mask_as_bits = x & mask
    return (x>>n) | (mask_as_bits << (bits - n))

def ROL(x, n, bits=32):
    return ROR(x, bits-n, bits)
