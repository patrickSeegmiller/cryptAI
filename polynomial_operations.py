
def horner_polynomial_evaluation(polynomial_coefficients, input_value):
    """
    TODO: Docstring
    """
    
    remainder = 0
    for coefficient in polynomial_coefficients:
        remainder = coefficient + remainder * input_value

    return remainder

def synthetic_division(polynomial_coefficients: list[float], constant_term: float) -> list[float]:
    """
    Performs synthetic division on a polynomial given its coefficients and a constant term.

    Args:
        polynomial_coefficients (list[float]): The coefficients of the polynomial in descending order of degree.
        constant_term (float): The constant term used in synthetic division.

    Returns:
        list[float]: The coefficients of the resulting polynomial after synthetic division.

    Raises:
        ValueError: If the input parameters are not in the expected format.
    """

    # First, check that the input is valid by checking that polynomial_coefficients is a list of integers.
    if not isinstance(polynomial_coefficients, list) or not all(isinstance(coeff, int) for coeff in polynomial_coefficients):
        raise ValueError("Polynomial coefficients must be a list of integers or floats.")
    if not isinstance(constant_term, int)):
        raise ValueError("Constant term must be an integer or float.")
    
    # Perform synthetic division
    remainder = 0
    resultant_coefficients = []
    for coefficient in polynomial_coefficients:
        resultant_coefficients.append(coefficient + remainder * constant_term)

    # Return the coefficients of the resulting polynomial
    return resultant_coefficients