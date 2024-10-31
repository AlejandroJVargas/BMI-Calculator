weight_in_kilograms = input("Put your weight in kilograms: ")
height_in_meters = input("Put your height in meters: ")

weight_in_kilograms = float(weight_in_kilograms)
height_in_meters = float(height_in_meters) / 100  # We make it in meters


BMI = weight_in_kilograms / (height_in_meters**2)

if BMI <= 18.5:
    print(f"Your BMI Weight is {BMI:.2f}. You are underweight")
elif BMI <= 24.9:
    print(f"Your BMI Weight is {BMI:.2f}. You are at normal weight")
elif BMI <= 29.9:
    print(f"Your BMI Weight is {BMI:.2f}. You are overweight")
else:
    print(f"Your BMI Weight is {BMI:.2f}. You are with obesity")
# print(f"Your BMI Weight is {BMI:.2f}")
