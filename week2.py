# Create a Dynamic Shopping Cart Program

def add_to_cart(cart = {}, item_name = '', price = 0, *args, **kwargs):
    cart = {}
    print("Welcome and Happy Shopping!")
    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == "done":
            break

        price = float(input(f"Enter the price for {item_name}: "))
        discount_input = input("Enter discounts (if any, separated by space, e.g., 10 20): ").strip()
        args = [float(d) for d in discount_input.split()]
        details = input("Enter item details (e.g., color=red size=large, separated by spaces): ").strip()
        kwargs = dict(item.split("=") for item in details.split())

        # Check if the item already exists in the cart ! not working
        if item_name in cart:
            print(f"{item_name} is already in the cart!")
            return cart

        # Apply discounts, if provided
        final_price = price
        for discount in args:
            final_price -= (final_price * discount / 100)

        # Add item to the cart
        cart[item_name] = {
            "original_price": price,
            "final_price": round(final_price, 2),
            "details": kwargs,
        }
        print(f"Added {item_name} to the cart with a final price of ${round(final_price, 2)}.")
    
    # Cart summary
    if cart:
        print("\n--Cart Summary--\n")
        total_cost = 0
        for item, details in cart.items():
            print(f"{item}: Final Price = ${details['final_price']}, Original Price = ${details['original_price']}")
            if details["details"]:
                print(f"  Details: {details['details']}")
            total_cost += details["final_price"]
        print(f"\nTotal Cost: ${round(total_cost, 2)}")
    else:
        print("Your cart is empty!")

    

add_to_cart()