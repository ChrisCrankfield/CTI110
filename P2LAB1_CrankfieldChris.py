# Crankfield Chris
# 6/30/2024
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle based on user input radius

import math

def main():
    # Input
    radius = float(input("What is the radius of the circle? "))
    
    # Calculations
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    
    # Output
    print(f"The Diameter of the circle is {diameter:.1f}")
    print(f"The Circumference of the circle is {circumference:.2f}")
    print(f"The Area of the circle is {area:.3f}")

if __name__ == "__main__":
    main()
