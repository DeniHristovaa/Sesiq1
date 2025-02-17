class Employee:

    def __init__(self, i_num, fname, lname, work_experience, education_level, salary, age):
        self.i_num = i_num
        self.fname = fname
        self.lname = lname
        self.work_experience = work_experience
        self.education_level = education_level
        self.salary = salary
        self.age = age

    def display_info(self):
        print(f"{self.i_num}-{self.fname}-{self.lname}-{self.work_experience}-{self.education_level}-{self.salary}-{self.age}")

    def bonus(self):
        if self.education_level == "higher":
            bonus = 0.05 * self.salary
        elif self.education_level == "secondary":
            bonus = 0.02 * self.salary
        else:
            bonus = 0

        if self.work_experience > 0:
            bonus += (0.012 * self.salary) * self.work_experience

if __name__ == "__main__":
    employee_list = []

    n = int(input())
    for employee in range(n):
        i_num = input()
        fname = input()
        lname = input()
        work_experience = input()
        education_level = input()
        salary = input()
        age = input()
        employee = Employee(i_num, fname, lname, work_experience, education_level,salary,age)
        employee_list.append(employee)


def sort_employee(employee_list):
    sorted_employee_list = sorted(employee_list, key=lambda employee: employee.age)
    for employee in sorted_employee_list:
        employee.display_info()

def search_by_name(employee_list, fname, lname):
    hasEmployee = False
    for employee in employee_list:
        if employee.fname == fname and employee.lname == lname:
            employee.display_info()
            hasEmployee = True

    if hasEmployee == False:
        print("Not found!!!")

def print_by_education_experience(employee_list, education, experience):
    for employee in employee_list:
        if employee.education_level == education and employee.work_experience == experience:
            employee.display_info()

def remove_employee(employee_list, i_num):
    hasEmployee = False
    for employee in employee_list:
        if employee.i_num == i_num:
            employee_list.remove(employee)
            print("Informatio deleted!!!")
            hasEmployee = True

    if hasEmployee == False:
        print("Wrong i_num!!!")