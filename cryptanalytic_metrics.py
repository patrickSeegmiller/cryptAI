from ngram_tools import get_ngram_frequency, get_ngram_frequency_from_file

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

def language_score(text: str, language: str = 'english') -> float:
    """
    Computes a language score for a piece of text based on the frequency of the letters, bigrams, trigrams, and 
    quadgrams in the text, as well as the word patterns in the text for the specified language. Uses the 
    letter_frequency_score, bigram_frequency_score, trigram_frequency_score, quadgram_frequency_score, 
    and word_pattern_score functions.

    TODO: Add support for other languages.

    TODO: Add support for other metrics (e.g. word length, word frequency, etc.)

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

def word_pattern_frequency_score(text: str, language: str = 'english') -> float:
    """
    Computes and returns the word pattern frequency score, which equals the sum over the mean squared differences between
    the word pattern relative frequencies present as observed in text and the expected relative frequencies for the indicated
    language.

    Args:
        text (str): The text to compute word pattern frequency score.
    """

def compute_text_entropy(text: str, type: str) -> float:
    """
    Computes and returns the entropy of a string of text. The possible entropy types include 
    'collision', 'hartley', 'shannon', and 'min'.

    Args:
        text (str): The text to compute the entropy of.
        type (str): The type of entropy to compute. This can be "shannon", "collision", or "min".

    Returns:
        float: The entropy of the text of the specified type.

    Raises:
        ValueError: If text is not a string.

    References:
        https://en.wikipedia.org/wiki/R%C3%A9nyi_entropy
    """

    # TODO: Currently only computes Shannon entropy. Add support for other types of text entropy.

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
