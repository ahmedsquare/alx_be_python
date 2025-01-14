FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit- 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    # Validate unit input
    while True:
        unit =  input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ["C", "F"]:
            break
        else:
            print("Invalid temperature. Please enter a (C/F).")

    if unit == "C":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F ")
    elif unit == "F":
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C ")
if __name__ == "__main__":
    main()