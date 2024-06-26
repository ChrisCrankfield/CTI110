# Chris Crankfield
# 6/20/2024
# P1HW1
# This program demonstrates basic input-output operations and arithmetic calculations in Python.

def main():
    # Part 1: Power Calculation
    base = int(input("Enter an integer as the base value: "))
    exponent = int(input("Enter an interger as the exponet: "))
    result = base ** exponent
    print(f"{base} to the power of {exponent} is {result}!")

    # Part 2: Arithmetic Operations
    num1 = int(input("Enter a starting integer: "))
    num2 = int(input("Enter an integer to add: "))
    num3 = int(input("Enter an integer to subtract: "))

    sum_ab = num1 + num2
    final_result = sum_ab - num3

    # Printing the formatted output
    print(f"The result of {num1} + {num2} - {num3} is {final_result}")

if __name__ == "__main__":
    main()
