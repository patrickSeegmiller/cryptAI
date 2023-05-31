def absolute_value(n):
    """
    
    """
    if n >= 0:
        return n
    else:
        return -n

def fast_powering_algorithm(base: int, exponent: int, modulus: int) -> int:
    """
    Compute the value of `base`^`exponent` modulo `modulus` using the fast powering algorithm.
    
    The fast powering algorithm computes the value of `base`^`exponent` modulo `modulus` by expressing
    `exponent` in binary, in order of increasing powers of 2. Powers of `base` are computed, reducing modulo
    `modulus` at each step.
    
    Args:
        base (int): The base value.
        exponent (int): The exponent value.
        modulus (int): The modulus value.
    
    Returns:
        int: The result of `base`^`exponent` modulo `modulus`.
    """

    binary_N = f'{exponent:08b}'[::-1]
    exponents = [int(bit) for bit in binary_N]
    
    power_of_base = base

    value = base ** exponents[0]

    for i in range(1, len(binary_N)):
        power_of_base = (power_of_base ** 2) % modulus
        value = (value * (power_of_base ** exponents[i])) % modulus
        
    return value

def greatest_common_divisor(a: int, b: int) -> int: # The Euclidean Algorithm
    """
    Returns the greatest common divisor (GCD) of two non-negative integers, a and b.

    The greatest common divisor of two non-negative integers, a and b, is the largest
    integer that divides both a and b without leaving a remainder. The Euclidean Algorithm
    is used to compute the GCD of two non-negative integers, by repeatedly applying the
    following rule: if a > b, then the GCD of a and b is the same as the GCD of b and the
    remainder of a divided by b. This process is repeated until the remainder is 0, at
    which point the GCD is the last non-zero remainder.

    Args:
        a (int): The first non-negative integer.
        b (int): The second non-negative integer.

    Returns:
        int: The greatest common divisor (GCD) of a and b.

    Raises:
        ValueError: If a or b is not a non-negative integer.

    """

    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers.")

    while a != 0:
        a, b = b % a, a
    return b

if __name__ == '__main__':
    