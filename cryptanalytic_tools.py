import math

from whole_number_operations import integer_sqrt
from prime_number_sieves import sieve_of_eratosthenes
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

    # Import the regular expressions module.
    import re

    # Check that text is a string and n is a positive integer.
    if not isinstance(text, str) or not isinstance(n, int) or n <= 0:
        raise ValueError("text must be a string and n must be a positive integer.")
    
    # Initialize a dictionary to store the frequency distribution of n-grams.
    frequency_distribution = {}

    # Convert the text to lowercase.
    text = text.lower()

    # Remove all non-alphabetic characters from the text.
    text = re.sub(r"[^a-z]", "", text)

    # Iterate over each n-gram in the text, adding it to the dictionary or
    # incrementing its count if it already exists.
    for i in range(len(text) - n + 1):
        n_gram = text[i:i+n]
        if n_gram in frequency_distribution:
            frequency_distribution[n_gram] += 1
        else:
            frequency_distribution[n_gram] = 1

    # Convert frequecies to relative frequencies.
    for n_gram in frequency_distribution:
        frequency_distribution[n_gram] /= len(text)
        
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
    import re

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

            # Convert the line to lowercase.
            line = line.lower()

            # Remove all non-alphabetic characters from the line.
            line = re.sub(r"[^a-z]", "", line)

            # Split the line into words
            line = line.split()

            # Iterate over each word in the line.
            for word in line:
                # Iterate over each n-gram in the word.
                for i in range(len(word) - n + 1):
                    n_gram = word[i:i+n]
                    if n_gram in frequency_distribution:
                        frequency_distribution[n_gram] += 1
                    else:
                        frequency_distribution[n_gram] = 1

    # Convert frequencies to relative frequencies.
    total = sum(frequency_distribution.values())
    for n_gram in frequency_distribution:
        frequency_distribution[n_gram] /= total

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

def is_language_word_pattern(text_word_patterns: str, threshold: float = 0.9, language: str = "english") -> bool:
    """
    Determines whether a text is in language or not by exploring the word patterns of the text and comparing them
    to the word patterns of language words. The text is considered to be in the language if the proportion of word patterns
    that are found in the language dictionary is greater than or equal to the threshold.

    Args:
        text_word_patterns (str): File path to a file containing the word patterns of the text to analyze.
        threshold (float): The proportion of word patterns that must be found in the language dictionary for the text to be
            considered language. Defaults to 0.9.
        language (str): The language to compare the text to. Defaults to "english".
    
    Returns:
        bool: True if the text is written in language, False otherwise.
    
    Raises:
        ValueError: If text is not a non-empty string.
        ValueError: If the threshold is not a float between 0 and 1.
    
    """
    # Check that text is a non-empty string.
    if not isinstance(text_word_patterns, str) or len(text_word_patterns) == 0:
        raise ValueError("text must be a non-empty string.")
    # Check that threshold is a float between 0 and 1.
    if not isinstance(threshold, float) or threshold < 0 or threshold > 1:
        raise ValueError("threshold must be a float between 0 and 1.")
    
    # Load the dictionary of English word patterns.
    english_word_patterns = load_word_patterns()

    # Initialize a counter to count the number of word patterns that are found in the English dictionary.
    num_english_word_patterns = 0

    # Open the file containing the word patterns of the text to analyze and iterate over each line.
    with open(text_word_patterns, "r") as file:
        for line in file:
            # If the word pattern is found in the English dictionary, increment the counter.
            if line in english_word_patterns:
                num_english_word_patterns += 1

    # Return True if the proportion of word patterns that are found in the English dictionary is greater than or equal to the threshold.
    return num_english_word_patterns / len(text_word_patterns) >= threshold

def load_word_patterns(language: str = "english") -> dict:
    """
    Loads the dictionary of word patterns for the specified language from a JSON file.

    Raises:
        FileNotFoundError: If the word patterns file is not found.

    """

    # Import json.
    import json

    # Initialize a dictionary to store the word patterns.
    word_patterns = {}

    try:
        # Open the JSON file containing the word patterns.
        with open(f"word_patterns/{language}.json", "r") as file:
            # Load the word patterns into the dictionary.
            word_patterns = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Word patterns file for {language} not found.")
    
    # Return the dictionary of word patterns.
    return word_patterns

