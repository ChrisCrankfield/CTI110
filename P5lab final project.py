#Crankfield Chris
#7/22/20024
#Project
#Calculating items and prices 


def disperse_change(change_due):
    dollars = int(change_due)
    change_due = (change_due - dollars) * 100
    quarters = int(change_due // 25)
    change_due = 25
    dimes = int(change_due // 10)
    change_due = 10
    nickels = int(change_due // 5)
    change_due = 5
    pennies = int(change_due)
    
    #breakdown
    if dollars > 0:
        print(dollars, "Dollars")
    if quarters > 0:
        print(quarters, "Quarters")
    if dimes > 0:
        print(dimes, "Dimes")
    if nickels > 0:
        print(nickels, "Nickels")
    if pennies > 0:
        print(pennies, "Pennies")
def show_avail_items(item_dict):
    print(f'{"Grocery Item":<15}{"Price":<12}')
    print("-" * 40 )
    for item, price in item_dict.items():
        print(f"{item}: ${price:.2f}")
def show_cart(cart):
    print("Grocery Checkout Recepit:")
    print("-" * 40 )
    for item in cart:
        print(item)
def calc_total(cart, item_dict):
    subtotal = 0
    for item in cart:
        if item in item_dict:
            subtotal += item_dict[item]
    
    tax = subtotal * 0.21
    total_cost = subtotal + tax
    
    print("Receipt:")
    for item in cart:
        if item in item_dict:
            print(f"{item}: ${item_dict[item]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax ($0.21)")
    print(f"Total: ${total_cost:.2f}")
    
    return total_cost
def main():
    #Available items and their prices
    item_prices = {
        "apple": 3.69,
        "berries": 4.00,
        "chocolate": 2.89,
        "turkey": 6.99,
        "cheese": 4.00,
        "pepsi": 7.89,
        "eggs": 3.50,
        "bread": 3.00,
        
    }
    
   
    
    # Show available items
    show_avail_items(item_prices)
    
    # Shopping cart (empty list to start)
    cart = []
    
    # Prompt user to add items to cart
    while True:
        item = input("Enter an item to add to cart (type 'end' to finish): ").lower()
        if item == 'end':
            break
        elif item in item_prices:
            cart.append(item)
        else:
            print("That item is not in stock")
        
            
    
    # Show items in cart
    show_cart(cart)
    
    # Calculate total cost
    total_cost = calc_total(cart, item_prices)
    
    # Simulate payment 
    print("\nPayment Details:")
    print(f"Amount due: ${total_cost:.2f}")
    cash_given = float(input("Enter amount of cash given: $"))
    change_due = cash_given - total_cost
    
    # Display change breakdown
    if change_due >= 0:
        print(f"Change due: ${change_due:.2f}")
        print("Change breakdown:")
        disperse_change(change_due)
    else:
        print("Insufficient funds!")

if __name__ == "__main__":
    main()



