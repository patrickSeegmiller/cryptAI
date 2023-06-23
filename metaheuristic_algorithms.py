
import math
import random

from ngram_tools import get_ngram_frequency, get_ngram_frequency_from_file, load_ngram_frequencies
from cryptanalytic_metrics import compute_text_entropy

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

        # Initialize the current key to a random dictionary, mapping symbols in the ciphertext to English alphabet characters.
        self.current_key = {}
        ciphertext_symbols = set(self.text)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for symbol in ciphertext_symbols:
            self.current_key[symbol] = random.choice(alphabet)

        # Initialize the current score.
        self.current_score = self.compute_score()

    def compute_score(self):
        """
        Computes the score of the current key by the sum of the squared differences between the expected and actual n-gram 
        relative frequencies.

        """

        # Compute the actual n-gram frequencies.
        actual_ngram_frequencies = {}
        for i in self.n:
            actual_ngram_frequencies[i] = get_ngram_frequency(self.text, i)

        # Compute the score.
        score = 0
        for i in self.n:
            for ngram in self.expected_ngram_frequencies[i]:
                score += (self.expected_ngram_frequencies[i][ngram] - actual_ngram_frequencies[i][ngram])**2

        return score

    

    

