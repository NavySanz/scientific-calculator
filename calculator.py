"""
Scientific Calculator
A command-line scientific calculator built in Python.
"""

import math
import operator


# ── Basic Operations ──────────────────────────────────────────────────────────

def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return a / b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def modulo(a: float, b: float) -> float:
    """Return a % b."""
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero.")
    return a % b

def power(base: float, exp: float) -> float:
    """Return base ** exp."""
    return base ** exp

def floor_divide(a: float, b: float) -> float:
    """Return a // b (integer division)."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a // b


# ── Scientific Operations ─────────────────────────────────────────────────────

def square_root(x: float) -> float:
    """Return √x. Raises ValueError for negative input."""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)

def nth_root(x: float, n: float) -> float:
    """Return the nth root of x."""
    if n == 0:
        raise ValueError("Root degree cannot be zero.")
    if x < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of a negative number.")
    return math.copysign(abs(x) ** (1 / n), x)

def logarithm(x: float, base: float = math.e) -> float:
    """Return log_base(x). Defaults to natural log."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    if base <= 0 or base == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    return math.log(x, base)

def log10(x: float) -> float:
    """Return log base 10 of x."""
    return logarithm(x, 10)

def log2(x: float) -> float:
    """Return log base 2 of x."""
    return logarithm(x, 2)

def exponential(x: float) -> float:
    """Return e^x."""
    return math.exp(x)

def absolute(x: float) -> float:
    """Return |x|."""
    return abs(x)

def factorial(n: int) -> int:
    """Return n! Raises ValueError for negative or non-integer input."""
    if not isinstance(n, (int, float)) or n != int(n):
        raise ValueError("Factorial is only defined for non-negative integers.")
    n = int(n)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def ceiling(x: float) -> int:
    """Return the smallest integer >= x."""
    return math.ceil(x)

def floor(x: float) -> int:
    """Return the largest integer <= x."""
    return math.floor(x)

def round_to(x: float, decimals: int = 0) -> float:
    """Round x to a given number of decimal places."""
    return round(x, decimals)


# ── Trigonometry (radians) ────────────────────────────────────────────────────

def sine(x: float) -> float:
    """Return sin(x) where x is in radians."""
    return math.sin(x)

def cosine(x: float) -> float:
    """Return cos(x) where x is in radians."""
    return math.cos(x)

def tangent(x: float) -> float:
    """Return tan(x) where x is in radians."""
    return math.tan(x)

def arcsine(x: float) -> float:
    """Return arcsin(x) in radians. x must be in [-1, 1]."""
    if not -1 <= x <= 1:
        raise ValueError("arcsin input must be in the range [-1, 1].")
    return math.asin(x)

def arccosine(x: float) -> float:
    """Return arccos(x) in radians. x must be in [-1, 1]."""
    if not -1 <= x <= 1:
        raise ValueError("arccos input must be in the range [-1, 1].")
    return math.acos(x)

def arctangent(x: float) -> float:
    """Return arctan(x) in radians."""
    return math.atan(x)

def degrees_to_radians(deg: float) -> float:
    """Convert degrees to radians."""
    return math.radians(deg)

def radians_to_degrees(rad: float) -> float:
    """Convert radians to degrees."""
    return math.degrees(rad)


# ── Hyperbolic Functions ──────────────────────────────────────────────────────

def sinh(x: float) -> float:
    """Return hyperbolic sine of x."""
    return math.sinh(x)

def cosh(x: float) -> float:
    """Return hyperbolic cosine of x."""
    return math.cosh(x)

def tanh(x: float) -> float:
    """Return hyperbolic tangent of x."""
    return math.tanh(x)


# ── Constants ─────────────────────────────────────────────────────────────────

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "phi": (1 + math.sqrt(5)) / 2,   # Golden ratio
    "inf": math.inf,
}


# ── CLI Interface ─────────────────────────────────────────────────────────────