def generate_word_patterns(text_file_path: str, json: bool="True") -> None:
    """
    Generates dictionares of English word patterns and their counts for use to generate a master file of word
    patterns, as well as with the is_english function. 
    
    The patterns are strings of digits where each unique digit represents a distinct letter in the alphabet. For example, 
    the word pattern "0120" represents any four letter word where the first and last letters are the same, 
    and the middle two letters are both different from the first and last letters, like "that" or "barb". In like manner, 
    the pattern "010" represents any three letter word where the first and last letters are the same, like "bob" or "dad".

    The patterns are stored in a dictionary with the pattern as the key and the number of words in the English dictionary
    with that pattern as the value. For example, the pattern "0" has a value of 2, since there are two words in the English
    dictionary with that pattern, "a" and "I".

    Args:
        text_file_path (str): The path to the text file to be used to generate the word patterns.
        json (bool): Whether to save the word patterns as a JSON file. Defaults to True.

    Raises:
        ValueError: If text_file_path is not a non-empty string.
        ValueError: If word_pattern_file_path is not a non-empty string.
    """

    # Check that text_file_path is a non-empty string.
    if not isinstance(text_file_path, str) or text_file_path == "":
        raise ValueError("text_file_path must be a non-empty string.")
    
    # Initialize a dictionary to store the word patterns.
    word_patterns = {}

    # Initialize a dictionary to store the words with each pattern.
    pattern_words = {}

    # Open the text file and iterate over each line.
    with open(text_file_path, "r") as file:
        for line in file:
            # Strip the newline character from the line.
            line = line.strip()
            # Skip the line if it is empty.
            if line == "":
                continue
            # Split the line into a list of words.
            words = line.split(" ")
            # Iterate over each word in the list.
            for word in words:
                # Get the pattern of the word
                pattern = get_word_pattern(word)
                # Add the pattern to the word_patterns dictionary and the word to the pattern_words.
                if pattern in word_patterns:
                    word_patterns[pattern] += 1
                    pattern_words[pattern].append(word)
                else:
                    word_patterns[pattern] = 1

    # If json is True, write the word patterns to a JSON file.
    if json:
        # Import json.
        import json

        # Create a file path for the JSON file.
        json_file_path = text_file_path.replace(".txt", "_word_patterns.json")

        # Open the JSON file and write the word patterns to it.
        with open(json_file_path, "w") as file:
            json.dump(word_patterns, file)

        # Return from the function.
        return
    
    # Creates a word pattern file path based on the text file path.
    word_pattern_file_path = text_file_path.replace(".txt", "_word_patterns.txt")

    # Write word patterns, the words they represent, and the number of words they represent to the word pattern file.
    with open(word_pattern_file_path, "w") as file:
        for pattern in word_patterns:
            file.write(f"{pattern}, {word_patterns[pattern]}, {pattern_words[pattern]}\n")

    return
    
def get_word_pattern(word: str) -> str:
    """
    Produces the word pattern for a single word. The pattern is a string of digits where each unique digit represents a distinct
    letter in the alphabet. For example, the word pattern "0120" represents any four letter word where the first and last letters
    are the same, and the middle two letters are both different from the first and last letters, like "that" or "barb". In like
    manner, the pattern "010" represents any three letter word where the first and last letters are the same, like "bob" or "dad".

    Args:
        word (str): The word to produce the word pattern for.

    Raises:
        ValueError: If word is not a non-empty string.
    """

    # Import the regular expressions module.
    import re

    # Check that word is a non-empty string.
    if not isinstance(word, str) or word == "":
        raise ValueError("word must be a non-empty string.")
    
    # Convert the word to lowercase.
    word = word.lower()

    # Remove non-alphabetic characters from the word.
    word = re.sub(r"[^a-z]", "", word)

    # Iterate over each letter in the word and replace it with a unique digit.
    for letter in word:
        # Replace the letter with a unique digit.
        word = word.replace(letter, str(word.index(letter)))

    # Return the word pattern.
    return word

def english_score(text: str) -> float:
    """
    Computes a score for a piece of text based on the frequency of the letters, bigrams, trigrams, and quadgrams in the text, as
    well as the english word patterns in the text. Wraps the letter_frequency_score, bigram_frequency_score, trigram_frequency_score,
    quadgram_frequency_score, and word_pattern_score functions.

    Args:
        text (str): The text to compute the english score for.

    Raises:
        ValueError: If text is not a non-empty string.

    """
    
    # Check that text is a non-empty string.
    if not isinstance(text, str) or text == "":
        raise ValueError("text must be a non-empty string.")
    
    # Compute the letter frequency score.
    letter_frequency_score = letter_frequency_score(text)
    # Compute the bigram frequency score.
    bigram_frequency_score = bigram_frequency_score(text)
    # Compute the trigram frequency score.
    trigram_frequency_score = trigram_frequency_score(text)
    # Compute the quadgram frequency score.
    quadgram_frequency_score = quadgram_frequency_score(text)
    # Compute the word pattern score.
    word_pattern_score = word_pattern_score(text)

    # Compute the english score.
    english_score = letter_frequency_score + bigram_frequency_score + trigram_frequency_score + quadgram_frequency_score + word_pattern_score

    # Return the english score.
    return english_score

