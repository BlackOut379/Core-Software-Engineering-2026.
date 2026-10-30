
# Marks Percentage Calculator

A Python program that accepts marks for multiple subjects, validates each entry, and calculates the average percentage once the user finishes entering marks. The program uses exception handling to manage invalid inputs and a helper function to separate calculation logic from input handling.

## Features

- Accepts marks for multiple subjects through continuous user input.
- Uses `complete` as a termination command to finish entering marks.
- Validates that marks are integer values between 0 and 100 (inclusive).
- Handles invalid numerical inputs and out-of-range marks using exception handling.
- Tracks the total marks and number of subjects entered.
- Calculates the average percentage using a standalone `percent()` function.
- Displays the final percentage rounded to two decimal places.
- Handles cases where no marks have been entered.

## Validation Rules

| Condition | Program Behaviour |
| :--- | :--- |
| Marks between 0 and 100 | Accepts the marks |
| Marks below 0 | Rejects the input |
| Marks above 100 | Rejects the input |
| Non-integer input | Displays an error message |
| `complete` | Stops accepting marks |
| No marks entered | Displays a message instead of calculating |

## How to Run

1. Ensure Python 3 is installed.
2. Execute the file via your terminal:
   ```bash
   python percentage.py
   ```
3. Enter marks for each subject when prompted.
4. Type `complete` when you have finished entering marks.

## Examples

### Multiple Subjects

```text
Enter marks according to sequence in integer form. Once marks is done type complete.
Enter marks of 1 subject: 85
Enter marks of 2 subject: 90
Enter marks of 3 subject: 75
Enter marks of 4 subject: complete
Percentage is 83.33%
```

### Invalid Marks

```text
Enter marks of 1 subject: 120
Marks should be under 100 and above 0.
Enter marks of 1 subject: 85
```

### Invalid Data Type

```text
Enter marks of 1 subject: abc
Enter Integer value.
```

### No Marks Entered

```text
Enter marks of 1 subject: complete
No marks were entered. Cannot calculate percentage.
```

## Concepts Used

- Function definition and function calls using `main()` and `percent()`
- Variables and assignment for tracking total marks and subject count
- Formatted strings using f-strings
- Continuous input handling using `while True`
- Type conversion using `int()`
- String methods using `.lower()`
- Conditional statements using `if`, `elif`, and `else`
- Exception handling using `try` and `except`
- Raising custom `ValueError` exceptions using `raise`
- Exception handling with `else`
- Loop termination using `break`
- Arithmetic operations for calculating average percentage
- Floating-point formatting using `:.2f`
- Functional decomposition using a helper function

## Limitations

- Accepts integer marks only; decimal marks are not supported.
- Treats every subject as equally weighted.
- Does not store individual subject marks after calculation.
- Requires the user to type `complete` to finish entering marks.

## Course Context

- **Course:** CS50P (CS50's Introduction to Programming with Python)
- **Lecture:** 2 (Loops)
- **Additional Concepts:** Exception Handling
