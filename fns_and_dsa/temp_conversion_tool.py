FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)
def convert_to_celsius(fahrenheit):
    celsius_temp = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius_temp
def convert_to_fahrenheit(celsius):
    fahrenheit_temp = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit_temp
temprature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if temprature == float or int:
    if unit.upper() == 'C':
        print(f"{temprature}°C is {convert_to_fahrenheit(temprature)}°F")
    elif unit.upper() == 'F':
        print(f"{temprature}°F is {convert_to_celsius(temprature)}°C")
else:
    print("You entered a wrong input. Please enter a numeric value.")
