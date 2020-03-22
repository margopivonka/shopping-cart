import datetime as dt
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail 

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
EMAIL_ADDRESS = os.environ..get("EMAIL_ADDRESS", "OOPS, please set env var called 'EMAIL_ADDRESS'")




#TODO: make tax rate variable 
TAX_RATE = 0.06

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

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
#TIMESTAMP AND FORMATTING
#
checkout_time = dt.datetime.now()
formatted_time = checkout_time.strftime("%Y-%m-%d %H:%M")


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
# INFO DISPLAY / OUTPUT
#

print(divider)
print("MARGO'S GROCERY STORE") 
print(divider)
print(" ")
print("Web: www.margos.com")
print("Phone: (216)-112-1357")
print("Checkout time: " + formatted_time)
print(divider)
print(" ")
print("SELECTED PRODUCTS: ")
for p in selected_products:
        print(f"... {p['name']} {to_usd(p['price'])}")

print(divider)
print(" ")
print("SUBTOTAL: " + to_usd(subtotal))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(total))



#
#SEND EMAIL RECEIPT
#

print("Would you like a copy of your receipt?")
user_email = input("Please enter your email address, or type 'NO' to skip this step: ")

if user_email.upper() == "Y":
    print(f"Hello Superuser! Using your default email address {EMAIL_ADDRESS}")
    user_email = EMAIL_ADDRESS

if user_email.upper() in ["N", "NO", "N/A"]:
    print("You have selected not to receive a copy of your receipt via email")
elif "@" not in user_email:
    print("Please enter a valid email address")
else:
    print("Now sending receipt via email...")

    formatted_products = []
    for p in selected_products:
        formatted_product = p
        if not isinstance(formatted_product["price"], str):
            formatted_product["price"] = to_usd(p["price"])
        formatted_products.append(formatted_product)

receipt = {
    "subtotal_price_usd": to_usd(subtotal),
    "tax_price_usd": to_usd(tax),
    "total_price_usd": to_usd(total),
    "formatted_time": formatted_time,
    "products": formatted_products
}

client = SendGridAPIClient(SENDGRID_API_KEY)

message = Mail(from_email=user_email, to_emails=user_email)
message.template_id = SENDGRID_TEMPLATE_ID
message.dynamic_template_data = receipt

response = client.send(message)

if str(response.status_code) == "202":
    print("Email sent successfully!")
else:
    print("Sorry, something went wrong...")
    print(response.status_code)
    print(response.body)


print(" ")
print(divider)
print("THANKS, SEE YOU AGAIN")
print(divider)
print(" ")


# A grocery store name of your choice
# A grocery store phone number and/or website URL and/or address of choice
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)
# The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
# The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
# The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
# A friendly message thanking the customer and/or encouraging the customer to shop again