from random import randint

from whole_number_operations import fast_powering_algorithm, integer_sqrt, greatest_common_divisor
from prime_number_sieves import sieve_of_eratosthenes

def trial_division_primality_test(n: int) -> bool:
    """
    Determines whether n is a prime number by checking whether any integer in the interval
    [2, integer_sqrt(n)] is a divisor of n.

    Args:
        n (int): The integer to test for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """

    # Input validation
    if not isinstance(n, int) or n <= 1:
        raise ValueError("n must be a positive integer greater than 1.")

    # We first check that n is a positive integer greater than 1.
    # If n is 2 or 3, we return True.
    if n <= 3:
        return n > 1

    # If n > 3, we check whether any integer in the interval [2, integer_sqrt(n)] is a divisor of n.
    limit = integer_sqrt(n)
    for i in range(2, limit):
        if n % i == 0:
            return False
        
    # If no integer in the interval [2, integer_sqrt(n)] is a divisor of n, we return True.
    return True

def sixk_plus_one_primality_test(n: int) -> bool:
    """
    Determines whether n is a prime number by first checking whether n is divisible by 2 or
    3, and then checking any integer of the form 6k+-1 in the interval [5, integer_sqrt(n)] is a
    divisor of n (where k is a whole number). This works since any prime number other than 2
    and 3 can be written as 6k+1 or 6k-1, where k is a whole number.

    Args:
        n (int): The integer to test for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """

    # Input validation
    if not isinstance(n, int) or n <= 1:
        raise ValueError("n must be a positive integer greater than 1.")

    # First, we check if n equals 2 or 3, or if n is divisible by 2 or 3.
    if n <= 3:
        return n > 1
    if (n % 2 == 0) or (n % 3 == 0):
        return False

    # If n is not divisible by 2 or 3, we check whether any integer of the form 6k+-1 in the interval
    # [5, integer_sqrt(n)] is a divisor of n.
    limit = integer_sqrt(n)
    for i in range(5, limit+1, 6):
        if (n % i == 0) or (n % (i+2) == 0):
            return False
    return True

def primes_only_primality_test(n: int) -> bool:
    """
    Determines whether n is a prime number by checking whether any prime number in the interval
    [2, integer_sqrt(n)] is a divisor of n. The list of prime numbers is first obtained by way of the
    Sieve of Eratosthenes with an upper limit equal to integer_sqrt(n).

    Args:
        n (int): The integer to test for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """

    # Input validation
    if not isinstance(n, int) or n <= 1:
        raise ValueError("n must be a positive integer greater than 1.")
    
    # If n is 2 or 3, we return True.
    if n <= 3:
        return n > 1

    # If n > 3, we check whether any prime number in the interval [2, integer_sqrt(n)] is a divisor of n.
    primes_up_to_sqrt_n = sieve_of_eratosthenes(integer_sqrt(n))
    for prime in primes_up_to_sqrt_n:
        if n % prime == 0:
            return False
        
    # If no prime number in the interval [2, integer_sqrt(n)] is a divisor of n, we return True.
    return True

def fermat_primality_test(n: int) -> bool:
    """Determines whether n is likely to be a prime number using Fermat's Little Theorem.

    Fermat's Little Theorem states that if n is a prime number and a is any positive integer
    less than n, then a raised to the power of (n-1) is congruent to 1 modulo n. This test
    checks whether a number in the interval [2, n-1] is a witness for the compositeness of n
    using Fermat's Little Theorem. However, it is important to note that there are infinitely
    many values (called Carmichael numbers) for which this test fails.

    Args:
        n (int): The integer to test for primality.

    Returns:
        bool: True if n is likely to be prime, False otherwise.

    Raises:
        ValueError: If n is not a positive integer greater than 1.
    """

    # We first check that n is a positive integer greater than 1.
    if not isinstance(n, int) or n <= 1:
        raise ValueError("n should be a positive integer greater than 1.")

    # We then check whether any number in the interval [2, n-1] is a Fermat witness for the compositeness of n
    for i in range(1,n):
        if (fast_powering_algorithm(i, n, n) - i) % n != 0:
            return False
    return True

