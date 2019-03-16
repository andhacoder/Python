weight = input("Enter the weight ")
unit = input("Enter L for lbs and K for kg ")
if unit.upper() == "L":
    converted= int(weight)*0.45
    print(f"Your weight in kg is {converted} kg")
elif unit.upper()=="K":
    converted = int(weight)/0.45
    print(f"Your weight in lbs is {converted} lbs")
else:
    print("Enter a correct value")
