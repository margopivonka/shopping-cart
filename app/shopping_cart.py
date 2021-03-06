import datetime as dt
import os

TAX_RATE = 0.06

# Function to reformat price data in to user-friendly format
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# Function to reformat timestamp to user-friendly format
def human_friendly_timestamp(formatted_time):
    checkout_time = dt.datetime.now()
    formatted_time = checkout_time.strftime("%Y-%m-%d %H:%M")
    return formatted_time

# Function to calculate total price using subtotal and tax values
def calculate_total_price(subtotal,tax):
    total = subtotal + tax
    return total


if __name__ == "__main__":

    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


    #
    #CAPTURE AND VALIDATE USER SELECTIONS
    #
    subtotal = 0
    selected_products = []

    while True:
        selected_id = input("Please input a product identifier, or type 'DONE': ")
        if selected_id.upper() == "DONE":
            break
            #break keyword will stop a loop
        else:
            try:
                matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
                matching_product = matching_products[0]
                selected_products.append(matching_product)
            except IndexError as e:
                print("Product was not found, please try again...")
    if not selected_products:
        print("Please select some products before continuing the process. Please try again...")
        exit()


#
#CALCULATE TAX AND TOTALS
#
    subtotal = sum([float(p["price"]) for p in selected_products])
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    
    
    divider = "------------------"
    
         #
        # Turn output into single function with parameter
        #
    def recepit_details(message):
        print(divider)
        print(message)
    
    
    
           #
        # INFO DISPLAY / OUTPUT
        #
    
    recepit_details("MARGO'S GROCERY STORE")
    recepit_details("Web: www.margos.com")
    recepit_details("Phone: (216)-112-1357")
    recepit_details("Checkout time: " + human_friendly_timestamp(dt.datetime.now()))
    recepit_details("Selected Products: ")
    
    for p in selected_products:
        print(f"... {p['name']} {to_usd(p['price'])}")
    
    
    
    print(" ")
    print("SUBTOTAL: " + to_usd(subtotal))
    print("TAX: " + to_usd(tax))
    print("TOTAL: " + to_usd(calculate_total_price(subtotal,tax)))
    
    
    recepit_details(" ")
