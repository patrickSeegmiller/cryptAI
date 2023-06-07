
def horners_polynomial_evaluation(polynomial_coefficients: list[float or int], input_value: (float or int)) -> float:
    """
    Evaluates a polynomial using Horner's method given its coefficients and an input value.

    Args:
        polynomial_coefficients (list[float]): The coefficients of the polynomial in descending order of degree.
        input_value (float): The value at which the polynomial is evaluated.

    Returns:
        float: The result of evaluating the polynomial at the given input value.

    Raises:
        ValueError: If the input parameters are not in the expected format.
    """

    # First, check that the input is valid by checking that polynomial_coefficients is a list of integers or floats
    # and that input_value is an integer or float.
    if not isinstance(polynomial_coefficients, list) or not all(isinstance(coeff, (int, float)) for coeff in polynomial_coefficients):
        raise ValueError("Polynomial coefficients must be a list of integers or floats.")
    if not isinstance(input_value, (int, float)):
        raise ValueError("Input value must be an integer or float.")
    
    # Evaluate the polynomial using Horner's method
    for coefficient in polynomial_coefficients:
        result = result * input_value + coefficient

    # Return the result
    return result

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
    if not isinstance(constant_term, int):
        raise ValueError("Constant term must be an integer or float.")
    
    # Perform synthetic division
    remainder = 0
    resultant_coefficients = []
    for coefficient in polynomial_coefficients:
        resultant_coefficients.append(coefficient + remainder * constant_term)

    # Return the coefficients of the resulting polynomial
    return resultant_coefficients

def polynomial_long_division(dividend: list[float], divisor: list[float]) -> tuple[list[float], list[float]]:
    """
    Performs polynomial long division on a dividend and divisor given their coefficients.

    Args:
        dividend (list[float]): The coefficients of the dividend in descending order of degree.
        divisor (list[float]): The coefficients of the divisor in descending order of degree.

    Returns:
        tuple[list[float], list[float]]: A tuple containing the coefficients of the quotient and remainder of the
        polynomial long division, both in descending order of degree.

    Raises:
        ValueError: If the input parameters are not in the expected format.
    """

    # First, check that the input is valid by checking that dividend and divisor are lists of integers.
    if not isinstance(dividend, list) or not all(isinstance(coeff, int) for coeff in dividend):
        raise ValueError("Dividend coefficients must be a list of integers or floats.")
    if not isinstance(divisor, list) or not all(isinstance(coeff, int) for coeff in divisor):
        raise ValueError("Divisor coefficients must be a list of integers or floats.")
    
    # Perform polynomial long division
    quotient = []
    remainder = dividend
    while len(remainder) >= len(divisor):
        # Calculate the next term of the quotient
        quotient.append(remainder[0] / divisor[0])
        # Calculate the next remainder
        remainder = [remainder[i] - quotient[-1] * divisor[i] for i in range(len(divisor))] + remainder[len(divisor):]

    # Return the quotient and remainder
    return (quotient, remainder)

