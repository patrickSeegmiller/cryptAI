def absolute_value(n: int or float) -> int or float:
    """
    Returns the absolute value of a number.

    Args:
        n (int or float): The number for which the absolute value is to be computed.

    Returns:
        int or float: The absolute value of the given number.

    """

    # Input validation
    if not isinstance(n, int) and not isinstance(n, float):
        raise ValueError("n must be an integer or a float.")
    
    # Return the absolute value of n
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

    # Input validation
    if not isinstance(base, int) or not isinstance(exponent, int) or not isinstance(modulus, int) or exponent < 0 or modulus < 0:
        raise ValueError("xponent, and modulus must be non-negative integers.")
    
    # Convert the exponent to binary and reverse it
    binary_N = f'{exponent:08b}'[::-1]
    exponents = [int(bit) for bit in binary_N]
    
    # Compute the value of base^exponent modulo modulus
    power_of_base = base
    value = base ** exponents[0]
    for i in range(1, len(binary_N)):
        power_of_base = (power_of_base ** 2) % modulus
        value = (value * (power_of_base ** exponents[i])) % modulus

    # Return the result 
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

    # Input validation
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers.")

    # Use the Euclidean Algorithm to compute the GCD
    while a != 0:
        a, b = b % a, a
    
    # Return the GCD
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

    # Input validation
    if not isinstance(N, int) or not isinstance(N, float) or N < 0:
        raise ValueError("N must be a non-negative integer.")

    # Maximum number of iterations
    MAX_ITERATIONS = 1000

    # Initial guess for the square root of N
    guess = 1 << ((N.bit_length() + 1) // 2)

    # Use a binary search until convergence or maximum number of iterations is reached
    for i in range(MAX_ITERATIONS):

        new_guess = (guess + N // guess) // 2
        #
        if new_guess >= guess:
            return new_guess
        guess = new_guess

    # If the maximum number of iterations is reached without convergence, raise an error
    raise RuntimeError(f"Maximum number of iterations ({MAX_ITERATIONS}) reached without convergence.")

def is_square(n: int) -> bool: 
    """
    Determines whether a whole number is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a perfect square, False otherwise.

    """

    # Input validation
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Check if the square root of n is an integer and return the result
    return integer_sqrt(n)**2 == n

def find_modular_inverse(a, m):
    """
    TODO: Docstring
    """
    if greatest_common_divisor(a,m) != 1: # If 'a' and 'm' are not relatively prime, 'a' has no modular inverse.
        return None     

    # We use the Extended Euclidean Algorithm to compute the multiplicative inverse of 'a' modulo 'm':
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3    
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def chinese_remainder_theorem(moduli, remainders):
    """
    TODO: Docstring
    """
    new_modulus = 1
    x = 0
    
    for i in range(len(moduli)):
        new_modulus *= moduli[i]
        product = 1
        for j in range(len(moduli)):
            if i == j:
                continue
            product *= moduli[j]

        x += remainders[i] * product * find_modular_inverse(product, moduli[i])
            
    return x % new_modulus

if __name__ == '__main__':
    import doctest
    doctest.testmod()