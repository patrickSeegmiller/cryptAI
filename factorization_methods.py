from whole_number_tools import fast_powering_algorithm, integer_sqrt, is_square, integer_nthrt, find_modular_inverse, greatest_common_divisor, absolute_value, integer_quadratic_formula, get_factor_base
from rational_number_tools import continued_fraction_expansion, get_continued_fraction_convergents
from primality_tests import miller_rabin_primality_test

def continued_fraction_factorization(e: int, N: int) -> list[int]:
    """
    Performs continued fraction factorization on the RSA public exponent `e` and modulus `N`. 

    Args:
        e (int): The RSA public exponent.
        N (int): The RSA modulus.

    Returns:
        list[int]: A list containing the two factors of `N`.

    Raises:
        ValueError: If `e` or `N` are not positive integers.

    """

    # We first check that e and N are positive integers.
    if not isinstance(e, int) or e <= 0 or not isinstance(N, int) or N <= 0:
        raise ValueError("e and N must be positive integers.")
    
    # Now we get the convergents of the continued fraction expansion of e/N.
    convergents = get_continued_fraction_convergents(continued_fraction_expansion(e, N))

    for num, denom in convergents:
        if num == 0:
            continue
        p, q = integer_quadratic_formula(1, ((e*denom - 1) // num) - N - 1, N)
        if (p != None) and (q!= None):
            if (p * q) == N:
                return [p, q]

    return None

def fermat_factorization(n: int) -> list[int]:
    """
    Performs Fermat's method for factoring an odd number `n`. Fermat's method relies on the fact that any 
    odd number can be expressed as a difference of squares. It checks numbers near the square root of `n` 
    for ways in which `n` can be written as a difference of perfect squares, because if `n = b^2 - a^2`, 
    it factors as `n = (b-a)(b+a)`.

    Args:
        n (int): The number to be factored.

    Returns:
        list[int]: A list containing the two factors of `n`.

    Raises:
        ValueError: If `n` is not an odd number greater than 1.

    """

    # We first check that n is an odd number greater than 1.
    if not isinstance(n, int) or n <= 1 or n % 2 == 0: 
        raise ValueError("n should be an odd number greater than 1.")
    
    # Next we check whether n is a perfect square.
    if is_square(n):
        return [integer_sqrt(n), integer_sqrt(n)]

    # Now we perform Fermat's method, starting with a = sqrt(n) + 1.
    # We check whether a^2 - n is a perfect square. If not, we increment a by 1 and repeat.
    try:
        a = integer_sqrt(n-1) + 1
        b_squared = a*a - n
        while not is_square(b_squared):
            a = a + 1
            b_squared = a*a - n
    except KeyboardInterrupt:
        print("Fermat's method was interrupted by the user.")
        return None

    # We return the factors of n.
    return [a - integer_sqrt(b_squared), a + integer_sqrt(b_squared)]

def known_decryption_key_factorization(decryption_key, public_exponent, modulus):
    """
    Uses the Chinese Remainder Theorem to factor a modulus N when the decryption key d is known.
    
    Args:
        decryption_key (int): The decryption key d.
        public_exponent (int): The public exponent e.
        modulus (int): The modulus N.

    Returns:
        list[int]: A list containing the two factors of N.

    Raises:
        ValueError: If the public exponent and the modulus are not positive integers.

    """

    k = decryption_key * public_exponent - 1
    factors_of_two = 0
    while k % 2 == 0:
        factors_of_two += 1
        k = k // 2

    # TODO: Finish this function. Will use the Chinese Remainder Theorem to factor N through the decryption key d.

def pollard_p_1_factorization(N: int, a=2) -> list[int]:
    """
    Factorizes a composite number N using Pollard's p - 1 Factorization Algorithm. Pollard's 

    Args:
        N (int): The number to be factorized.
        a (int, optional): The base to be used in the factorization algorithm. Defaults to 2.

    Returns:
        list[int]: A list containing two nontrivial factors of N.

    Raises:
        ValueError: If N is a probable prime, which is checked by using the Miller-Rabin primality test.

    """

    # Check whether N is a probable prime.
    if miller_rabin_primality_test(N):
        raise ValueError(f"{N} is a probable prime, so it (almost certainly) cannot be factorized.")
   
    # Set the upper bound for the exponent in the factorization algorithm.
    UPPER_BOUND = 1000000

    # Perform the factorization algorithm.
    for i in range(2, UPPER_BOUND):
        a = fast_powering_algorithm(a, i, N)
        d = greatest_common_divisor(a - 1, N)
        if 1 < d and d < N:
            print(f"Pollard's p - 1 Factorization Algorithm factored {N}: ", end="")
            return [d, N // d]

    print(f"Pollard's p - 1 Factorization Algorithm did not succeed in finding a non trivial factor of {N} with an upper bound of {UPPER_BOUND}.")
    return None

def pollard_rho_factorization(N: int, x=1, y=2) -> list[int]:
    """
    Uses Pollard's rho factorization algorithm to factor a composite number N

    Args:
        N (int): The number to be factorized.
        x (int, optional): The initial value of x. Defaults to 1.
        y (int, optional): The initial value of y. Defaults to 2.

    Returns:
        list[int]: A list containing two nontrivial factors of N.

    Raises:
        ValueError: If N is a probable prime, which is checked by using the Miller-Rabin primality test.
        Exception: If the maximum number of iterations has been reached without finding a nontrivial factor of N.

    """

    # Check whether N is a probable prime.
    if miller_rabin_primality_test(N):
        raise ValueError(f"{N} is a probable prime, so it (almost certainly) cannot be factorized.")

    # Set the maximum number of iterations for the factorization algorithm.
    MAX_ITERATIONS = 1000000

    # Perform the factorization algorithm.
    g = greatest_common_divisor(absolute_value(y - x), N)
    for i in range(MAX_ITERATIONS):
        x = (x**2 + 1) % N
        y = (y**2 + 1) % N
        y = (y**2 + 1) % N
        g = greatest_common_divisor(absolute_value(y - x), N)
        if g > 1 and g < N:
            return [g, N // g] 

    # Raise an exception if the maximum number of iterations has been reached without finding a nontrivial factor of N.
    raise Exception(f"The maximum number of iterations has been reached without finding any nontrivial factors of {N}.")

def quadratic_sieve(N, B):
    """
    TODO: Docstring
    """

    #TODO: Implement the algorithm

def rational_sieve(N, B):
    """
    TODO: Docstring
    """
    factor_base = get_factor_base(B)

    # Check for divisibility by the primes in the factor base.
    for factor in factor_base:
        if N % factor == 0:
            return [factor, N // factor]
        
    # TODO: Implement the rest of the algorithm

def shanks_square_forms_factorization(N):
    """
    TODO: Docstring
    """

    # TODO: Implement the algorithm

def trial_division_factorization(N: int) -> list[int]:
    """
    Applies trial division up to the square root of N to factor N.
    
    Args:
        N (int): The number to be factorized.

    Returns:
        list[int]: A list containing two factors of N.

    Raises:
        ValueError: If N is a probable prime, which is checked by using the Miller-Rabin primality test.

    """

    # Check whether N is a probable prime.
    if miller_rabin_primality_test(N):
        raise ValueError(f"{N} is a probable prime, so it (almost certainly) cannot be factorized.")

    # Perform trial division up to the square root of N.
    for i in range(2, integer_sqrt(N) + 1):
        if N % i == 0:
            print(f"Trial division factored {N}: ", end="")
            return [i, N // i]

    print(f"Trial division did not succeed in finding a non trivial factor of {N}.")
    return None

def williams_p_1_factorization(N: int, B=1000) -> list[int]:
    """
    Factorizes a composite number N using Williams' p + 1 Factorization Algorithm.

    Args:
        N (int): The number to be factorized.
        B (int, optional): The bound to be used in the factorization algorithm. Defaults to 1000.

    Returns:
        list[int]: A list containing two nontrivial factors of N.

    Raises:
        ValueError: If N is a probable prime, which is checked by using the Miller-Rabin primality test.

    """

    # TODO This needs to be tested.

    # Check whether N is a probable prime.
    if miller_rabin_primality_test(N):
        raise ValueError(f"{N} is a probable prime, so it (almost certainly) cannot be factorized.")

    # Set the upper bound for the exponent in the factorization algorithm.
    UPPER_BOUND = 1000000

    # Perform the factorization algorithm.
    for i in range(2, UPPER_BOUND):
        a = fast_powering_algorithm(2, i, N)
        d = greatest_common_divisor(a - 1, N)
        if 1 < d and d < N:
            print(f"Williams' p + 1 Factorization Algorithm factored {N}: ", end="")
            return [d, N // d]

    print(f"Williams' p + 1 Factorization Algorithm did not succeed in finding a non trivial factor of {N} with an upper bound of {UPPER_BOUND}.")
    return None