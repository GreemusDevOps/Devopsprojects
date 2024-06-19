def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    Formula: (Fahrenheit - 32) * 5/9
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test the functions
celsius_temp = 30
fahrenheit_temp = 86

print("Celsius to Fahrenheit:")
print(f"{celsius_temp}°C = {celsius_to_fahrenheit(celsius_temp)}°F")

print("\nFahrenheit to Celsius:")
print(f"{fahrenheit_temp}°F = {fahrenheit_to_celsius(fahrenheit_temp)}°C")

