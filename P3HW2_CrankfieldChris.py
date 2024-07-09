# Chris Crankfield
# 7-9-2024
# P3HW2
# This program will calucalte an employee's pay

#Request employee information

name = input ( "Enter the employee's name: ")
hoursWorked = float ( input("Enter number of hours worked: "))
payRate =float(input("Enter the employee's pay rate: "))

if hoursWorked > 40:
    # Calculate overtime
    ovtHours = hoursWorked - 40
    # Calculate ovetime pay
    ovtPay = ovtHours * (payRate * 1.5)
    #Calculate pay for regular hours
    regPay = 40 * payRate
    #Calculate gross pay
    grossPay = regPay + ovtPay


else:
    # set over time hours and pay to zero
    ovtHours = 0
    ovtPay = 0
    regPay = payRate * hoursWorked
    grossPay = regPay




print("-"*37)
print("Employee name: ",name,"\n")

print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
print("-" * 100)

print(f'{hoursWorked:<15}{payRate:<12}{ovtHours:<12}{ovtPay:<20.2f}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')