def letter_frequency_score(text: str, language: str = 'english') -> float:
    """
    Computes the mean of sum of squared errors between the letter frequencies in the text and the expected letter frequencies
    for the indicated language.

    Args:
        text (str): The text to compute the letter frequency score for.
        language (str): The language to compute the letter frequency score for. Defaults to 'english'.

    Raises:
        ValueError: If text is not a non-empty string.
        ValueError: If language is not a non-empty string.
    
    Returns:
        float: The letter frequency score for the text.
    
    """

    # Import the numpy module.
    import numpy as np

    # Check that text is a non-empty string.
    if not isinstance(text, str) or text == "":
        raise ValueError("text must be a non-empty string.")
    # Check that language is a non-empty string.
    if not isinstance(language, str) or language == "":
        raise ValueError("language must be a non-empty string.")
    
    # Imnitialize a 1-d numpy array to store the letter frequencies in the text.
    text_letter_frequencies = np.zeros(26)
    # Load the expected letter frequencies for the language.
    language_letter_frequencies = np.loadtxt(f"text_tools/letter_frequencies/{language}_letter_frequencies.txt", delimiter=",")

    # Convert the text to lowercase.
    text = text.lower()

    # Iterate over each letter in the language alphabet.
    for letter in language_letter_frequencies[0]:
        # Compute the letter frequency in the text.
        letter_frequency = text.count(letter) / len(text)
        # Add the letter frequency to the text_letter_frequencies array.
        text_letter_frequencies[ord(letter) - 97] = letter_frequency

    # Compute and return the mean of sum of squared errors between the letter frequencies in the text and the expected letter frequencies
    # for the language.
    return np.mean((text_letter_frequencies - language_letter_frequencies[1]) ** 2)

def bigram_frequency_score(text: str, language: str = 'english') -> float:
    """
    Computes the mean of the sum of squared errors for the bigram frequencies in the text and the expected bigram frequencies
    for the indicated language.

    Args:
        text (str): The text to compute the bigram frequency score for.
        language (str): The language to compute the bigram frequency score for. Defaults to 'english'.

    Raises:
        ValueError: If text is not a non-empty string.
        ValueError: If language is not a non-empty string.

    Returns:   
        float: The bigram frequency score for the text.
    
    """

    # import the numpy module.
    import numpy as np

    # Check that text is a non-empty string.
    if not isinstance(text, str) or text == "":
        raise ValueError("text must be a non-empty string.")
    # Check that language is a non-empty string.
    if not isinstance(language, str) or language == "":
        raise ValueError("language must be a non-empty string.")
    
    # Initialize a 2-d numpy array to store the bigram frequencies in the text.
    text_bigram_frequencies = np.zeros((26, 26))

    # Load the expected bigram frequencies for the language.
    language_bigram_frequencies = np.loadtxt(f"text_tools/bigram_frequencies/{language}_bigram_frequencies.txt", delimiter=",")

    # Convert the text to lowercase.
    text = text.lower()

    # Iterate over each bigram in the language alphabet.    
    for bigram in language_bigram_frequencies[0]:
        # Compute the bigram frequency in the text.
        bigram_frequency = text.count(bigram) / len(text)
        # Add the bigram frequency to the text_bigram_frequencies array.
        text_bigram_frequencies[ord(bigram[0]) - 97][ord(bigram[1]) - 97] = bigram_frequency

    # Compute and return the mean of sum of squared errors between the bigram frequencies in the text and the expected bigram frequencies
    # for the language.
    return np.mean((text_bigram_frequencies - language_bigram_frequencies[1]) ** 2)

