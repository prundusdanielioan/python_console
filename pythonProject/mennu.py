def option1():
    print("You selected option 1: Running function 1...")
    # Add your code here for option 1
    # Example:
    print("Function 1 executed!")

def option2():
    print("You selected option 2: Running function 2...")
    # Add your code here for option 2
    # Example:
    print("Function 2 executed!")

def option3():
    print("You selected option 3: Running function 3...")
    # Add your code here for option 3
    # Example:
    print("Function 3 executed!")

def main_menu():
    while True:
        # Display the menu options to the user
        print("\nMain Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")

        # Get user input
        choice = input("Enter your choice (1-4): ")

        # Check the user's choice and call the corresponding function
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("Exiting the program...")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the main menu function
if __name__ == "__main__":
    main_menu()
