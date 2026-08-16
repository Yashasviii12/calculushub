from sympy import symbols, sympify, diff, solve, simplify, S, latex, pretty, SympifyError

def absolute_extrema():
    x = symbols('x')

    while True:
        raw = input("Enter function f(x): ").strip()
        if raw.lower() in {"quit", "exit", "q"}:
            print("Goodbye.")
            break
        if not raw:
            continue

        var_input = input("Variable (default x): ").strip()
        var_name = var_input if var_input else "x"
        x = symbols(var_name)

        try:
            a = sympify(input("Lower bound a: ").strip())
            b = sympify(input("Upper bound b: ").strip())
            if b < a:
                a, b = b, a

            expr = sympify(raw)
            df = diff(expr, x)

            critical = set()
            for sol in solve(df, x, domain=S.Reals):
                if sol.is_real and a <= sol <= b:
                    critical.add(sol)

            candidates = [a, b] + list(critical)
            values = []
            for pt in candidates:
                val = expr.subs(x, pt)
                if val.is_real:
                    values.append((pt, float(val)))

            abs_max = max(values, key=lambda item: item[1])
            abs_min = min(values, key=lambda item: item[1])

            print("\n  Original:   f =", pretty(expr, use_unicode=True))
            print("  Interval:  [", pretty(a, use_unicode=True), ", ", pretty(b, use_unicode=True), "]", sep="")
            print("  Critical: ", ", ".join(pretty(p, use_unicode=True) for p in critical) or "None")
            print("  Abs max:  f(", pretty(abs_max[0], use_unicode=True), ") = ", pretty(expr.subs(x, abs_max[0]), use_unicode=True), sep="")
            print("  Abs min:  f(", pretty(abs_min[0], use_unicode=True), ") = ", pretty(expr.subs(x, abs_min[0]), use_unicode=True), sep="")
            print("  LaTeX:    f(", latex(abs_max[0]), ") = ", latex(expr.subs(x, abs_max[0])), sep="")
            print("            f(", latex(abs_min[0]), ") = ", latex(expr.subs(x, abs_min[0])), "\n", sep="")

        except SympifyError as e:
            print(f"Could not parse expression: {e}. Please check syntax.\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    absolute_extrema()
