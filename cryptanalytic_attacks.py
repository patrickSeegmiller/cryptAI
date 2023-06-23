from whole_number_tools import integer_sqrt
from prime_number_sieves import sieve_of_eratosthenes
from ngram_tools import get_ngram_frequency_from_file, get_ngram_frequency
from factorization_methods import fermat_factorization, trial_division_factorization, pollard_rho_factorization, pollard_p_1_factorization, williams_p_1_factorization#, quadratic_sieve_factorization, shanks_square_forms_factorization, rational_sieve, general_number_field_sieve

def factorization_attack(n: int, algo='trial_division') -> tuple:
    """
    Attempts to factor a positive integer n by brute force using the selected factorization algorithm. 
    
    Args:
        n (int): The number to factor.
        algo (str): The factorization algorithm to use. Options are 'continued_fraction', 'fermat', 
             'general_number_field_sieve', 'pollard_p_1', 'pollard_rho', 'quadratic_sieve', 'rational_sieve', 
             or the default of 'trial_division'.

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

def evaluate_public_key(public_modulus: int, public_exponent: int, algorithms: list[str] = ['trial_division']) -> dict:
    """
    Evaluates the strength of a public key by applying a series of cryptanalytic attacks to the public modulus and/or
    public exponent.

    Args:
        public_modulus (int): The public modulus.
        public_exponent (int): The public exponent.
        algorithms (list[str]): A list of factorization algorithms to use. Options are 'continued_fraction', 'fermat', 
             'general_number_field_sieve', 'pollard_p_1', 'pollard_rho', 'quadratic_sieve', 'rational_sieve', 
            or the default of 'trial_division'.

    Returns:
        dict: A dictionary containing the results of the cryptanalytic attacks.
    
    Raises:
        ValueError: If public_modulus is not a positive integer or public_exponent is not a positive integer.
    
    """
    # Check that public_modulus and public_exponent are positive integers.
    if not isinstance(public_modulus, int) or public_modulus <= 0:
        raise ValueError("public_modulus must be a positive integer.")
    if not isinstance(public_exponent, int) or public_exponent <= 0:
        raise ValueError("public_exponent must be a positive integer.")
    
    # Initialize a dictionary to store the results of the cryptanalytic attacks.
    results = {}
    
    # Factor the public modulus using the specified factorization algorithms.
    for algorithm in algorithms:
        try:
            results[algorithm] = factorization_attack(public_modulus, algorithm)
        except Exception as e:
            results[algorithm] = e

    return results





    







