#hotel menu
menu = {
    "pizza": 80,
    "chicken tikka": 349,
    "margherita": 199,
    "cold coffee": 130,
    "café latte": 140,
    "masala chai": 40,
    "green tea": 60,
    "ginger tulsi tea": 50,
    "paneer tikka sandwich": 129,
    "veg grilled sandwich": 99,
    "chicken mayo sandwich": 149,
    "peppy paneer": 399
}

print("***** Welcome to Sagar Shop *****\n")

print("------ MENU ------")
for item, price in menu.items():
    print(f"{item.title()} : ₹{price}")

total_amount = 0

while True:
    item = input("\nEnter item name: ").lower()

    if item in menu:
        total_amount += menu[item]
        print(f"{item.title()} added to your order.")
    else:
        print("Sorry, this item is not available.")

    another = input("Do you want to add another item? (yes/no): ").lower()
    if another != "yes":
        break

print(f"\nTotal amount to pay: ₹{total_amount}")