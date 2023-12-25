print("Welcome to the BMI Calculator")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height/100)**2
if bmi < 18.5:
    print(f"Your BMI is {round(bmi,2)}, you are underweight.")
elif  bmi < 25:
    print(f"Your BMI is {round(bmi,2)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi,2)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi,2)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi,2)}, you are clinically obese.")
    
    
