# lead beep to an adventure!
print("What type of adventure should Beep go into?")
adventure = input()
if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest!")
elif (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")