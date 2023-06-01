from primality_tests import miller_rabin_get_prime
from whole_number_operations import integer_sqrt

def hex_string_to_base_ten_integer(hex_value):
    """
    This function takes a string representing a hexadecimal value (e.g., an RSA modulus)
    and returns the same value as a base-10 integer. 
    """

    # Check that the input is a string containing only hexadecimal digits
    if not isinstance(hex_value, str) or not all([char in '0123456789abcdefABCDEF \n' for char in hex_value]):
        raise ValueError("hex_value must be a string containing only hexadecimal digits.")
    
    # Return the base-10 integer value of the hexadecimal string
    return int(hex_value.replace(' ','').replace('\n',''), 16)

def generate_rsa_public_key(number_of_bits: int = 1024, public_exponent: int = 65537) -> list[int]:
    """
    Generates an RSA public key.

    Args:
        number_of_bits (int): The number of bits for the RSA modulus. Defaults to 1024.
        public_exponent (int): The public exponent value. Defaults to 65537.

    Returns:
        list[int]: A list containing the public exponent and the RSA modulus.

    Raises:
        ValueError: If `number_of_bits` is less than 2 or `public_exponent` is not a positive integer.
    """
   
    # Input validation
    if not isinstance(number_of_bits, int) or number_of_bits < 2:
        raise ValueError("number_of_bits must be a positive integer greater than 1.")
    if not isinstance(public_exponent, int) or public_exponent < 1:
        raise ValueError("public_exponent must be a positive integer.")

    # Generate the RSA modulus by multiplying two primes generated using the Miller-Rabin primality test
    p = miller_rabin_get_prime(2 ** (number_of_bits - 1), 2 ** (number_of_bits))
    q = miller_rabin_get_prime(2 ** (number_of_bits - 1), 2 ** (number_of_bits))
    while q == p:
        q = miller_rabin_get_prime(2 ** (number_of_bits - 1), 2 ** (number_of_bits))

    N = p * q
    return [public_exponent, N]

def generate_bad_rsa_public_key(bad_primes=False, weak_decryption_key=False, really_bad_modulus=False, number_of_bits=1024):
    """
    TODO: Docstring
    """

    if weak_decryption_key:
        p = miller_rabin_get_prime(2 ** (number_of_bits - 1), 2 ** (number_of_bits))
        q = p
        while q == p:
            q = miller_rabin_get_prime(2 ** (number_of_bits - 1), 2 ** (number_of_bits))
            
        d = miller_rabin_get_prime(2, integer_sqrt(integer_sqrt(p*q)) // 4 - 1)
        e = find_modular_inverse(d, (p-1)*(q-1))
    else:
        e = 65537

    if really_bad_modulus:
        p = random.randint(2, 2**(number_of_bits))
        q = random.randint(2, 2**(number_of_bits))
        return [e, p*q]
    
    if bad_primes:
        p = miller_rabin_get_prime(2 ** (number_of_bits - 1), 2 ** (number_of_bits))
        q = miller_rabin_get_prime(p, p + 1000000000)
            
    return [e, p * q]