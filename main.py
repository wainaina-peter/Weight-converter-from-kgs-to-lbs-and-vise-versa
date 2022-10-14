#Weight converter from kgs to lbs and vise versa
weight = int(input("Enter your weight: "))
unit = input("(K)gs or (L)bs:")

if unit.upper() == "L":
    converted = weight * 0.45
    print("You are" + " " + str(converted) + " " + "Kilograms")
else:
    converted = round(weight/0.45, 2) # rounds off the quotient to 2.d.p
    print("You are" + " " + str(converted) + " " + "Pounds")