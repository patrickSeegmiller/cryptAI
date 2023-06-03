
def continued_fraction_expansion(num: int, denom: int) -> list[int]:
    """
    cf_expansion takes the numerator and denominator of a positive rational number as parameters and returns its
    continued fraction expansion as a list.

    Args:
        num (int): The numerator of the rational number to be converted to a continued fraction.
        denom (int): The denominator of the rational number to be converted to a continued fraction.

    Returns:
        list[int]: The continued fraction expansion of the rational number num/denom.

    """

    # We first check that num and denom are positive integers.
    if not isinstance(num, int) or not isinstance(denom, int) or num <= 0 or denom <= 0:
        raise ValueError("num and denom should be positive integers.")
    
    # Next, we initialize the integer part, remainder, and result list.
    integer_part = num // denom
    remainder = num % denom
    result = [integer_part]

    # We now compute the continued fraction expansion, appending each integer part to the result list.
    while remainder != 0:
        num, denom = denom, remainder
        integer_part = num // denom
        remainder = num % denom
        result.append(integer_part)

    # We return the continued fraction expansion.
    return result

def get_continued_fraction_convergents(continued_fraction: list[int]) -> list[tuple[int, int]]:
    """
    get_cf_convergents takes a continued fraction expansion as a list and returns a list of tuples containing the
    numerator and denominator of each convergent.

    Args:
        continued_fraction (list[int]): The continued fraction expansion of a rational number as a list.

    Returns:
        list[tuple[int, int]]: A list of tuples containing the numerator and denominator of each convergent of the
        continued fraction.
    
    Raises:
        TypeError: If continued_fraction is not a list of integers. 
        ValueError: If continued_fraction is empty.

    """

    # We first check that continued_fraction is a list of integers.
    if not isinstance(continued_fraction, list) or not all(isinstance(x, int) for x in continued_fraction):
        raise TypeError("continued_fraction should be a list of integers.")
    # We also check that continued_fraction is not empty.
    if len(continued_fraction) == 0:
        raise ValueError("continued_fraction should not be empty.")
    
    # We now initialize the lists h and k, which will contain the numerators and denominators of the convergents.
    h = [continued_fraction[0], continued_fraction[0]*continued_fraction[1]+1]
    k = [1, continued_fraction[1]]
    
    # Finally, we compute the numerators and denominators of the convergents.
    for i in range(2, len(continued_fraction)):
        h.append(continued_fraction[i] * h[i-1] + h[i-2])
        k.append(continued_fraction[i] * k[i-1] + k[i-2])

    # We return the list of tuples representing the convergents.
    return list(zip(h,k))