import matplotlib.pyplot as graph
import numpy as np
import sympy as sp
def graph_analysis(func, x_min=-100, x_max=100):

    x=sp.symbols('x')
    try:
        expr=sp.sympify(func)
    except Exception as e:
        print(f"Error parsing the function: {e}")
        print("Make sure to use '*' for multiplication and '**' for exponents.")
        return
    print(f"\n Analyzing the function: {expr}")
    print("-" * 50)
    # Find pts. of discontinuity
    discontinuities = sp.singularities(expr, x, domain=sp.S.Reals)
    # Calculate derivative
    derivative = sp.diff(expr, x)
    # find non differentiable points
    non_differentiable_points = sp.singularities(derivative, x, domain=sp.S.Reals)
    # Display results
    print(f" Derivative: {derivative}")
    print(f" Discontinuities: {discontinuities}")
    print(f" Non-differentiable points: {non_differentiable_points}")
    print("-" * 50)
    # Plot the function
    f_numeric = sp.lambdify(x, expr, modules=['numpy'])
    real_discontinuities = sorted([float(d) for d in discontinuities if d.is_real])
    buffer = 0.01
    if not real_discontinuities:
        x_vals = np.linspace(x_min, x_max, 2000)
        with np.errstate(divide='ignore', invalid='ignore'):
            y_vals = f_numeric(x_vals)
        graph.plot(x_vals, y_vals, label=f"f(x) = {expr}", color='blue', linewidth=2)
    else:
        boundaries = [x_min] + real_discontinuities + [x_max]
        for i in range(len(boundaries) - 1):
            left, right = boundaries[i], boundaries[i + 1]
            if left in real_discontinuities:
               left += buffer
            
            if right in real_discontinuities:
                right -= buffer
            x_vals = np.linspace(left, right, 1000)
            with np.errstate(divide='ignore', invalid='ignore'):
                y_vals = f_numeric(x_vals)
            lbl = f"f(x) = {expr}" if i == 0 else ""
            graph.plot(x_vals, y_vals, label=lbl, color='blue', linewidth=2,)
    real_non_diff_points = [float(p) for p in non_differentiable_points if p.is_real]
    for point in real_discontinuities:
        graph.axvline(x=point, color='red', linestyle='--', alpha=0.7, label=f"Discontinuity at x={point}" if point == real_discontinuities[0] else "")
    for point in real_non_diff_points:
        if point not in real_discontinuities:
            graph.axvline(x=point, color='orange', linestyle='--', alpha=0.8, linewidth=2, label=f"Non-differentiable at x={point}" if point == real_non_diff_points[0] else "")
    graph.axhline(0, color='black', linewidth=0.8)
    graph.axvline(0, color='black', linewidth=0.8)
    graph.grid(True, linestyle=':', alpha=0.6)
    graph.title(f"Graph of f(x) = {expr}")
    graph.xlabel("x")
    graph.ylabel("f(x)")
    graph.xlim(x_min, x_max)
    graph.ylim(-100, 100)
    graph.legend()
    graph.show()

#running the function
input_expr = input("Enter a function of x: ")
graph_analysis(input_expr)
