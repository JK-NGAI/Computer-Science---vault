# Student Records Management System for OUK

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*60)
    print("     OUK STUDENT RECORDS MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search Student by ID")
    print("4. Search Student by Name")
    print("5. Delete Student Record")
    print("6. Update Student Information")
    print("7. Display Statistics")
    print("8. Exit")
    print("="*60)

def get_student_details():
    """Capture student details from user input"""
    print("\n--- ENTER STUDENT DETAILS ---")
    
    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender (M/F): ")
    course = input("Enter Course/Program: ")
    year_of_study = input("Enter Year of Study (1-4): ")
    email = input("Enter Email Address: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Home Address: ")
    
    # Format student record as a string with comma separation
    student_record = f"{student_id},{full_name},{age},{gender},{course},{year_of_study},{email},{phone},{address}\n"
    
    return student_record

def add_student():
    """Add a new student to the file"""
    try:
        student_record = get_student_details()
        
        # Open file in append mode to add new student
        with open("ouk_students.txt", "a") as file:
            file.write(student_record)
        
        print("\n✅ Student record added successfully!")
        
    except Exception as e:
        print(f"\n❌ Error adding student: {e}")

def display_all_students():
    """Display all students from the file"""
    try:
        print("\n" + "="*100)
        print("                    ALL STUDENTS RECORDS")
        print("="*100)
        
        # Open file in read mode
        with open("ouk_students.txt", "r") as file:
            students = file.readlines()
        
        if not students:
            print("\n📁 No student records found.")
            return
        
        # Display header
        print(f"{'ID':<10} {'NAME':<20} {'AGE':<5} {'GENDER':<8} {'COURSE':<20} {'YEAR':<5} {'EMAIL':<25} {'PHONE':<15}")
        print("-"*100)
        
        # Display each student
        for student in students:
            details = student.strip().split(',')
            if len(details) >= 8:
                print(f"{details[0]:<10} {details[1]:<20} {details[2]:<5} {details[3]:<8} {details[4]:<20} {details[5]:<5} {details[6]:<25} {details[7]:<15}")
        
        print("="*100)
        print(f"Total Students: {len(students)}")
        
    except FileNotFoundError:
        print("\n📁 No student records found. Please add students first.")
    except Exception as e:
        print(f"\n❌ Error displaying students: {e}")

def search_student_by_id():
    """Search for a student by ID"""
    try:
        search_id = input("\nEnter Student ID to search: ")
        
        found = False
        with open("ouk_students.txt", "r") as file:
            for line in file:
                details = line.strip().split(',')
                if details[0] == search_id:
                    print("\n✅ STUDENT FOUND:")
                    print("-"*40)
                    print(f"Student ID: {details[0]}")
                    print(f"Full Name: {details[1]}")
                    print(f"Age: {details[2]}")
                    print(f"Gender: {details[3]}")
                    print(f"Course: {details[4]}")
                    print(f"Year of Study: {details[5]}")
                    print(f"Email: {details[6]}")
                    print(f"Phone: {details[7]}")
                    print(f"Address: {details[8]}")
                    found = True
                    break
        
        if not found:
            print(f"\n❌ Student with ID {search_id} not found.")
            
    except FileNotFoundError:
        print("\n📁 No student records found.")
    except Exception as e:
        print(f"\n❌ Error searching student: {e}")

def search_student_by_name():
    """Search for students by name (partial match)"""
    try:
        search_name = input("\nEnter student name to search: ").lower()
        
        found_students = []
        with open("ouk_students.txt", "r") as file:
            for line in file:
                details = line.strip().split(',')
                if search_name in details[1].lower():
                    found_students.append(details)
        
        if found_students:
            print(f"\n✅ Found {len(found_students)} student(s):")
            print("-"*60)
            for student in found_students:
                print(f"ID: {student[0]} | Name: {student[1]} | Course: {student[4]}")
        else:
            print(f"\n❌ No students found with name containing '{search_name}'.")
            
    except FileNotFoundError:
        print("\n📁 No student records found.")
    except Exception as e:
        print(f"\n❌ Error searching students: {e}")

