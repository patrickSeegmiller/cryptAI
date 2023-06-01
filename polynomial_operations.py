
def horners_method_of_polynomial_evaluation(polynomial_coefficients, input_value):
    """
    TODO: Docstring
    """
    
    remainder = 0
    for coefficient in polynomial_coefficients:
        remainder = coefficient + remainder * input_value

    return remainder

def synthetic_division(polynomial_coefficients, constant_term):
    """
    TODO: Docstring
    """
    
    remainder = 0
    resultant_coefficients = []
    for coefficient in polynomial_coefficients:
        remainder = coefficient + remainder * constant_term
        resultant_coefficients.append(remainder)

    return resultant_coefficients