def trigram_frequency_score(text: str, language: str = 'english') -> float:
    """
    Computes the mean of the sum of squared errors for the trigram frequencies in the text and the expected trigram frequencies
    for the indicated language.

    Args:
        text (str): The text to compute the trigram frequency score for.
        language (str): The language to compute the trigram frequency score for. Defaults to 'english'.

    Raises:
        ValueError: If text is not a non-empty string.
        ValueError: If language is not a non-empty string.

    Returns:
        float: The trigram frequency score for the text.

    """

    # import the numpy module.
    import numpy as np

    # Check that text is a non-empty string.
    if not isinstance(text, str) or text == "":
        raise ValueError("text must be a non-empty string.")
    # Check that language is a non-empty string.
    if not isinstance(language, str) or language == "":
        raise ValueError("language must be a non-empty string.")
    
    # Initialize a 3-d numpy array to store the trigram frequencies in the text.
    text_trigram_frequencies = np.zeros((26, 26, 26))

    # Load the expected trigram frequencies for the language.
    language_trigram_frequencies = np.loadtxt(f"text_tools/trigram_frequencies/{language}_trigram_frequencies.txt", delimiter=",")

    # Convert the text to lowercase.
    text = text.lower()

    # Iterate over each trigram in the language alphabet.
    for trigram in language_trigram_frequencies[0]:
        # Compute the trigram frequency in the text.
        trigram_frequency = text.count(trigram) / len(text)
        # Add the trigram frequency to the text_trigram_frequencies array.
        text_trigram_frequencies[ord(trigram[0]) - 97][ord(trigram[1]) - 97][ord(trigram[2]) - 97] = trigram_frequency

    # Compute and return the mean of sum of squared errors between the trigram frequencies in the text and the expected trigram frequencies
    # for the language.
    return np.mean((text_trigram_frequencies - language_trigram_frequencies[1]) ** 2)

def quadgram_frequency_score(text: str, language: str = 'english') -> float:
    """
    Computes the mean of the sum of squared errors for the quadgram frequencies in the text and the expected quadgram frequencies
    for the indicated language.
    
    Args:
        text (str): The text to compute the quadgram frequency score for.
        language (str): The language to compute the quadgram frequency score for. Defaults to 'english'.
        
    Raises:
        ValueError: If text is not a non-empty string.
        ValueError: If language is not a non-empty string.
        
    Returns:
        float: The quadgram frequency score for the text.
    
    """

    # Import the numpy module.
    import numpy as np

    # Check that text is a non-empty string.
    if not isinstance(text, str) or text == "":
        raise ValueError("text must be a non-empty string.")
    # Check that language is a non-empty string.
    if not isinstance(language, str) or language == "":
        raise ValueError("language must be a non-empty string.")
    
    # Initialize a 4-d numpy array to store the quadgram frequencies in the text.
    text_quadgram_frequencies = np.zeros((26, 26, 26, 26))

    # Load the expected quadgram frequencies for the language.
    language_quadgram_frequencies = np.loadtxt(f"text_tools/quadgram_frequencies/{language}_quadgram_frequencies.txt", delimiter=",")

    # Convert the text to lowercase.
    text = text.lower()

    # Iterate over each quadgram in the language alphabet.
    for quadgram in language_quadgram_frequencies[0]:
        # Compute the quadgram frequency in the text.
        quadgram_frequency = text.count(quadgram) / len(text)
        # Add the quadgram frequency to the text_quadgram_frequencies array.
        text_quadgram_frequencies[ord(quadgram[0]) - 97][ord(quadgram[1]) - 97][ord(quadgram[2]) - 97][ord(quadgram[3]) - 97] = quadgram_frequency

    # Compute and return the mean of sum of squared errors between the quadgram frequencies in the text and the expected quadgram frequencies
    # for the language.
    return np.mean((text_quadgram_frequencies - language_quadgram_frequencies[1]) ** 2)

def ciphertext_partition_word_pattern_score(ciphertext_partition: list[str]) -> float:
    """
    Computes a word pattern score for a given partition of the ciphertext. The score is computed by computing total number
    of word patterns in the partition that are in the word patterns dictionary, and dividing by the total number of substrings
    in the partition.

    Args:
        ciphertext_partition (list[str]): The partition of the ciphertext to compute the word pattern score for.

    Raises:
        ValueError: If ciphertext_partition is not a non-empty list of non-empty strings.
    
    """

    # Check that ciphertext_partition is a non-empty list of non-empty strings.
    if not isinstance(ciphertext_partition, list) or ciphertext_partition == []:
        raise ValueError("ciphertext_partition must be a non-empty list.")
    for substring in ciphertext_partition:
        if not isinstance(substring, str) or substring == "":
            raise ValueError("ciphertext_partition must be a non-empty list of non-empty strings.")

    # Initialize a variable to store the score.
    score = 0

    # Load the word patterns dictionary.
    word_patterns = load_word_patterns()

    # Iterate over each substring in the partition.
    for substring in ciphertext_partition:
        # Get the word pattern of the substring.
        pattern = get_word_pattern(substring)
        # Check if the pattern is in the word patterns dictionary.
        if pattern in word_patterns:
            # Add the number of words in the English dictionary with that pattern to the score.
            score += word_patterns[pattern]
    
    # Return the score.
    return score / len(ciphertext_partition)

