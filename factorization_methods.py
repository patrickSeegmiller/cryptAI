from whole_number_operations import fast_powering_algorithm, integer_sqrt, is_square

def fermat_factorization(n: int) -> list[int]:
    '''
        Performs Fermat's method for factoring an odd number `n`.
    
        Fermat's method relies on the fact that any odd number can be expressed 
        as a difference of squares. It checks numbers near the square root of `n` 
        for ways in which `n` can be written as a difference of perfect squares. 
        If `n = b^2 - a^2`, it factors as `n = (b-a)(b+a)`.

    Args:
        n (int): The number to be factored.

    Returns:
        list[int]: A list containing the two factors of `n`.

    Raises:
        ValueError: If `n` is not an odd number greater than 1.

    '''

    # We first check that n is an odd number greater than 1.
    if not isinstance(n, int) or n <= 1 or n % 2 == 0: 
        raise ValueError("n should be an odd number greater than 1.")
    
    # Next we check whether n is a perfect square.
    if is_square(n):
        return [integer_sqrt(n), integer_sqrt(n)]

    # Now we perform Fermat's method, starting with a = sqrt(n) + 1.
    # We check whether a^2 - n is a perfect square. If not, we increment a by 1 and repeat.
    try:
        a = integer_sqrt(n-1) + 1
        b_squared = a*a - n
        while not is_square(b_squared):
            a = a + 1
            b_squared = a*a - n
    except KeyboardInterrupt:
        print("Fermat's method was interrupted by the user.")
        return None

    # We return the factors of n.
    return [a - integer_sqrt(b_squared), a + integer_sqrt(b_squared)]
