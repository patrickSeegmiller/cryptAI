from whole_number_operations import integer_sqrt
from prime_number_sieves import sieve_of_eratosthenes

def index_of_coincidence(text):
    """
    Calculates the index of coincidence of a string of text.

    Args:
        text (str): The text to calculate the index of coincidence of.

    Returns:
        float: The index of coincidence of the text.

    Raises:
        ValueError: If text is not a string.

    References:
        https://en.wikipedia.org/wiki/Index_of_coincidence
    """

    # Input validation
    if not isinstance(text, str):
        raise ValueError("text must be a string.")

    # Initialize a dictionary to count the number of occurrences of each letter
    # in the text.
    letter_counts = {}

    # Iterate over each letter in the text, adding it to the dictionary or
    # incrementing its count if it already exists.
    for letter in text:
        if not letter.isalpha():
            continue
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # Calculate the index of coincidence by summing the product of the number of
    # occurrences of each letter and the number of occurrences of each letter
    # minus 1, then dividing by the product of the length of the text and the
    # length of the text minus 1.
    index_of_coincidence = 0
    for letter in letter_counts:
        index_of_coincidence += letter_counts[letter] * (letter_counts[letter] - 1)
    index_of_coincidence /= len(text) * (len(text) - 1)

    # Return the index of coincidence.
    return index_of_coincidence

def get_factor_pairs(n: int) -> list[tuple]:
    """
    Returns a list of all factor pairs of a positive integer. This is intended
    to be used for breaking columnar transposition ciphers by identifying the
    possible grid sizes.

    Args:
        n (int): The positive integer to get the factor pairs of.

    Returns:
        list[tuple]: A list of tuples containing the factor pairs of n.

    Raises:
        ValueError: If n is not a positive integer.
    """

    # Check that n is a positive integer.
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    # Initialize a list to store the factor pairs.
    factor_pairs = []

    # Iterate over all integers up to the square root of n.
    for i in range(1, integer_sqrt(n)+  1) : 
        # If i is a factor of n, add the factor pair (i, n/i) to the list.
        if n % i == 0:
            factor_pairs.append((i, n/i))

    # Return the list of factor pairs.
    return factor_pairs

def get_prime_factorization(n: int) -> list[tuple]:
    """
    Returns the prime factorization of a positive integer as a list of tuples where the
    first element of each tuple is a prime factor and the second element is the
    power to which that prime factor is raised.

    Args:
        n (int): The positive integer to factorize.

    Returns:
        list[tuple]: A list of tuples containing the prime factorization of n.

    Raises:
        ValueError: If n is not a positive integer.
    
    References:
        https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    """

    # Check that n is a positive integer.
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    # Initialize a list to store the prime factorization.
    prime_factorization = []

    # Iterate over all prime numbers less than or equal to the square root of n.
    for i in sieve_of_eratosthenes(integer_sqrt(n)):
        # If i is a factor of n, determine the power on i, and add (i, power) to the list.
        if n % i == 0:
            # Initialize a variable to store the power to which i is raised.
            power = 0

            # Divide n by i until it is no longer a factor of n, incrementing the
            # power each time.
            while n % i == 0:
                n //= i
                power += 1

            # Add the factor pair (i, power) to the prime factorization list.
            prime_factorization.append((i, power))

    # Return the prime factorization list.
    return prime_factorization