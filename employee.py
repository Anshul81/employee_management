class Employee:
    def __init__(self, emp_id, first_name, last_name, salary):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def annual_salary(self):
        return self.salary * 12


class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, first_name, last_name, salary):
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
            return
        self.employees[emp_id] = Employee(emp_id, first_name, last_name, salary)
        print(f"Added employee: {self.employees[emp_id].full_name()}")

    def view_employee(self, emp_id):
        employee = self.employees.get(emp_id)
        if not employee:
            print(f"No employee found with ID {emp_id}")
            return
        print(f"ID: {employee.emp_id}, Name: {employee.full_name()}, Salary: {employee.salary}, Annual Salary: {employee.annual_salary()}")

    def delete_employee(self, emp_id):
        if emp_id not in self.employees:
            print(f"No employee found with ID {emp_id}")
            return
        removed_employee = self.employees.pop(emp_id)
        print(f"Deleted employee: {removed_employee.full_name()}")

    def update_employee(self, emp_id, first_name=None, last_name=None, salary=None):
        employee = self.employees.get(emp_id)
        if not employee:
            print(f"No employee found with ID {emp_id}")
            return
        if first_name:
            employee.first_name = first_name
        if last_name:
            employee.last_name = last_name
        if salary:
            employee.salary = salary
        print(f"Updated employee: {employee.full_name()}")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        for emp_id, employee in self.employees.items():
            print(f"ID: {emp_id}, Name: {employee.full_name()}, Salary: {employee.salary}")
