
def twos_complement(value, bits):
    """Signs a value with an arbitrary number of bits."""
    if value >= (1 << (bits - 1)):
        value = -((~value + 1) + (1 << bits))
    return value
