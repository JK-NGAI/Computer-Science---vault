# Step 1: Create a set of car brands in Kenya
kenya_cars = {"Toyota", "Isuzu", "Nissan", "Mazda", "Volkswagen"}
print(sorted(kenya_cars))  # ['Isuzu', 'Mazda', 'Nissan', 'Toyota', 'Volkswagen']

# Step 2: Add 'Mobis' to the Kenya set
kenya_cars.add("Mobis")
print(sorted(kenya_cars))  # ['Isuzu', 'Mazda', 'Mobis', 'Nissan', 'Toyota', 'Volkswagen']

# Step 3: Create a set of car brands in Uganda
uganda_cars = {"FORD", "PEUGEOT", "FIAT", "Toyota", "Nissan"}
print(sorted(uganda_cars))  # ['FIAT', 'FORD', 'Nissan', 'PEUGEOT', 'Toyota']

# Step 4: Display car brands in Uganda but not in Kenya
uganda_not_kenya = uganda_cars - kenya_cars
print(sorted(uganda_not_kenya))  # ['FIAT', 'FORD', 'PEUGEOT']

# Step 5: Display car brands in Kenya but not in Uganda
kenya_not_uganda = kenya_cars - uganda_cars
print(sorted(kenya_not_uganda))  # ['Isuzu', 'Mazda', 'Mobis', 'Volkswagen']

# Step 6: Display car brands in both Kenya and Uganda
both_countries = kenya_cars & uganda_cars
print(sorted(both_countries))  # ['Nissan', 'Toyota']

# Step 7: Display all car brands in Kenya and Uganda
all_cars = kenya_cars | uganda_cars
print(sorted(all_cars))  # ['FIAT', 'FORD', 'Isuzu', 'Mazda', 'Mobis', 'Nissan', 'PEUGEOT', 'Toyota', 'Volkswagen']