# Crankfield Chris

# July 16, 2024

# P5LAB

# This program will simulate a customer using a self-checkout machine.

# A random float value will be generated as the total owed for the purchase



# User define function





#Function to determine change returned to customer

import random





def disperse_change (change):

   

     

  if change == 0:

    print("No Change Due")



  #Calculate the amount of each coin needed

  #integer division - //



  num_dollars = change // 100

  change = change - (num_dollars * 100)



  num_quarters = change // 25

  change = change - (num_quarters * 25)



  num_dimes = change // 10

  change = change - (num_dimes * 10)



  num_nickles = change // 5

  change = change - (num_nickles *5)



  num_pennies = change // 1



  #Display coins owed



  if num_dollars > 0:

      print(num_dollars, end=" ")

      if num_dollars == 1:

        print("Dollar")

      else:

        print("Dollars")

         

  if num_quarters > 0:

      print(num_quarters, end=" ")

      if num_quarters == 1:

        print("Quarter")

      else:

        print("Quarters")



  if num_dimes > 0:

      print(num_dimes, end=" ")

      if num_dimes == 1:

        print("Dime")

      else:

        print("Dimes")



  if num_nickles > 0:

      print(num_nickles, end=" ")

      if num_nickles == 1:

        print("Nickle")

      else:

        print("Nickles")



  if num_pennies > 0:

      print(num_pennies, end=" ")

      if num_pennies == 1:

        print("Penny")

      else:

        print("Pennies")





#Main Function

def main() :

  # generate a random float number

  amount_owed = round(random.uniform(0.01, 100.00), 2)



  # Display the amount owed

  print(f"You owe: $(amount_owed:.2f)")

   

  # prompt user to enter float as cash they will put in the checkout machine

  amount_paid = float(input("How much cash will you put in the self_checkout? "))

   

  # calculate the change owed

  change_owed = amount_paid - amount_owed

   

  # Display change owed

  print(f"Change is: $(change_owed:.2f)")

  print()

   

  # Convert the change owed into an integer

  change_owed = round(change_owed * 100)

   

  # Call function and call the change owed as a parameter

  disperse_change(change_owed)



#Call the main function

main()
