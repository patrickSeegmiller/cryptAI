def absolute_value(n: int or float) -> int or float:
    """
    Returns the absolute value of a number.

    Args:
        n (int or float): The number for which the absolute value is to be computed.

    Returns:
        int or float: The absolute value of the given number.

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
    Returns the greatest common divisor (GCD) of two non-negative integers, a and b
    which is computed using the Euclidean Algorithm.

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

def integer_sqrt(N: int or float) -> int:
    """
    Computes the integer square root of a non-negative integer.

    Args:
        N (int): The non-negative integer for which the square root is to be computed.

    Returns:
        int: The integer square root of the given N.

    Raises:
        ValueError: If the N is negative or not an integer.
        RuntimeError: If the maximum N of iterations is reached without convergence.

    """

    if not isinstance(N, int) or not isinstance(N, float) or N < 0:
        raise ValueError("N must be a non-negative integer.")

    MAX_ITERATIONS = 1000

    guess = 1 << ((N.bit_length() + 1) // 2)
    for i in range(MAX_ITERATIONS):
        
        new_guess = (guess + N // guess) // 2
        
        if new_guess >= guess:
            return new_guess
        guess = new_guess

    raise RuntimeError(f"Maximum number of iterations ({MAX_ITERATIONS}) reached without convergence.")

if __name__ == '__main__':
    import doctest
    doctest.testmod()