def miller_rabin_primality_test(n, num_potential_witnesses = 100, percent_certain = None):
    """
    Determines whether `n` is likely to be a prime number using the Miller-Rabin primality test.

    Args:
        n (int): The integer to test for primality.
        number_of_potential_witnesses (int, optional): The number of integers to check as 
        potential witnesses to the compositeness of `n`. Defaults to 100.
        percent_certain (float, optional): How certain the user wants to be that `n` is prime 
        as a decimal on the interval [0, 1). Defaults to 0.99.

    Returns:
        bool: True if `n` is likely to be prime, False otherwise.
    """
   
    # If percent_certain is specified we determine the approximate number of potential
    # witnesses of compositeness that need to be tested.
    if percent_certain != None:
        num_potential_witnesses = int((-1 / 2) * math.log2(percent_certain / log(n)))

    # We randomly select integers in the interval [2,n) that we will use as potential witnesses
    # for the compositeness of n.
    potentialWitnesses = [randint(2,n) for i in range(num_potential_witnesses)]

    # Lastly, we iterate through each potential witness, checking each with the
    # miller_rabin_witness_for_compositeness function.
    for potentialWitness in potentialWitnesses:
        if miller_rabin_witness_for_compositeness(n,potentialWitness):
            return False

    return True # n is likely prime
    

def miller_rabin_witness_for_compositeness(n: int, potential_witness: int) -> bool:
    """
    Determines whether a number is a witness for the compositeness of another number using the Miller-Rabin algorithm.

    Args:
        n (int): The number to be tested for compositeness.
        potential_witness (int): The number that may demonstrate n is composite.

    Returns:
        bool: True if the potential witness is a witness for the compositeness of n, False otherwise.

    """

    # First we check whether n is even or shares a nontrivial factor with the potentialWitness.
    if (n % 2 == 0) or (greatest_common_divisor(n, potentialWitness) != 1):
        return True # n is composite

    # Now we break the value n-1 into 2^k times an odd number called oddPart
    # by repeatedly dividing by 2 until the result is odd. 
    k = 0
    oddPart = n-1 # oddPart is initialized to n-1
    # We divide oddPart by 2 until it is odd, incrementing k each time
    while oddPart % 2 == 0:
        k += 1
        oddPart = oddPart // 2

    # Check whether the qth power of the potential witness is congruent to 1 modulo n.
    # If it is, the test fails, meaning n -might- be prime. The Fast Powering
    # Algorithm is applied to simplify the computation
    potentialWitness = fast_powering_algorithm(potentialWitness,oddPart,n)   
    if (potentialWitness - 1) % n == 0:
        return False # n may be prime

    # Check whether the (2^j)*q-th power of the potential witness is congruent to -1 
    # modulo n for j from 1 to k. If it is, the test fails, meaning n -might- be prime.
    for i in range(k):
        if (-1 % n == potentialWitness):
            return False # n may be prime
        potentialWitness = (potentialWitness ** 2) % n

    # If we make it through all the tests, the potentialWitness is a witness for the
    # compositeness of n. That is, n is definitely composite.
    return True # n is composite


def miller_rabin_get_prime(lower_limit: int = 2**1024, upper_limit: int = 2**1025) -> int:
    """
    Generates a probable prime number within the specified range [lower_limit, upper_limit] using
    the Miller-Rabin primality test.

    Args:
        lower_limit (int, optional): The lower limit of the range. Defaults to 2^1024.
        upper_limit (int, optional): The upper limit of the range. Defaults to 2^1025.

    Returns:
        int: A probable prime number within the specified range.

    Raises:
        ValueError: If the lower_limit is greater than the upper_limit.
        RuntimeError: If the maximum number of iterations is reached without finding a probable prime.

    Note:
        The function uses the Miller-Rabin primality test to identify probable prime numbers.

    """

    # Check that the lower limit is less than the upper limit
    if lower_limit > upper_limit:
        raise ValueError("Lower limit should be less than or equal to the upper limit.")

    # Initialize the maximum number of iterations``
    MAX_ITERATIONS = 10000

    # Generate a random number in the specified range
    n = randint(lower_limit, upper_limit)

    # Iterate through the range until a probable prime is found
    for i in range(MAX_ITERATIONS):
        if miller_rabin_primality_test(n):
            return n
        n = randint(lower_limit,upper_limit)

    # Raise a RuntimeError if we reach this point without finding a probable prime
    raise RuntimeError(f"Maximum number of iterations {MAX_ITERATIONS} reached without locating a probable prime.")
