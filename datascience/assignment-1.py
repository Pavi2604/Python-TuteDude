employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 30, 'department': 'IT', 'salary': 60000}
}

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_employee():
    """Adds a new employee to the system."""
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Employee ID already exists. Please enter a unique ID.")
                continue
            
            name = input("Enter Employee Name: ")
            age = int(input("Enter Employee Age: "))
            department = input("Enter Employee Department: ")
            salary = float(input("Enter Employee Salary: "))
            
            employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
            print("Employee successfully added!")
            break
        except ValueError:
            print("Invalid input. Please enter the correct data type.")

def view_employees():
    """Displays all employees in the system."""
    if not employees:
        print("No employees available.")
        return
    
    print("\nEmployee Details:")
    print("ID\tName\tAge\tDepartment\tSalary")
    print("-" * 40)
    for emp_id, details in employees.items():
        print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t{details['salary']}")

def search_employee():
    """Searches for an employee by ID and displays their details."""
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print("\nEmployee Found:")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric Employee ID.")

if __name__ == "__main__":
    main_menu()