def generate_ciphertext_word_pattern_tree(ciphertext: str) -> list[dict]:
    """
    Constructs a tree of word patterns for the ciphertext. Each node in the tree is a dictionary with the following keys:

    "pattern": The word pattern of the node.
    "children": A list of dictionaries representing the children of the node.

    Begins by randomly partitioning the ciphertext into large, likely substrings from the word pattern dictionary. 
    Then, for each substring, recursively randomly partition it into smaller substrings until the substrings in the 
    tree are all in the word pattern dictionary.

    Args:
        ciphertext (str): The ciphertext to construct the word pattern tree for.

    Raises:
        ValueError: If ciphertext is not a non-empty string.

    TODO: Come up with a way to adapt this to polyalphabetic and polygraphic ciphers.
    
    """

    # Check that ciphertext is a non-empty string.
    if not isinstance(ciphertext, str) or ciphertext == "":
        raise ValueError("ciphertext must be a non-empty string.")
    
    # Import the random module.
    import random

    # Load the word patterns dictionary.
    word_patterns = load_word_patterns()

    # Initialize a list to store the tree.
    tree = []

    # Perform a random partition of the ciphertext into large, likely substrings from the word pattern dictionary.
    ciphertext_partition = random_partition(ciphertext, word_patterns)

    # Iterate over each substring in the partition.
    for substring in ciphertext_partition:
        # Randomly partition the substring into smaller substrings until the substrings are all in the word pattern dictionary.
        substring_partition = random_partition(substring, word_patterns)
        # Initialize a list to store the children of the substring.
        children = []

def random_text_partition(text: str, language: str = "english") -> list[str]:
    """
    Randomly partitions a text into a sequence of substrings that all have word patterns in the word patterns dictionary. 
    As the word patterns assume a one-to-one correspondence between ciphertext letters and plaintext letters, substrings
    should be contiguous.

    Args:
        text (str): The text to partition.
        language (str): The language to use to partition the text. Defaults to 'english'.

    Raises:
        ValueError: If text is not a non-empty string.
        ValueError: If language is not a non-empty string.

    Returns:
        list[str]: A list of sequential substrings that all have word patterns in the word patterns dictionary.
    
    """

    # Check that text is a non-empty string.
    if not isinstance(text, str) or text == "":
        raise ValueError("text must be a non-empty string.")
    # Check that language is a non-empty string.
    if not isinstance(language, str) or language == "":
        raise ValueError("language must be a non-empty string.")
    
    # Import the random module.
    import random

def word_pattern_count(text_file: str, language: str = "english") -> dict[str, int]:
    """
    Counts the number of times each word pattern in the word patterns dictionary appears in the text file.

    Args:
        text_file (str): The text file to count the word patterns in.
        language (str): The language to use to count the word patterns. Defaults to 'english'.

    Raises:
        ValueError: If text_file is not a non-empty string.
        ValueError: If language is not a non-empty string.

    Returns:
        dict[str, int]: A dictionary mapping each word pattern in the word patterns dictionary to the number of 
        times it appears in the text file.
    
    """

def word_pattern_relative_frequencies(file_path: str, language: str = "english") -> dict[str, int]:
    """
    Computes the relative frequency of each a word pattern dictionary's word patterns in each text in file_path. 
    Used in conjunctino with word_pattern_count to generate expected word pattern relative frequencies for a language.

    Args:
        file_path (str): The path to the directory containing the texts to compute the word pattern relative frequencies for.
        language (str): The language to use to compute the word pattern frequencies. Defaults to 'english'.

    Raises:
        ValueError: If text_file is not a non-empty string.
        ValueError: If language is not a non-empty string.
    
    Returns:
        dict[str, int]: A dictionary mapping each word pattern in the word patterns dictionary to the relative frequency
        of that word pattern in the texts in file_path.
    
    """

    # Check that file_path is a non-empty string.
    if not isinstance(file_path, str) or file_path == "":
        raise ValueError("file_path must be a non-empty string.")
    
    # Check that language is a non-empty string.
    if not isinstance(language, str) or language == "":
        raise ValueError("language must be a non-empty string.")
    
    # Import the os module.
    import os

    # Iterate over each text file in file_path, counting how many times each word

    




    







