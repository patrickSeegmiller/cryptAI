
import math
import random

from encryption_decryption.cryptanalytic_tools import compute_text_entropy, get_ngram_frequency, get_ngram_frequency_from_file

class NGramSimulatedAnnealing():
    def __init__(self, text: str, n=[1, 2, 3, 4]) -> None:
        """
        Initializes a simulated annealing algorithm for finding the key of a
        substitution cipher.

        Args:
            text (str): The text under examination.
            n (list): The n-grams to use in the algorithm. Defaults to [1, 2, 3, 4] (i.e. letters, bigrams, trigrams, and quadrigrams.)

        Raises:
            ValueError: If text is not a string or n is not a list of positive integers.
        """
        # Check that text is a string and n is a list of positive integers.
        if not isinstance(text, str) or not isinstance(n, list) or not all(isinstance(i, int) for i in n) or not all(i > 0 for i in n):
            raise ValueError("text must be a string and n must be a list of positive integers.")
        
        # Initialize the text and n-grams.
        self.text = text
        self.n = n

        # Initialize the expected n-gram frequencies.
        self.expected_ngram_frequencies = {}
        for i in n:
            self.expected_ngram_frequencies[i] = load_ngram_frequencies("machine_learning_tools/english_ngram_frequencies.txt", i)

    def compute_score(self):






    

