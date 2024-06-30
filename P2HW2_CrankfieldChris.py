# Crankfield Chris
# 6/30/2024
# P2HW2
# This program manages grades for multiple modules.


#Initialize an empty list to store grades.
grades = []

#Prompt user to enter grades for each module.

# Loop through modules 1 to 6 and ask for grades.
for i in range(1, 7):
    grade = float(input(f"Enter the grade for each Module {i}: "))
    grades.append(grade)

# Step 3: Calculate required statistics
lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

# Step 4: Display results as specified
print("\nResults:")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {sum_grades}")
print(f"Average Grade: {average_grade:.2f}")  # Display average with two decimal places
