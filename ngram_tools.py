
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