def delete_student():
    """Delete a student record by ID"""
    try:
        delete_id = input("\nEnter Student ID to delete: ")
        
        # Read all students
        with open("ouk_students.txt", "r") as file:
            students = file.readlines()
        
        found = False
        # Write back all except the one to delete
        with open("ouk_students.txt", "w") as file:
            for student in students:
                if student.split(',')[0] != delete_id:
                    file.write(student)
                else:
                    found = True
        
        if found:
            print(f"\n✅ Student with ID {delete_id} deleted successfully!")
        else:
            print(f"\n❌ Student with ID {delete_id} not found.")
            
    except FileNotFoundError:
        print("\n📁 No student records found.")
    except Exception as e:
        print(f"\n❌ Error deleting student: {e}")

def update_student():
    """Update student information"""
    try:
        update_id = input("\nEnter Student ID to update: ")
        
        # Read all students
        with open("ouk_students.txt", "r") as file:
            students = file.readlines()
        
        found = False
        # Update the specific student
        with open("ouk_students.txt", "w") as file:
            for student in students:
                details = student.strip().split(',')
                if details[0] == update_id:
                    found = True
                    print("\nCurrent Student Details:")
                    print(f"Name: {details[1]}")
                    print(f"Course: {details[4]}")
                    print(f"Year: {details[5]}")
                    
                    print("\nEnter new details (press Enter to keep current):")
                    new_name = input(f"Full Name [{details[1]}]: ") or details[1]
                    new_age = input(f"Age [{details[2]}]: ") or details[2]
                    new_gender = input(f"Gender [{details[3]}]: ") or details[3]
                    new_course = input(f"Course [{details[4]}]: ") or details[4]
                    new_year = input(f"Year of Study [{details[5]}]: ") or details[5]
                    new_email = input(f"Email [{details[6]}]: ") or details[6]
                    new_phone = input(f"Phone [{details[7]}]: ") or details[7]
                    new_address = input(f"Address [{details[8]}]: ") or details[8]
                    
                    updated_record = f"{update_id},{new_name},{new_age},{new_gender},{new_course},{new_year},{new_email},{new_phone},{new_address}\n"
                    file.write(updated_record)
                    print("\n✅ Student record updated successfully!")
                else:
                    file.write(student)
        
        if not found:
            print(f"\n❌ Student with ID {update_id} not found.")
            
    except FileNotFoundError:
        print("\n📁 No student records found.")
    except Exception as e:
        print(f"\n❌ Error updating student: {e}")

def display_statistics():
    """Display statistics about students"""
    try:
        with open("ouk_students.txt", "r") as file:
            students = file.readlines()
        
        if not students:
            print("\n📁 No student records found.")
            return
        
        total_students = len(students)
        courses = {}
        genders = {'M': 0, 'F': 0}
        years = {}
        
        for student in students:
            details = student.strip().split(',')
            # Count by course
            course = details[4]
            courses[course] = courses.get(course, 0) + 1
            
            # Count by gender
            gender = details[3].upper()
            if gender in genders:
                genders[gender] += 1
            
            # Count by year
            year = details[5]
            years[year] = years.get(year, 0) + 1
        
        print("\n" + "="*50)
        print("          STUDENT STATISTICS")
        print("="*50)
        print(f"Total Students: {total_students}")
        
        print("\n📊 Students by Course:")
        for course, count in courses.items():
            print(f"   {course}: {count} student(s)")
        
        print("\n📊 Students by Gender:")
        print(f"   Male: {genders['M']}")
        print(f"   Female: {genders['F']}")
        
        print("\n📊 Students by Year:")
        for year in sorted(years.keys()):
            print(f"   Year {year}: {years[year]} student(s)")
        
        print("="*50)
        
    except FileNotFoundError:
        print("\n📁 No student records found. Please add students first.")
    except Exception as e:
        print(f"\n❌ Error displaying statistics: {e}")

def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            search_student_by_id()
        elif choice == '4':
            search_student_by_name()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            update_student()
        elif choice == '7':
            display_statistics()
        elif choice == '8':
            print("\n✅ Thank you for using OUK Student Records System!")
            print("   Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 8.")

# Run the program
if __name__ == "__main__":
    # Create initial file if it doesn't exist
    try:
        with open("ouk_students.txt", "x"):
            print("📁 New student records file created.")
    except FileExistsError:
        pass  # File already exists
    
    main()