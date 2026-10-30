
# Basic Calculator

A Python program that performs basic arithmetic operations on two numbers entered by the user. The program supports addition, subtraction, multiplication, and division, with input validation and exception handling to manage invalid inputs and division by zero.

## Features

- Accepts two numerical inputs from the user.
- Supports four basic arithmetic operations: addition, subtraction, multiplication, and division.
- Validates the entered arithmetic operator.
- Prevents division by zero using exception handling.
- Handles invalid numerical inputs without terminating the program.
- Uses a `while` loop to repeatedly request valid inputs until all entries are correct.
- Employs a standalone `operation()` function to separate calculation logic from input handling.

## Supported Operations

| Operator | Operation | Example |
| :--- | :--- | :--- |
| `+` | Addition | `10 + 5 = 15` |
| `-` | Subtraction | `10 - 5 = 5` |
| `*` | Multiplication | `10 * 5 = 50` |
| `/` | Division | `10 / 5 = 2` |

## How to Run

1. Ensure Python 3 is installed.
2. Execute the file via your terminal:
   ```bash
   python calculator.py
   ```
3. Enter the first number, second number, and desired operator when prompted.

## Examples

### Addition

```text
Enter First number of operation: 10
Enter Second Number of operation: 5
Enter the symbol of operand: +
Answer: 15.0
```

### Division by Zero

```text
Enter First number of operation: 10
Enter Second Number of operation: 0
Enter the symbol of operand: /
For a division second number cannot be zero.
```

### Invalid Operator

```text
Enter First number of operation: 10
Enter Second Number of operation: 5
Enter the symbol of operand: %
Please enter a valid operator (+, -, *, /).
```

### Invalid Numerical Input

```text
Enter First number of operation: abc
Please enter valid numbers.
```

## Concepts Used

- Function definition and function calls using `main()` and `operation()`
- Floating-point conversion using `float()`
- String input and whitespace removal using `.strip()`
- Conditional statements using `if`, `elif`, and `else`
- Tuple creation and membership testing using `not in`
- `while` loops for repeated input validation
- Exception handling using `try` and `except`
- Handling `ValueError` and `ZeroDivisionError`
- Raising exceptions using `raise`
- Using `else` with exception handling
- Returning calculated results from helper functions

## Limitations

- Supports only four basic arithmetic operations.
- Accepts numerical inputs only; expressions such as `10 + 5 * 2` are not supported.
- Does not support advanced mathematical operations such as exponentiation, square roots, or percentages.
- Requires all three inputs to be valid before performing a calculation.

## Course Context

- **Course:** CS50P (CS50's Introduction to Programming with Python)
- **Problem Set:** 3 (Exceptions)
