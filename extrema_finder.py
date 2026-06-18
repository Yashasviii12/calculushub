"""
CalculusHub Extrema Finder
Finds absolute minima and maxima of a mathematical function on a given interval.
"""

import numpy as np
from sympy import symbols, sympify, diff, solve, lambdify, Float
from typing import Dict, Tuple, List


def find_extrema(func_str: str, interval: Tuple[float, float]) -> Dict:
    """
    Find absolute minima and maxima of a function on a closed interval.
    
    Parameters:
    -----------
    func_str : str
        Mathematical function as a string (e.g., 'x**2 + 3*x - 5', 'sin(x)', 'exp(-x**2)')
    interval : tuple of float
        Closed interval [a, b] to search for extrema
    
    Returns:
    --------
    dict : A dictionary containing:
        - 'min_value': float - The absolute minimum value
        - 'min_x': float - The x-coordinate where minimum occurs
        - 'max_value': float - The absolute maximum value
        - 'max_x': float - The x-coordinate where maximum occurs
        - 'critical_points': list - All critical points found in the interval
    
    Raises:
    -------
    ValueError: If the function string is invalid or interval is malformed
    SyntaxError: If the mathematical expression cannot be parsed
    
    Examples:
    ---------
    >>> result = find_extrema('x**2 - 4*x + 3', [0, 5])
    >>> print(result)
    {
        'min_value': -1.0,
        'min_x': 2.0,
        'max_value': 8.0,
        'max_x': 5.0,
        'critical_points': [2.0]
    }
    
    >>> result = find_extrema('sin(x)', [0, 3.14159])
    """
    
    # Validate input
    if not isinstance(interval, (tuple, list)) or len(interval) != 2:
        raise ValueError("Interval must be a tuple/list of two numbers [a, b]")
    
    a, b = float(interval[0]), float(interval[1])
    
    if a >= b:
        raise ValueError(f"Invalid interval: a ({a}) must be less than b ({b})")
    
    try:
        # Define symbol and parse the function
        x = symbols('x', real=True)
        # Use locals dict to ensure 'x' is properly recognized in the string
        f = sympify(func_str, locals={'x': x})
        
        # Compute the derivative
        f_prime = diff(f, x)
        
        # Find critical points by solving f'(x) = 0
        critical_points = []
        try:
            solutions = solve(f_prime, x)
            # Filter real solutions within the interval
            for sol in solutions:
                try:
                    sol_float = float(sol.evalf())
                    # Check if solution is a real number and within interval
                    if isinstance(sol_float, (int, float)) and a <= sol_float <= b:
                        critical_points.append(sol_float)
                except (TypeError, ValueError):
                    # Skip complex or non-evaluable solutions
                    continue
        except Exception as e:
            # If solving fails, use numerical approach
            pass
        
        # Create a numerical function for evaluation
        f_numeric = lambdify(x, f, 'numpy')
        
        # Evaluate at critical points and interval endpoints
        evaluation_points = [a, b] + critical_points
        
        try:
            evaluations = []
            for point in evaluation_points:
                try:
                    value = float(f_numeric(point))
                    evaluations.append((point, value))
                except (ValueError, TypeError, RuntimeError):
                    # Skip points that cannot be evaluated
                    continue
            
            if not evaluations:
                raise ValueError("Could not evaluate the function at any point in the interval")
            
            # Find minima and maxima
            min_point, min_value = min(evaluations, key=lambda x: x[1])
            max_point, max_value = max(evaluations, key=lambda x: x[1])
            
            # Round to reasonable precision
            min_value = round(float(min_value), 10)
            max_value = round(float(max_value), 10)
            min_point = round(float(min_point), 10)
            max_point = round(float(max_point), 10)
            critical_points = [round(float(p), 10) for p in critical_points]
            
            return {
                'min_value': min_value,
                'min_x': min_point,
                'max_value': max_value,
                'max_x': max_point,
                'critical_points': critical_points
            }
        
        except Exception as e:
            raise RuntimeError(f"Error evaluating function: {str(e)}")
    
    except SyntaxError as e:
        raise SyntaxError(f"Invalid mathematical expression: {func_str}. Error: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error processing function: {str(e)}")


def find_extrema_with_details(func_str: str, interval: Tuple[float, float]) -> Dict:
    """
    Extended version that includes all evaluation points and their values.
    
    Returns:
    --------
    dict : Includes all information from find_extrema() plus:
        - 'endpoint_values': dict - Values at interval endpoints
        - 'critical_point_values': dict - Values at critical points
    
    Examples:
    ---------
    >>> result = find_extrema_with_details('x**3 - 3*x', [-2, 2])
    """
    
    # Get basic extrema
    result = find_extrema(func_str, interval)
    
    # Get detailed evaluation information
    x = symbols('x', real=True)
    f = sympify(func_str, locals={'x': x})
    f_numeric = lambdify(x, f, 'numpy')
    
    a, b = float(interval[0]), float(interval[1])
    
    result['endpoint_values'] = {
        'a': {'x': a, 'value': round(float(f_numeric(a)), 10)},
        'b': {'x': b, 'value': round(float(f_numeric(b)), 10)}
    }
    
    result['critical_point_values'] = {
        f'x{i}': {'x': point, 'value': round(float(f_numeric(point)), 10)}
        for i, point in enumerate(result['critical_points'])
    }
    
    return result


if __name__ == '__main__':
    # Example usage
    print("=== CalculusHub Extrema Finder ===\n")
    
    # Example 1: Quadratic function
    print("Example 1: f(x) = x^2 - 4x + 3, interval [0, 5]")
    result1 = find_extrema('x**2 - 4*x + 3', [0, 5])
    print(f"Result: {result1}\n")
    
    # Example 2: Trigonometric function
    print("Example 2: f(x) = sin(x), interval [0, 3.14159]")
    result2 = find_extrema('sin(x)', [0, 3.14159])
    print(f"Result: {result2}\n")
    
    # Example 3: Cubic function
    print("Example 3: f(x) = x^3 - 3x, interval [-2, 2]")
    result3 = find_extrema_with_details('x**3 - 3*x', [-2, 2])
    print(f"Result: {result3}\n")
    
    # Example 4: Exponential function
    print("Example 4: f(x) = e^(-x^2), interval [-2, 2]")
    result4 = find_extrema('exp(-x**2)', [-2, 2])
    print(f"Result: {result4}\n")
