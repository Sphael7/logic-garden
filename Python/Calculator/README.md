# 🧮 Advanced Python Calculator

A robust and interactive **command-line calculator** built in Python.
It supports arithmetic evaluation, linear and system equation solving, as well as power and root calculations — all handled **safely** and with **error protection**.

---

## 🚀 Features

-   **Expression Evaluator**
    Safely parses and evaluates arithmetic expressions using Python’s `ast` module to prevent code injection.
    > Example: `3 + 5 * (2 - 1)` → `8`

-   **Linear Equation Solver**
    Solves single-variable equations in the form **ax + b = 0**.
    > Example: `2x + 4 = 0` → `x = -2`

-   **System of Linear Equations (2 Variables)**
    Solves systems like:
    ```text
    a1*x + b1*y = c1  
    a2*x + b2*y = c2
    ```
    using **Cramer’s Rule**.

-   **Power and Root Calculator**
    Computes exponents and roots with validation for invalid or complex results.
    > Examples:
    > Power: `2^3` → `8`
    > Root: `x^(1/3)` → cube root of x

-   **Error Handling**
    Graceful handling for invalid input, division by zero, and disallowed operations.

-   **Modular Design**
    Each operation is implemented in its own function so the code is easy to extend and test.

---

## 🧰 Tech Stack

| Component | Detail |
| :--- | :--- |
| **Language** | Python 3 |
| **Core Modules** | `ast`, `math` |

---

## ⚙️ How to Run

1.  **Clone this repository** (or your fork):

    ```bash
    git clone [https://github.com/sphael/logic-garden.git](https://github.com/sphael/logic-garden.git)
    cd logic-garden/calculator
    ```

2.  **Run the program**:

    ```bash
    python calculator.py
    ```

3.  Follow the on-screen menu to use different features.

---

## 🧩 Menu Overview

| Option | Function | Description |
| :---: | :--- | :--- |
| **1** | Arithmetic Expression | Evaluate safe math expressions |
| **2** | Linear Equation | Solve `ax + b = 0` |
| **3** | System of Equations | Solve two-variable equations |
| **4** | Power & Root | Compute exponents and roots |
| **0** | Exit | Quit the calculator |

---

## 🛡️ Safety

All mathematical expressions are parsed using Python’s **Abstract Syntax Trees (AST)** to prevent execution of arbitrary code. Inputs are validated and common math errors (like division by zero) are handled gracefully.

---

## 🧩 Implementation Notes

-   `_evaluate_expression_safely(expression: str)` uses `ast.parse` and `ast.walk` to allow **only math-related AST nodes** before compiling and evaluating the AST.
-   Linear and system solvers handle edge cases (**no solution, infinite solutions**) using determinant checks with a small epsilon for floating point comparisons.
-   Power & root handler supports both direct exponents and `1/n` root notation; it **rejects even roots of negative numbers** to avoid complex results (the program reports a math error instead).
-   The program uses a simple dictionary mapping for menu choices to keep the main loop clean and extensible.

---

##
## ✅ Example Session

```text
=== Advanced Python Calculator ===
1. Arithmetic Expression
2. Linear Equation (ax + b = 0)
3. System of Equations (2 vars)
4. Power & Root
0. Exit

Select option: 1
Enter arithmetic expression: 3 + 4 * 2
Result: 11
```

---

## 👨‍💻 Author

-   **Developer**: Sphael7 — [https://github.com/sphael](https://github.com/Sphael7)
-   **Project**: Logic Garden — [https://github.com/sphael/logic-garden](https://github.com/Sphael7/logic-garden)

---

## 🪴 Part of Logic Garden

This calculator is part of **Logic Garden**, a long-term collection of small, independent coding experiments focused on clean logic, reusability, and continual learning.