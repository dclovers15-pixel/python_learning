


fruits = [
    {"name" : "apple", "price" : "5"},
    {"name" : "lemon", "price" : "3"},
    {"name" : "orange", "price" : "7"},
    {"name" : "mango", "price": "2"},
    { "name" : "pineapple", "price" : "1"},
    {"name" : "watermelon", "price" : "4"},
    ]
for fr in fruits :
    print (f"{fr['name']} price is : {fr['price']}")
names = {f["name"] for f in fruits}
cart =[]
while True:
    fruit_choice = input(" these are the fruits we have, which one do u want ?"
    "  enter done when ur finished ")
    
  
    if fruit_choice not in  names :
        print ("please choose the ones we have")
        continue
    if fruit_choice == "done":
        break
    cart.append(fruit_choice)
total_price = 0
for item in cart:
     for fruit in fruits:
         if item == fruit["name"]:
            total_price += int(fruit["frice"])