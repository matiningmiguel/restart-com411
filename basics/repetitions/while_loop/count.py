# Beep must avoid some cables
print("How many live cables should I avoid?")
live_cables = int(input())
cables_avoided = 0
while cables_avoided < live_cables:
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print(f"Done! {cables_avoided} cables avoided")
