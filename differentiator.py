from sympy import symbols, sympify, diff, simplify, latex, pretty, SympifyError

def differentiate_function():
   
    while True:
        raw = input("Enter function f(x): ").strip()
        if raw.lower() in {"quit", "exit", "q"}:
            print("Goodbye.")
            break
        if not raw:
            continue

        var_input = input("Differentiate with respect to (default x): ").strip()
        var_name = var_input if var_input else "x"

        try:
            x = symbols(var_name)
            expr = sympify(raw)
            derivative = diff(expr, x)
            simplified = simplify(derivative)

            print("\n  Original:    f =", pretty(expr, use_unicode=True))
            print("  Derivative: f' =", pretty(simplified, use_unicode=True))
            print("  LaTeX:      f' =", latex(simplified))
            print()
        except SympifyError as e:
            print(f"Could not parse expression: {e}. Please check syntax.")
        except Exception as e:
            print(f"Error: {e}")

a=int(input("enter the function:"))
    differentiate_function(a)
