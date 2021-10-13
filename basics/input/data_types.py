# Beep wishes to learn more about you!
print("What is your name?")
name = input()
print("What is your age?")
age = int(input())
print("What is your height?")
height = float(input())
print("What is your weight?")
weight = float(input())
#calculate bmi
bmi = weight / (height **2)
print(f"{name} you are {age} years old and your bmi is {bmi}")