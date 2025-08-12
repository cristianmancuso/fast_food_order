fast_food = [
    {"name": "Hamburger", "price": 5.00},
    {"name": "Cheeseburger", "price": 6.00},
    {"name": "Fries", "price": 2.00},
    {"name": "Soda", "price": 1.00},
    {"name": "Water", "price": 1.00},
    {"name": "Iced Tea", "price": 2.00},
    {"name": "Chicken Nuggets", "price": 4.00},
    {"name": "Chicken Wings", "price": 7.00},
    {"name": "Pizza", "price": 8.00},
    {"name": "Hot Dog", "price": 3.00},
    {"name": "Sandwich", "price": 4.00},
]

# Welcome message
nombre = input("Hello, what is your name? ")   #ask the user their name

print(f"Hello, {nombre}! Welcome to the restaurant. We have the following menu:") #print the welcome message

print("----------------------------------")
for item in fast_food:  #loop in the menu

    print(f"{item['name']} - ${item['price']}") #print the menu

print("----------------------------------")

total = 0 #total of the order
choiseuser = [] #list of the order

# Loop through the menu
for i in fast_food: #loop in the menu

    print(f"Do you want to eat: {i['name']} - ${i['price']}?") #print the menu

    choise = input("Write yes or no: ").strip().lower() #ask the user if they want to eat the item
    while choise not in ('yes','no'): 
        print("Please type yes or no.") #if the user type something else
        choise = input("Write yes or no: ").strip().lower()#ask the user if they want to eat the item

    if choise == "yes": #ask the user how many they want
        howmany = input("How many do you want? ") #ask the user how many they want
        while howmany.isdigit() == False: #if the user type a letter
             print("Please type a number.") 
             howmany = input("How many do you want? ") #ask the user how many they want
        else:
            howmany = int(howmany) #convert the user input to an integer
            total += i["price"] * howmany #add the price of the item to the total
            choiseuser.append(f"{i['name']} x {howmany} = ${i['price'] * howmany}") #add the item to the list of the order
    else:
         print("Ok, let's see what else you want.") #if the user type no


print("----------------------------------")
print(f"Thank you for ordering in this restaurant, {nombre}. We hope you have a good day!") #print the thank you message
print("You have chosen:") #print the items that the user has chosen

for order in choiseuser: #loop in the list of the order

    print(" -", order) #print the item that the user has chosen
print(f"Your total is: ${total}") #print the total of the order
