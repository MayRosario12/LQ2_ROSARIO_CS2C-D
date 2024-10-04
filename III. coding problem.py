  #Function to get user input
def get_user_info():
    # Prompt for input
    name = input("Ayam Mariano: ")
    address = input("Paduros, Burgos Ilocos Sur: ")
    age = int(input("22: "))
    class_role = input(" Student): ")
    course = input(" (BSCS): ")

    # Detect the course using a conditional statement
    if course == "BSCS":
        process_class_role(name, age, class_role, course)
    elif course == "BSM":
        process_class_role(name, age, class_role, course)
    elif course == "BAEL":
        process_class_role(name, age, class_role, course)
    else:
        print("Invalid course. Please enter a valid course.")
    
# Function to process class role and loop to print the name based on age
def process_class_role(name, age, class_role, course):
    # Check for valid class role
    if class_role == "Officer":
        print(f"Course: {course} | Role: Officer")
    elif class_role == "Student":
        print(f"Course: {course} | Role: Student")
    elif class_role == "Teacher":
        print(f"Course: {course} | Role: Teacher")
    else:
        print(f"Course: {course} | Role: Undefined (default to 'Student')")
        class_role = "Student"
    
    # Loop to print the user's name based on 1/4th of the age
    iterations = age // 4
    for i in range(iterations):
        print(f"{i + 1}: {name}")

# Call the function to run the program
get_user_info()



