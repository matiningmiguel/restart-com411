# What type of book cover is this?
print("What type of cover does the book have, hard or soft?")
cover = input()
if cover == "hard":
    print("Books with hard covers can be more expensive!")
elif cover == "soft":
    print("Is the book perfect bound?")
perfect_bound = input()
if perfect_bound == "yes":
    print("Soft cover, perfect bound books are very popular!")
else:
    print("Soft cover coils or stitches are great for short books.")

