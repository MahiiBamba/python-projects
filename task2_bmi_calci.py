# BMI Calculator (Beginner Level)

def main():
    print("BMI Calculator")
    print("==============")
    
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return
            
    except ValueError:
        print("Error: Please enter valid numbers for weight and height.")
        return
    
    
    bmi = weight / (height * height)
    
   
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    
    print("\nResults:")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
    
    
    if category == "Underweight":
        print("Consider consulting a healthcare provider about healthy weight gain strategies.")
    elif category == "Overweight" or category == "Obese":
        print("Consider consulting a healthcare provider about healthy weight management.")
    else:
        print("You are in a healthy weight range. Keep maintaining good habits!")

if __name__ == "__main__":
    main()