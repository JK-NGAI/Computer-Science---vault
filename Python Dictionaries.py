# Create an empty dictionary
student_counties = {}

# Display the dictionary
print(student_counties)
# Create the empty dictionary
student_counties = {}

# Add students and their counties
student_counties["Mathew"] = "Busia"
student_counties["Caleb"] = "Mombasa"
student_counties["Malik"] = "Nakuru"
student_counties["Sarah"] = "Kajiado"

# Display the dictionary
print(student_counties)
# Given dictionary
student_counties = {"Mathew":"Busia", "Caleb":"Mombasa", "malik":"Nakuru", "Sarah":"Kajiado"}

# Change Caleb's county
student_counties["Caleb"] = "Nyandarua"

# Display the dictionary
print(student_counties)
# First dictionary
student_counties = {"Mathew":"Busia", "Caleb":"Nyandarua", "malik":"Nakuru", "Sarah":"Kajiado"}

# Additional students dictionary
additional_students = {"Malik":"Bungoma", "Martin":"Kisumu", "Kyalo":"Machakos", "Mwaniki":"Kitui", "Wafula":"Kakamega"}

# Add elements from additional_students to student_counties
student_counties.update(additional_students)

# Display the updated dictionary
print(student_counties)
# Given dictionary
student_counties = {
    'Mathew': 'Busia',
    'Caleb': 'Nyandarua',
    'malik': 'Nakuru',
    'Sarah': 'Kajiado',
    'Malik': 'Bungoma',
    'Martin': 'Kisumu',
    'Kyalo': 'Machakos',
    'Mwaniki': 'Kitui',
    'Wafula': 'Kakamega'
}

# Display the county Sarah is from
print(student_counties["Sarah"])
# Given dictionary
student_counties = {
    'Mathew': 'Busia',
    'Caleb': 'Nyandarua',
    'malik': 'Nakuru',
    'Sarah': 'Kajiado',
    'Malik': 'Bungoma',
    'Martin': 'Kisumu',
    'Kyalo': 'Machakos',
    'Mwaniki': 'Kitui',
    'Wafula': 'Kakamega'
}

# Display all counties
print(student_counties.values())
# Given dictionary
student_counties = {
    'Mathew': 'Busia',
    'Caleb': 'Nyandarua',
    'malik': 'Nakuru',
    'Sarah': 'Kajiado',
    'Malik': 'Bungoma',
    'Martin': 'Kisumu',
    'Kyalo': 'Machakos',
    'Mwaniki': 'Kitui',
    'Wafula': 'Kakamega'
}

# Display all student names
print(student_counties.keys())
# Given dictionary
remaining_stud = {
    'Mathew': 'Busia',
    'Caleb': 'Nyandarua',
    'malik': 'Nakuru',
    'Sarah': 'Kajiado',
    'Martin': 'Kisumu',
    'Kyalo': 'Machakos',
    'Mwaniki': 'Kitui',
    'Wafula': 'Kakamega'
}

# Display the value for key "Mwaniki"
print(remaining_stud["Mwaniki"])