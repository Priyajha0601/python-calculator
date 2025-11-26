# --- Simple Python Calculator Program ---

def calculator():
    print("\n--- Simple Calculator ---")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print(f"Result: {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1 * num2}")
    elif choice == "4":
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid choice")

calculator()

# 🧮 Python Calculator Program

A basic calculator built with Python that performs simple math operations using user input.

## 🚀 Features
- Add, subtract, multiply, divide
- Simple, beginner-friendly code
- Runs in any Python environment or online compiler

## 📂 Project Files
| File | Description |
|------|-------------|
| `calculator.py` | Main program file |

## ▶ How to Run
Open a terminal and run:
```bash
python calculator.py

