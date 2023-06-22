import math

from whole_number_operations import integer_sqrt
from prime_number_sieves import sieve_of_eratosthenes
from ngram_tools import get_ngram_frequency_from_file, get_ngram_frequency
from factorization_methods import fermat_factorization, trial_division_factorization, pollard_rho_factorization, pollard_p_1_factorization, williams_p_1_factorization#, quadratic_sieve_factorization, shanks_square_forms_factorization, rational_sieve, general_number_field_sieve

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

def generate_ngram_frequencies(file_path: str, n=[1, 2, 3, 4]) -> None:
    """
    Generates a file containing the relative frequency distribution of n-grams from a file of text.
    The generated file consists of max(n) sections sepearated by a line containing only the character "#" and
    each section contains the frequency distribution of n-grams of length n. The format of each section is as follows:
        n-gram, relative_frequency
        n-gram, relative_frequency
        ...
    Only the 20 most common n-grams are included in the file for n-grams of length greater than one.

    Args:
        file_path (str): The path to the file to compute the frequency distribution of.
        n (list): A list of integers representing the number of characters in each n-gram.

    Raises:
        ValueError: If file_path is not a string or n is not a list of positive integers.

    """

    # Check that file_path is a valid.
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string.")
    
    # Check that n is a list of positive integers.
    if not isinstance(n, list) or not all(isinstance(i, int) and i > 0 for i in n):
        raise ValueError("n must be a list of positive integers.")
    
    # Initialize a dictionary to store the frequency distributions of the different n-grams.
    ngram_frequencies = {}

    # Open the file and iterate over each line.
    with open(file_path, "r") as file:
        for line in file:
            # Iterate over each n-gram in the line, adding it to the dictionary or
            # incrementing its count if it already exists.
            for i in range(len(line) - max(n) + 1):
                for j in n:
                    n_gram = line[i:i+j]
                    if n_gram in ngram_frequencies:
                        ngram_frequencies[n_gram] += 1
                    else:
                        ngram_frequencies[n_gram] = 1

    # Sort the n-grams in each frequency distribution by their frequency.
    for ngram_frequency in ngram_frequencies.values():
        ngram_frequency = dict(sorted(ngram_frequency.items(), key=lambda item: item[1], reverse=True))

    # Write the frequency distributions to a file.
    with open("ngram_frequencies.txt", "w") as file:
        for i in range(max(n)):
            for ngram, frequency in ngram_frequencies[i].items():
                file.write(f"{ngram}, {frequency}\n")
            file.write("#\n")
    
    # Return the frequency distribution dictionary.
    return ngram_frequencies

def load_ngram_frequencies(file_path: str) -> dict:
    """
    Loads a dictionary containing the relative frequency distribution of n-grams from a file. The format of 
    is as follows:
        n-gram, relative_frequency
        n-gram, relative_frequency
        ...
    Only the 20 most common n-grams are included in the file for n-grams of length greater than one (for now!).
    """

    # Check that file_path is a string.
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string.")
    
    # Initialize a dictionary to store the frequency distributions of the different n-grams.
    ngram_frequencies = {}

    # Initialize the n-gram size.
    n = 1

    # Open the file and iterate over each line.
    with open(file_path, "r") as file:
        # Skip the first line.
        next(file)

        # For each of the four sections, iterate over each line, adding the n-gram and its
        # relative frequency to a dictionary. Then add the dictionary to the ngram_frequencies dictionary.
        for line in file:
            if line == "#\n":
                frequency_distribution = {}
                ngram_frequencies[n] = frequency_distribution
                n += 1
            else:
                ngram, frequency = line.split(", ")
                frequency_distribution[ngram] = float(frequency)
        
    # Return the ngram_frequencies dictionary.
    return ngram_frequencies

def factorization_attack(n: int, algo='trial_division') -> tuple:
    """
    Attempts to factor a positive integer n by brute force using the selected factorization algorithm. 
    
    Args:
        n (int): The number to factor.
        algo (str): The factorization algorithm to use. Options are 'trial_division', 'pollard_rho', 'pollard_p_1', 
            'williams_p_1', 'fermat', 'shanks_square_forms', 'rational_sieve', 'quadratic_sieve', and 'general_number_field_sieve'.

    """
    # Check that n is a positive integer.
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")
    
    # Check that algo is a valid factorization algorithm.
    if algo not in ['trial_division', 'pollard_rho', 'pollard_p_1', 'williams_p_1', 'fermat', 'shanks_square_forms', 'rational_sieve', 'quadratic_sieve', 'general_number_field_sieve']:
        raise ValueError("algo must be a valid factorization algorithm.")
    
    # Set a maximum number of iterations for the factorization algorithm.
    max_iterations = 1000000
    
    # Initialize a dictionary to store the factorization algorithms.
    factorization_algorithms = {
        'trial_division': trial_division_factorization,
        'pollard_rho': pollard_rho_factorization,
        'pollard_p_1': pollard_p_1_factorization,
        'williams_p_1': williams_p_1_factorization,
        'fermat': fermat_factorization,
        'shanks_square_forms': shanks_square_forms_factorization,
        'rational_sieve': rational_sieve,
        'quadratic_sieve': quadratic_sieve_factorization,
        'general_number_field_sieve': general_number_field_sieve
    }

    # Factor n using the selected factorization algorithm and return the factors or max_iterations is reached
    # without finding the factors.
    factors = factorization_algorithms[algo](n, max_iterations)
    
    # Raise an exception if the factors were not found.
    if factors is None:
        raise Exception(f"Factors not found after {max_iterations} iterations of the {algo} algorithm.")
    return factors



    




    







