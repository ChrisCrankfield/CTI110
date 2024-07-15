# Chris Crankfield
# 7-9-2024
# P3HW2
# This program will calculate an employee's pay


# Begin loop to input employee data
while True:
    # Request employee information
    name = input("Enter the employee's name (enter 'Done' to finish): ")
    
    # Check if user wants to terminate
    if name.lower() == 'done':
        break
    
    hoursWorked = float(input("Enter number of hours worked? "))
    payRate = float(input("Enter the employee's pay rate? "))
    
    
    if hoursWorked > 40:
        # Calculate overtime
        ovtHours = hoursWorked - 40
        # Calculate overtime pay
        ovtPay = ovtHours * (payRate * 1.5)
        # Calculate pay for regular hours
        regPay = 40 * payRate
        # Calculate gross pay
        grossPay = regPay + ovtPay
    else:
        ovtHours = 0
        ovtPay = 0
        regPay = payRate * hoursWorked
        grossPay = regPay
    
    # Accumulate totals
    totalOvertime += ovtPay
    totalRegularPay += regPay
    totalGrossPay += grossPay
    employeeCount += 1
    
    # Print employee pay details
    print("-" * 37)
    print("Employee name: ", name, "\n")
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print("-" * 100)
    print(f'{hoursWorked:<15}{payRate:<12}{ovtHours:<12}{ovtPay:<20.2f}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')
    print("-" * 100)

# Print totals and summary
print("\nSummary:")
print(f"Total overtime paid: ${totalOvertime:.2f}")
print(f"Total regular pay: ${totalRegularPay:.2f}")
print(f"Total gross pay: ${totalGrossPay:.2f}")
print(f"Number of employees: {employeeCount}")
