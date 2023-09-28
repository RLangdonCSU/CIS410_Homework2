import conversion_module as cm

def main():
    """Main function to get user inputs and display the output."""
    cm.display_title()
    
    while True:
        cm.display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '3':  # Exit the program
            print("Goodbye!")
            break
        elif choice == '1' or choice == '2':
            temperature = int(input("Enter temperature: "))  # Assume the user will enter valid data
            
            if choice == '1':  # Fahrenheit to Celsius
                converted_temp = cm.fahrenheit_to_celsius(temperature)
                print(f"{temperature} Fahrenheit is {round(converted_temp)} Celsius.")
                
            elif choice == '2':  # Celsius to Fahrenheit
                converted_temp = cm.celsius_to_fahrenheit(temperature)
                print(f"{temperature} Celsius is {round(converted_temp)} Fahrenheit.")
        else:
            print("Invalid choice, please choose a valid option from the menu.")
        
        continue_program = input("Would you like to convert another temperature? (y/n): ")
        if continue_program.lower() != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
