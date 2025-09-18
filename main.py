class Person:  # parent class
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def show(self):
        return f"The Person name is {self.name} and age is {self.age}"


class Student(Person):  # inheritance
    def __init__(self, name: str, age: int, rollno: int, mailid: str, branch: str):
        super().__init__(name, age)
        self.rollno = rollno
        self.mailid = mailid
        self.branch = branch
        self.id = rollno  # use rollno as unique ID

    def show(self):
        return f"name: {self.name}, age: {self.age}, rollno: {self.rollno}, mail: {self.mailid}, branch: {self.branch}"


class Employee(Person):
    def __init__(self, name: str, age: int, emailid: str, subject: list[str], salary: float, department: str, emp_id: int):
        super().__init__(name, age)
        self.mailid = emailid
        self.subject = subject
        self.salary = salary
        self.department = department
        self.id = emp_id  # unique employee ID

    def show(self):
        print(super().show())
        return f"mail id: {self.mailid}, subject: {self.subject}, salary: {self.salary}, department: {self.department}"


class University:
    student_table = dict()
    employee_table = dict()

    def __init__(self, university_name: str, courses: list):
        self.university_name = university_name
        self.courses = courses

    def add_student(self, student_obj: Student):
        if student_obj.id not in University.student_table:
            University.student_table[student_obj.id] = [student_obj.name, student_obj.age, student_obj.rollno,
                                                        student_obj.mailid, student_obj.branch]
        else:
            return "student id already exists"

    def add_employee(self, employee_obj: Employee):
        if employee_obj.id not in University.employee_table:
            University.employee_table[employee_obj.id] = [employee_obj.name, employee_obj.age, employee_obj.mailid,
                                                          employee_obj.subject, employee_obj.salary,
                                                          employee_obj.department]
        else:
            return "employee id already exists"

    def total_students(self, branch: str = None):
        result = []
        if branch:
            for item in University.student_table.items():
                if University.student_table[item[0]][4] == branch:
                    result.append(f"student id: {item[0]}, details: {item[1]}")
        else:
            for item in University.student_table.items():
                result.append(f"student id: {item[0]}, details: {item[1]}")
        return "\n".join(result)

    def total_employees(self, department: str = None):
        result = []
        if department:
            for item in University.employee_table.items():
                if University.employee_table[item[0]][5] == department:
                    result.append(f"employee id: {item[0]}, details: {item[1]}")
        else:
            for item in University.employee_table.items():
                result.append(f"employee id: {item[0]}, details: {item[1]}")
        return "\n".join(result)

    def add_course(self, course_name: str):
        if course_name not in self.courses:
            self.courses.append(course_name)
            return f"{course_name} added successfully"
        else:
            return f"{course_name} already exists"


# main
if __name__ == "__main__":
    u = University("VIT", ["cse", "ece", "mech", "robotics"])
    s1 = Student("MRIDULA", 20, 4204, "MRI@gmail.com", "cse")
    u.add_student(s1)
    s2 = Student("LALIT", 21, 4205, "LAL@gmail.com", "ece")
    u.add_student(s2)
    s3 = Student("SUSHMA", 21, 4206, "SUS@gmail.com", "cse")
    u.add_student(s3)
    print(u.total_students(branch="cse"))
    print("************************************************************************************")
    print(u.total_students()) 
    #try to give choices and also add emploee details in main. ----->task
