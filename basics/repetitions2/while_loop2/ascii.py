# ascii
print("How many bars should be charged?")
bars_2_charge = int(input())
charged_bars = 0
while charged_bars < bars_2_charge:
    charged_bars = charged_bars + 1
    print(f"Charging: {'o' * charged_bars}")

print("The battery is fully charged")#
