def showcart():
    print("Items in cart:")
    for i in cart:
        print(f"{i}. {items[i-1]} - {prices[i-1]}")

def addtocart():
    print("Items in store:")
    for i in range(len(items)):
        print(f"{i+1}. {items[i]} - {prices[i]}")
    item = int(input("Enter the item number to add to cart: "))
    cart.append(item)

def removefromcart():
    showcart()
    item = int(input("Enter the item number to remove from cart: "))
    cart.remove(item)

def checkout():
    total = 0
    showcart()
    for i in cart:
        total += prices[i-1]
    print("Total Amount: ", total)

items=["apple","banana","cherry","grapes","mango"]
prices=[30,40,50,60,70]
cart=[]

while True:
    print("1. Add to cart")
    print("2. Remove from cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Quit")
    option = int(input("Enter your option: "))
    if option == 1:
        addtocart()
    elif option == 2:
        removefromcart()
    elif option == 3:
        showcart()
    elif option == 4:
        checkout()
    elif option == 5:
        break
    else:
        print("Invalid Option")