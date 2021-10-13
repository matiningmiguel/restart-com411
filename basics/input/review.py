# Give the robot a name!
name = input("What should my name be?")
print(f"\'{name}\'... that's a cool name!")
# Give the robot an age!
print("How old am I?")
age = int(input())
print(f"\'{age}\' years old! I'll take that!")
# Give the robot a height!
print("How tall am I? (in meters)")
height = int(input())
print(f"I'm \'{height}\' cm tall... Got it!")
# Give the robot a weight!
print("How much do I weigh? (in kg)")
weight = int(input())
print(f"I weigh \'{weight}\' in kg... Okay!")
# Calculating the robot's BMI
bmi = weight / (height **2)
print(f"\nJudging by those numbers, my BMI should be {bmi}")
