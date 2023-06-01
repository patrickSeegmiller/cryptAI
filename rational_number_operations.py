
def cf_expansion(num, denom):
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
    list
        
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

def get_cf_convergents(cf):
    """
    TODO: Docstring
    """
    h = [cf[0], cf[0]*cf[1]+1]
    k = [1, cf[1]]
    
    for i in range(2, len(cf)):
        h.append(cf[i] * h[i-1] + h[i-2])
        k.append(cf[i] * k[i-1] + k[i-2])

    return list(zip(h,k))