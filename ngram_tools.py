
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
