def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius and return the result."""
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit and return the result."""
    return (c * 9 / 5) + 32


def display_title():
    """Display the title of the program."""
    print("Temperature Conversion Program")


def display_menu():
    """Display the conversion options menu."""
    print("\nMENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")