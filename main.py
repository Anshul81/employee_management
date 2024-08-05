from employee import EmployeeManager

def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. List All Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter employee ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            salary = float(input("Enter salary: "))
            manager.add_employee(emp_id, first_name, last_name, salary)
        elif choice == '2':
            emp_id = input("Enter employee ID: ")
            manager.view_employee(emp_id)
        elif choice == '3':
            emp_id = input("Enter employee ID: ")
            first_name = input("Enter new first name (leave blank to skip): ")
            last_name = input("Enter new last name (leave blank to skip): ")
            salary = input("Enter new salary (leave blank to skip): ")
            salary = float(salary) if salary else None
            manager.update_employee(emp_id, first_name, last_name, salary)
        elif choice == '4':
            emp_id = input("Enter employee ID: ")
            manager.delete_employee(emp_id)
        elif choice == '5':
            manager.list_employees()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
