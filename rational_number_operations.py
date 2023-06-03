
def continued_fraction_expansion(num: int, denom: int) -> list[int]:
    """
    cf_expansion takes the numerator and denominator of a positive rational number as parameters and returns its
    continued fraction expansion as a list.

    Parameters
    ----------
    num : int
        num should be the numerator of the rational number to be converted to a continued fraction

    denom : int
        denom should be the denominator of the rational number to be converted to a continued fraction

    Returns
    -------
    list of ints  
        The continued fraction expansion of the rational number num/denom
    """

    i_part = num // denom
    r = num % denom
    
    result = [i_part]
    while r != 0:
        num, denom = denom, r
        i_part = num // denom
        r = num % denom
        result.append(i_part)

    return result

def get_continued_fraction_convergents(continued_fraction: list[int]) -> list[tuple[int, int]]:
    """
    get_cf_convergents takes a continued fraction expansion as a list and returns a list of tuples containing the
    numerator and denominator of each convergent.

    Parameters
    ----------
    continued_fraction : list of ints 
        continued_fraction should be a list containing the continued fraction expansion of a rational number

    Returns
    -------
    list of tuples
        Each tuple contains the numerator and denominator of a convergent of the continued fraction
    
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