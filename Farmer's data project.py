# Dictionary to store all farmers' data
farmers_data = {}

while True:
    print("\n--- Farmer Data Capturing Tool ---")
    print("1. Add a new farmer")
    print("2. View a farmer's details")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        # Input farmer details
        name = input("Enter farmer's name: ")
        age = input("Enter farmer's age: ")
        location = input("Enter farmer's location: ")
        crops = input("Enter crops they farm (comma separated): ").split(',')
        land_size = input("Enter size of land (in acres): ")
        
        # Store in dictionary
        farmers_data[name] = {
            'Age': age,
            'Location': location,
            'Crops': [crop.strip() for crop in crops],  # remove extra spaces
            'Land Size': land_size
        }
        print(f"Farmer {name} added successfully!")

    elif choice == '2':
        # View farmer's details
        search_name = input("Enter the name of the farmer to view: ")
        if search_name in farmers_data:
            print(f"\nDetails of {search_name}:")
            for key, value in farmers_data[search_name].items():
                print(f"{key}: {value}")
        else:
            print(f"No details found for farmer named {search_name}.")
    
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")