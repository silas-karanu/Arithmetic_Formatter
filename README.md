# Arithmetic_Formatter
Receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The program should optionally take a second argument. When the second argument is set to True, the answers should be displayed.


# ➕ Arithmetic Arranger

A Python function that formats and optionally solves a list of arithmetic problems (addition and subtraction) vertically, similar to how they would appear on paper.

---

## ✅ Features

- Arranges up to 5 arithmetic problems
- Supports `+` and `-` operators only
- Validates input format, length, and digits
- Optionally displays computed answers
- Output is a single formatted string suitable for printing

---

## 🧠 How It Works

For each arithmetic problem:
- Splits the expression into two operands and one operator
- Validates all components (e.g., digits only, max 4 digits)
- Right-aligns numbers based on width
- Optionally computes and includes answers if `show_answers=True`
- Joins all formatted parts with 4 spaces between each problem

---

## 📌 Function Signature

```python
def arithmetic_arranger(problems, show_answers=False):
```
---

## Parameters:
- `problems` (list[str]): A list of up to 5 arithmetic expressions (e.g., `"32 + 698"`)
- `show_answers` (bool): If `True`, also show the results of the problems (default: `False`)

---

## ❗ Validation Rules
- Maximum of 5 problems

- Operands must be digits only

- No more than 4 digits per operand

- Operators must be + or -

- Returns string error messages for invalid input

---

## 📦 Example Use Case
```python
arranged = arithmetic_arranger(["3 + 855", "988 + 40"], show_answers=True)
print(arranged)
```
---

## 🛠 Possible Improvements
Add support for `*` and `/` operators

Handle float numbers or negatives (currently not supported)

Return structured data (list of dicts) for custom rendering

---

## 🧑‍💻 License
MIT License – free to use and modify.
