# Beep wants to know about the best place to go food shopping
print("Where should I go shopping?")
shop = input()
if (shop == "Lidl") or (shop == "Aldi"):
    print(f"According to my calculations {shop} is the best for cheap deals!")
else:
    print("I've never heard of that shop before!")

print(f"\nWhat is the best aisle to shop in {shop}?")
aisle = input()
if aisle == "in the middle":
    print("There are some good deals here, the best!")
elif aisle == "on the outskirts":
    print("All the food here looks delicious!")
else:
    print("Does that aisle really exist?")

print("\nWhat were the other shops called?")
shop2 = input()
if (shop2 == "Waitrose") or (shop == "Asda"):
    print("That shop sounds expensive!")
else:
    print("Are you joking around with me?")