MENU = """
╔══════════════════════════════════════════╗
║        🔬 Scientific Calculator          ║
╠══════════════════════════════════════════╣
║  BASIC          │  SCIENTIFIC            ║
║  1. Add         │  9.  Square Root       ║
║  2. Subtract    │  10. Nth Root          ║
║  3. Multiply    │  11. Power             ║
║  4. Divide      │  12. Log (natural)     ║
║  5. Modulo      │  13. Log base 10       ║
║  6. Floor Div   │  14. Log base 2        ║
║                 │  15. Exponential (e^x) ║
║  TRIG (radians) │  16. Factorial (n!)    ║
║  17. sin        │  17. Absolute value    ║
║  18. cos        │  18. Ceiling / Floor   ║
║  19. tan        │                        ║
║  20. arcsin     │  CONSTANTS             ║
║  21. arccos     │  C. Show constants     ║
║  22. arctan     │                        ║
║  23. deg→rad    │  Q. Quit               ║
║  24. rad→deg    │                        ║
╚══════════════════════════════════════════╝
"""

def get_float(prompt: str) -> float:
    """Prompt user for a float value, supporting constant names."""
    while True:
        raw = input(prompt).strip().lower()
        if raw in CONSTANTS:
            print(f"  → Using {raw} = {CONSTANTS[raw]}")
            return CONSTANTS[raw]
        try:
            return float(raw)
        except ValueError:
            print("  ⚠  Invalid number. Try again.")

def get_int(prompt: str) -> int:
    """Prompt user for an integer value."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ⚠  Please enter a whole number.")

def show_result(result: float) -> None:
    """Display the result nicely."""
    if isinstance(result, float) and result.is_integer():
        print(f"\n  ✔  Result: {int(result)}\n")
    else:
        print(f"\n  ✔  Result: {result}\n")

def run():
    """Main calculator loop."""
    print(MENU)
    while True:
        choice = input("Enter option: ").strip().lower()

        try:
            if choice == "q":
                print("Goodbye! 👋")
                break

            elif choice == "c":
                print("\n  Constants:")
                for name, val in CONSTANTS.items():
                    print(f"    {name:6} = {val}")
                print()

            elif choice == "1":
                a, b = get_float("  a = "), get_float("  b = ")
                show_result(add(a, b))

            elif choice == "2":
                a, b = get_float("  a = "), get_float("  b = ")
                show_result(subtract(a, b))

            elif choice == "3":
                a, b = get_float("  a = "), get_float("  b = ")
                show_result(multiply(a, b))

            elif choice == "4":
                a, b = get_float("  a = "), get_float("  b = ")
                show_result(divide(a, b))

            elif choice == "5":
                a, b = get_float("  a = "), get_float("  b = ")
                show_result(modulo(a, b))

            elif choice == "6":
                a, b = get_float("  a = "), get_float("  b = ")
                show_result(floor_divide(a, b))

            elif choice == "9":
                x = get_float("  x = ")
                show_result(square_root(x))

            elif choice == "10":
                x = get_float("  x = ")
                n = get_float("  n (root degree) = ")
                show_result(nth_root(x, n))

            elif choice == "11":
                base = get_float("  base = ")
                exp = get_float("  exponent = ")
                show_result(power(base, exp))

            elif choice == "12":
                x = get_float("  x = ")
                show_result(logarithm(x))

            elif choice == "13":
                x = get_float("  x = ")
                show_result(log10(x))

            elif choice == "14":
                x = get_float("  x = ")
                show_result(log2(x))

            elif choice == "15":
                x = get_float("  x = ")
                show_result(exponential(x))

            elif choice == "16":
                n = get_float("  n = ")
                show_result(factorial(n))

            elif choice == "17":
                x = get_float("  x = ")
                show_result(absolute(x))

            elif choice == "18":
                x = get_float("  x = ")
                c = ceiling(x)
                f = floor(x)
                print(f"\n  ✔  Ceiling: {c}  |  Floor: {f}\n")

            elif choice == "19":
                x = get_float("  x (radians) = ")
                show_result(sine(x))

            elif choice == "20":  # actually mapped to sin above — reassigning
                x = get_float("  x (radians) = ")
                show_result(cosine(x))

            elif choice == "21":
                x = get_float("  x (radians) = ")
                show_result(tangent(x))

            elif choice == "22":
                x = get_float("  x ∈ [-1, 1] = ")
                show_result(arcsine(x))

            elif choice == "23":
                x = get_float("  x ∈ [-1, 1] = ")
                show_result(arccosine(x))

            elif choice == "24":
                x = get_float("  x = ")
                show_result(arctangent(x))

            else:
                print("  ⚠  Unknown option. Please choose from the menu.\n")

        except (ValueError, ZeroDivisionError) as err:
            print(f"\n  ✖  Error: {err}\n")


if __name__ == "__main__":
    run()
