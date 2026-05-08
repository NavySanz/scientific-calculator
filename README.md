# 🔬 Scientific Calculator

> A fully-featured command-line scientific calculator built in pure Python — no external dependencies.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-30%2B%20passing-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Built-in Constants](#-built-in-constants)
- [Running Tests](#-running-tests)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Category | Operations |
|---|---|
| **Basic Arithmetic** | Addition, Subtraction, Multiplication, Division, Modulo, Floor Division |
| **Powers & Roots** | Power (`xⁿ`), Square Root (`√x`), Nth Root |
| **Logarithms** | Natural log (`ln`), Log base 10, Log base 2, Custom base |
| **Exponential** | `eˣ` |
| **Rounding** | Ceiling (`⌈x⌉`), Floor (`⌊x⌋`), Round to N decimals |
| **Factorial** | `n!` |
| **Trigonometry** | `sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan` |
| **Angle Conversion** | Degrees ↔ Radians |
| **Hyperbolic** | `sinh`, `cosh`, `tanh` |
| **Constants** | π, e, τ, φ (golden ratio), ∞ |

---

## 🎬 Demo

```
╔══════════════════════════════════════════╗
║        🔬 Scientific Calculator          ║
╠══════════════════════════════════════════╣
║  BASIC          │  SCIENTIFIC            ║
║  1. Add         │  9.  Square Root       ║
║  2. Subtract    │  10. Nth Root          ║
║  3. Multiply    │  11. Power             ║
║  4. Divide      │  12. Log (natural)     ║
║  ...            │  ...                   ║
╚══════════════════════════════════════════╝

Enter option: 11
  base = 2
  exponent = 10
  ✔  Result: 1024

Enter option: 9
  x = 144
  ✔  Result: 12

Enter option: 19
  x (radians) = pi
  → Using pi = 3.141592653589793
  ✔  Result: 0
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8 or higher** — check your version with:
  ```bash
  python --version
  ```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/NavySanz/scientific-calculator.git

# 2. Navigate into the project folder
cd scientific-calculator

# 3. Run the calculator (no install needed!
python calculator.py
```

---

## 🧮 Usage

Once launched, type the number of the operation you want and follow the prompts.

### Example — Square Root

```
Enter option: 9
  x = 256
  ✔  Result: 16
```

### Example — Trigonometry

```
Enter option: 19        ← sin
  x (radians) = pi
  → Using pi = 3.141592653589793
  ✔  Result: 0
```

### Example — Logarithm

```
Enter option: 12        ← natural log
  x = e
  → Using e = 2.718281828459045
  ✔  Result: 1.0
```

### Example — Factorial

```
Enter option: 16
  n = 10
  ✔  Result: 3628800
```

---

## 🔢 Built-in Constants

When prompted for a number, you can type any of these constant names directly:

| Name | Symbol | Value |
|------|--------|-------|
| `pi` | π | `3.14159265358979...` |
| `e` | e | `2.71828182845904...` |
| `tau` | τ | `6.28318530717958...` |
| `phi` | φ | `1.61803398874989...` (Golden ratio) |
| `inf` | ∞ | Infinity |

---

## 🧪 Running Tests

The project comes with 30+ unit tests covering every function.

```bash
# Install pytest (one-time setup)
pip install pytest

# Run all tests with verbose output
python -m pytest tests/ -v
```

Expected output:

```
tests/test_calculator.py::TestBasicOperations::test_add            PASSED
tests/test_calculator.py::TestBasicOperations::test_divide         PASSED
tests/test_calculator.py::TestBasicOperations::test_divide_by_zero PASSED
...
30 passed in 0.12s
```

---

## 📁 Project Structure

```
scientific-calculator/
│
├── calculator.py            # Core logic + CLI interface
│
├── tests/
│   └── test_calculator.py   # Unit tests (pytest)
│
├── requirements-dev.txt     # Dev dependencies (pytest only)
├── .gitignore               # Python gitignore
└── README.md                # You are here!
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make** your changes and add tests if applicable
4. **Run** the test suite
   ```bash
   python -m pytest tests/ -v
   ```
5. **Commit** your changes
   ```bash
   git commit -m "Add: your feature description"
   ```
6. **Push** and open a **Pull Request**

### Ideas for Contributions

- 🖥️ GUI version using Tkinter or PyQt
- 📜 Calculation history with save/load
- 🔢 Complex number support
- 📐 Matrix operations

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

```
MIT License

Copyright (c) 2025 NavySanz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so.
```

---

## 👤 Author

**Your Name**
- GitHub: [@NavySanz](https://github.com/NavySanz)

---

<p align="center">Made with ❤️ and Python</p>
