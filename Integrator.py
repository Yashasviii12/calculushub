from sympy import symbols, sympify, integrate, simplify, latex, pretty, SympifyError


def integrate_function():
    while True:
        raw = input("Enter function f(x): ").strip()
        if raw.lower() in {"quit", "exit", "q"}:
            print("Goodbye.")
            break
        if not raw:
            continue

        var_input = input("Integrate with respect to (default x): ").strip()
        var_name = var_input if var_input else "x"

        try:
            x = symbols(var_name)
            expr = sympify(raw)
            integral = integrate(expr, x)
            simplified = simplify(integral)

            print("\n  Original:   f =", pretty(expr, use_unicode=True))
            print("  Integral:   F =", pretty(simplified, use_unicode=True), "+ C")
            print("  LaTeX:      F =", latex(simplified), "+ C\\n")

        except SympifyError as e:
            print(f"Could not parse expression: {e}. Please check syntax.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    integrate_function()
