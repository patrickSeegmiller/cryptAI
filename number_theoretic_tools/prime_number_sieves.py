import math
import sys

def sieve_of_eratosthenes(N: int) -> list[int]:
    """
    Generates a list of prime numbers up less than N using the Sieve of 
    Eratosthenes algorithm.

    Args:
        N (int): The limit up to which prime numbers should be generated.

    Returns:
        list: A list of prime numbers up to N.
    """
    
    # Initialize a list of booleans to represent whether each number is prime.
    is_prime = [True] * N

    # Iterate over the list of booleans, setting each composite number to False
    # (i.e. if is_prime[i] == True, then i is prime and all multiples of i and any of its
    # powers are composite).
    for i in range(2, math.ceil(math.sqrt(N))):
        if is_prime[i] == True:
            for j in [i*i + i*k for k in range(math.ceil((N-i*i)/i))]:
                is_prime[j] = False

    # Return a list of all prime numbers up to N, making sure to exclude 0 and 1
    # which were set to True by default.
    return [index for index, prime in enumerate(is_prime) if prime and index > 1]

def sieve_of_sundaram(N: int) -> list[int]:
    '''Generates a list of prime numbers up less than N using the Sieve of
    Sundaram algorithm.
    
    Args:
        N (int): The limit up to which prime numbers should be generated.
        
    Returns:
        list: A list of prime numbers up to N.
    '''

    #Input validation
    if N < 2 or not isinstance(N, int):
        raise ValueError("N must be an integer greater than 1.")
    
    #TODO: Implement Sieve of Sundaram algorithm
    return []

if __name__ == '__main__':
    # Default input if no command-line argument is provided
    default_limit = 100

    # Usage information
    print("Sieve of Eratosthenes - Prime Number Generator")
    print("Usage: python sieve_of_eratosthenes.py <N>")
    print("       where <N> is the limit up to which prime numbers should be generated.")
    print(f"\nIf no argument is provided, the default limit of {default_limit} will be used.")

    # Check command-line arguments for a limit
    if len(sys.argv) == 2:
        # Parse the limit from the command-line argument
        try:
            N = int(sys.argv[1])
        except ValueError:
            print("Invalid argument. Please provide a valid integer as the limit.")
            sys.exit(1)
    elif len(sys.argv) > 2:
        print("Invalid number of arguments. Please provide a single integer as the limit.")
        sys.exit(1)
    else:
        # Use the default limit
        N = default_limit

    # Generate prime numbers based on the limit
    primes = sieve_of_eratosthenes(N)

    # Print the result to the console
    print(f"Prime numbers up to {N}:")
    print(primes)

    # Exit gracefully with exit code 0
    sys.exit(0)