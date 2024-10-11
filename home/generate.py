import random
import pandas as pd

# Define possible answers for each question
answers = [1, 2, 3, 4]
flavors = ["California Pistachio Ice Cream", "Mississippi Mud Ice Cream", "Snickers Ice Cream", "Bavarian Chocolate Ice Cream", "Belgian Bliss Ice Cream", "Mint Milk Chocolate Chips Ice Cream", "Gold Medal Ribbon Ice Cream", "Dutch Chocolate Ice Cream", "Three cheers chocolate Ice Cream", "Chocolate Mousse Royale Ice Cream", "Chocolate Almond Praline Ice Cream", "Ferrero Moments Mousse Ice Cream", "Naughty Nutella Ice Cream", "Caramel Milk Cake Ice Cream", "Cotton Candy Ice Cream", "Jello Mello Ice Cream", "Vanilla Ice Cream", "Butterscotch Ribbon Ice Cream", "Honey Nut Crunch Ice Cream", "Splish Splash Ice Cream", "Hop Scotch Butterscotch Ice Cream", "Roasted Californian Almond Ice Cream", "Pralines 'N Cream Ice Cream", "Roasted Coffee Creme Ice Cream", "Cookie Crumble 'N Cream", "Brown Biscuit Boba Ice Cream", "Fresh Alphonso Mango Ice Cream", "Fresh Very Berry Strawberry Ice Cream", "Black Currant Ice Cream", "Banana 'N Strawberries Ice Cream", "Fruit Overload Ice Cream", "Shooting Star Ice Cream"]

# Generate random combinations of answers and assign random ice cream flavors
data = []
for _ in range(10000):  # Generate 1000 entries
    q1 = random.choice(answers)
    q2 = random.choice(answers)
    q3 = random.choice(answers)
    q4 = random.choice(answers)
    q5 = random.choice(answers)
    q6 = random.choice(answers)
    flavor = random.choice(flavors)
    
    data.append([q1, q2, q3, q4, q5, q6, flavor])

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Flavor'])

# Save as CSV
df.to_csv('ice_cream_quiz_dataset.csv', index=False)

print("Dataset generated successfully!")
