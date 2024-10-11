import json
import random

# Define the categories and products
products = {
    'Ice-cream': ["California Pistachio Ice Cream", "Mississippi Mud Ice Cream", "Snickers Ice Cream", "Bavarian Chocolate Ice Cream", "Belgian Bliss Ice Cream", "Mint Milk Chocolate Chips Ice Cream", "Gold Medal Ribbon Ice Cream", "Dutch Chocolate Ice Cream", "Three cheers chocolate Ice Cream", "Chocolate Mousse Royale Ice Cream", "Chocolate Almond Praline Ice Cream", "Caramel Milk Cake Ice Cream", "Cotton Candy Ice Cream", "Jello Mello Ice Cream", "Vanilla Ice Cream", "Butterscotch Ribbon Ice Cream", "Honey Nut Crunch Ice Cream", "Splish Splash Ice Cream", "Hop Scotch Butterscotch Ice Cream", "Roasted Californian Almond Ice Cream", "Pralines 'N Cream Ice Cream", "Roasted Coffee Creme Ice Cream", "Cookie Crumble 'N Cream", "Fresh Alphonso Mango Ice Cream", "Fresh Very Berry Strawberry Ice Cream", "Black Currant Ice Cream", "Banana 'N Strawberries Ice Cream", "Fruit Overload Ice Cream", "Shooting Star Ice Cream"],
    'Sundaes': [
"Alphonso Mango Fruit Cream Sundae", "Banana N Strawberry Fruit Cream Sundae", "Vanilla Fruit Cream Sundae", "Snickers Caramel Sundae", "Banana Royale", "Thunder Hot Fudge"],
    'Ice-cream Cakes': ["Vanilla Affair", "Chocolate Cheer", "Belgian Dream", "Bavarian Blast", "Nutella Slab"],
    'Shakes': ["Cotton Candy Milkshake", "Bavarian Chocolate Milkshake", "Fresh Alphonso Mango Milkshake", "Honey Nut Crunch Milkshake", "Mint Milk Chocolate Chips Milkshake"],
    'Brownie Swizzlers':["Choco Lava", " Vanilla Brownie"]
}

# Random price generation function
def generate_random_price(min_price, max_price):
    return f"₹{random.randint(min_price, max_price)}"

# Create a dictionary to hold the product data with prices
products_data = {}
# Assign random prices to products based on category
for category, items in products.items():
    products_data[category] = []
    for item in items:
        # Assign price range based on category
        if category == "Ice-cream":
            price = generate_random_price(90, 150)
        elif category == "Sundaes":
            price = generate_random_price(100, 250)
        elif category == "Ice-cream Cakes":
            price = generate_random_price(300, 500)
        elif category == "Shakes":
            price = generate_random_price(150, 300)
        elif category == "Brownie Swizzlers":
            price = generate_random_price(100, 200)
        
        # Construct the product dictionary
        product = {
            'name': item,
            'price': price,  # Random price assigned based on category
            'image': '/static/images/'+item.lower().replace(' ', '-') + '.jpeg'  # Generate image name
        }
        # Append the product to the respective category
        products_data[category].append(product)

# Write the data to a JSON file
with open('products_data.json', 'w') as json_file:
    json.dump(products_data, json_file, indent=4)

print("Product data generated successfully!")