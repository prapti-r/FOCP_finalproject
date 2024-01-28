# function for getting number of pizza orderd
def pizza_orderd():
    """
    Finds the number of pizzas ordered

    Returns:
       pizza (int): The numbers of pizza orderd.
    """

    while True:
        try:
            pizza = int(input("How many pizzas ordered? "))
            if pizza <= 0:
                print("Please enter a positive integer!")
                continue  # Continue the loop to prompt the correct input again
            return pizza
        except ValueError:
            print("Please enter a number!")


# fuction to get yes or no from user
def user_input(prompt):
    """
    Asks user input for yes/no questions.

    Parameters:
        prompt (str): The prompt to ask input to the user.

    Returns:
        user (str): The user's input, converted to lowercase.
    """

    while True:
        try:
            user = input(prompt).lower()
            if user not in ["y", "yes", "n", "no"]:
                print("Please answer 'Y/Yes' or 'N/No'.")
                continue  # Continue the loop to prompt the correct input again
            return user
        except ValueError:
            print("Please answer 'Y/Yes' or 'N/No'.")


# function to calculate total pizza prices
def calcualte_pizza(pizza, tuesday, delivery, app):
    """
    Calculates the total price of a pizza order based on users input.

    Parameters:
        pizza (int): The numbers of pizzas ordered.
        tuesday (str): Ask whether it's Tuesday or not. Answer in 'yes' or 'no'.
        delivery (str): Ask whether delivery is needed. Answer in 'yes' or 'no'.
        app (str): Ask whether an app discount is applied. Answer in 'yes' or 'no'.

    Returns:
        total price (float): The total price of the pizza order after discounts and delivery cost.
    """

    try:
        pizza_price = 12.0
        tuesday_discount = 0.5
        delivery_cost = 2.50
        app_discount = 0.25

        # check if tuesday discount is applied
        if tuesday.lower() == "yes" or tuesday.lower() == "y":
            total_price = pizza * pizza_price
            total_price -= total_price * tuesday_discount
        else:
            total_price = pizza * pizza_price

        # Check if delivery is required
        if delivery.lower() == "yes" or delivery.lower() == "y" and pizza < 5:
            total_price += delivery_cost

        # Check if the app is used
        if app.lower() == "yes" or app.lower() == "y":
            total_price -= total_price * app_discount

        return total_price

    except Exception as e:
        print(f"Unexpected error: {e}")


# prints from here
name = "BPP Pizza Price Calculator"
print(name)
print("=" * len(name))
print()

# function called to get the input
pizza = pizza_orderd()
delivery = user_input("Is delivery required? ")
tuesday = user_input("Is it Tuesday? ")
app = user_input("Did the customer use the app? ")
print()

# calculate total price
total_price = calcualte_pizza(pizza, tuesday, delivery, app)

# Display the total price
print(f"Total Price: £{total_price:.2f}.")
