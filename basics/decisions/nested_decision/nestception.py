# Beep is looking for his spare battery!
print("Where should I look for my spare battery?")
room = input()
if room == "in the bedroom":
    print("Where in the bedroom should I look?")
    bed_room = input()
    if bed_room == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")

elif room == "in the bathroom":
    print("Where in the bathroom should I look?")
    bath_room = input()
    if bath_room == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")

elif room == "in the lab":
    print("Where in the lab should I look?")
    lab_room = input()
    if lab_room == "on the table":
        print("Yes!I found my battery!")
    else:
        print("Found some tools but no battery")

else:
    print("I do not know where that is but I will keep looking")
