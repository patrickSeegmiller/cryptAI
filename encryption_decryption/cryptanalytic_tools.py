import math

from number_theoretic_tools.whole_number_operations import integer_sqrt
from number_theoretic_tools.prime_number_sieves import sieve_of_eratosthenes
from number_theoretic_tools.factorization_methods import fermat_factorization

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

def get_ngram_frequency(text: str, n: int) -> dict:
    """
    Computes and returns the frequency distribution of n-grams from a string of text, where n is the number of
    characters in each n-gram. This is particularly useful for cracking monoalphabetic, polyalphabetic,
    polygraphic, and columnar transposition ciphers, especially when used in conjunction with metaheuristic
    algorithms such as simulated annealing.

    Args:
        text (str): The text to compute the frequency distribution of.
        n (int): The number of characters in each n-gram.

    Returns:
        dict: A dictionary containing the frequency distribution of n-grams.

    Raises:
        ValueError: If text is not a string or n is not a positive integer.

    """

    # Check that text is a string and n is a positive integer.
    if not isinstance(text, str) or not isinstance(n, int) or n <= 0:
        raise ValueError("text must be a string and n must be a positive integer.")
    
    # Initialize a dictionary to store the frequency distribution of n-grams.
    frequency_distribution = {}

    # Iterate over each n-gram in the text, adding it to the dictionary or
    # incrementing its count if it already exists.
    for i in range(len(text) - n + 1):
        n_gram = text[i:i+n]
        if n_gram in frequency_distribution:
            frequency_distribution[n_gram] += 1
        else:
            frequency_distribution[n_gram] = 1

    # Return the frequency distribution dictionary.
    return frequency_distribution

def get_ngram_frequency_from_file(file_path: str, n: int) -> dict:
    """
    Computes and returns the frequency distribution of n-grams from a file, where n is the number of
    characters in each n-gram. See get_ngram_frequency for more information.

    Args:
        file_path (str): The path to the file to compute the frequency distribution of.
        n (int): The number of characters in each n-gram.

    Returns:
        dict: A dictionary containing the frequency distribution of n-grams.

    Raises:
        ValueError: If file_path is not a string or n is not a positive integer.

    """

    # Check that file_path is a string and n is a positive integer.
    if not isinstance(file_path, str) or not isinstance(n, int) or n <= 0:
        raise ValueError("file_path must be a string and n must be a positive integer.")
    
    # Initialize a dictionary to store the frequency distribution of n-grams.
    frequency_distribution = {}

    # Open the file and iterate over each line.
    with open(file_path, "r") as file:
        for line in file:
            # Iterate over each n-gram in the line, adding it to the dictionary or
            # incrementing its count if it already exists.
            for i in range(len(line) - n + 1):
                n_gram = line[i:i+n]
                if n_gram in frequency_distribution:
                    frequency_distribution[n_gram] += 1
                else:
                    frequency_distribution[n_gram] = 1

    # Return the frequency distribution dictionary.
    return frequency_distribution

def compute_text_entropy(text: str) -> float:
    """
    Computes and returns the Shannon entropy of a string of text. This is useful for
    determining whether a string of text is encrypted or not.

    Args:
        text (str): The text to compute the entropy of.

    Returns:
        float: The Shannon entropy of the text.

    Raises:
        ValueError: If text is not a string.

    """

    #Check that text is a string.
    if not isinstance(text, str):
        raise ValueError("text must be a string.")
    
    # Get the frequency distribution of characters in the text.
    frequency_distribution = get_ngram_frequency(text, 1)

    # Compute the entropy of the text.
    entropy = 0
    for frequency in frequency_distribution.values():
        probability = frequency / len(text)
        entropy -= probability * math.log2(probability)

    # Return the entropy of the text.
    return entropy

def compute_text_entropy_from_file(file_path: str) -> float:
    """
    Computes and returns the Shannon entropy of a file. This is useful for
    determining whether a file is encrypted or not.

    Args:
        file_path (str): The path to the file to compute the entropy of.

    Returns:
        float: The Shannon entropy of the file.

    Raises:
        ValueError: If file_path is not a string.

    """

    #Check that file_path is a string.
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string.")
    
    # Get the frequency distribution of characters in the file.
    frequency_distribution = get_ngram_frequency_from_file(file_path, 1)

    # Compute the entropy of the file.
    entropy = 0
    for frequency in frequency_distribution.values():
        probability = frequency / sum(frequency_distribution.values())
        entropy -= probability * math.log2(probability)

    # Return the entropy of the file.
    return entropy

def generate_ngram_frequencies(file_path: str) -> None:
    """
    Generates a file containing the frequency distribution of n-grams from a file of text.
    """


def load_ngram_frequencies(file_path: str) -> dict:
    """
    Loads a dictionary containing the relative frequency distribution of n-grams from a file. The file consists of
    four sections sepearated by a line containing only the character "#". The first section contains the
    frequency distribution of unigrams, the second section contains the frequency distribution of bigrams,
    the third section contains the frequency distribution of trigrams, and the fourth section contains the
    frequency distribution of quadgrams. The format of each section is as follows:
        n-gram, relative_frequency
        n-gram, relative_frequency
        ...
    Only the 20 most common n-grams are included in the file for n-grams of length greater than one.
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

def fermat_attack(n: int) -> tuple:
    """
    Attempts to factor a positive integer n using Fermat's factorization method. This method
    is particularly useful for factoring large integers that are the product of two primes
    that are close together. This serves as a wrapper for the fermat_factorization function.
    
    """
    # Check that n is a positive integer.
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")
    
    # Set the maximum number of iterations.
    max_iterations = 1000000

    # Run the fermat_factorization function until it returns a tuple of two factors or the
    # maximum number of iterations is reached.
    return fermat_factorization(n)
