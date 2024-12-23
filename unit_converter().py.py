def unit_converter():
    print("Unit Converter")
    print("1. Temperature (Celsius to Fahrenheit)")
    print("2. Length (Kilometers to Miles)")
    print("3. Weight (Kilograms to Pounds)")

    choice = input("Choose a conversion (1/2/3): ").strip()

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == "2":
        kilometers = float(input("Enter distance in kilometers: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} km = {miles} miles")
    elif choice == "3":
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kg = {pounds} lbs")
    else:
        print("Invalid choice.")

unit_converter()

