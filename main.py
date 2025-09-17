# person class
class Person:
    # initilization constaractor, it take name as partrameter
    def __init__(self, name:str):
        self.name = name

    #person class display details  method
    def display_details(self):
        return f"The Name is {self.name}"


# Student Class
class Student(Person):
    # Student class take name, roll number, branch, and email as parameters
    def __init__(self, name:str, roll_no:str, branch:str, email:str=None):
        super().__init__(name)
        self.roll_no = roll_no
        self.branch = branch
        self.email = email
    
    # Student class dipaly details method
    def display_details(self):
        print(super().display_details())
        return f"The student roll number is {self.roll_no} and branch is {self.branch}"
        

# Employee class
class Employee(Person):
    # Employee class take name, employee id, branch,subject and salary as parameters
    def __init__(self, name, emp_id, branch, subject, salary):
        super().__init__(name)
        self.emp_id = emp_id
        self.branch = branch
        self.subject = subject
        self.salary = salary
    
    # Employee class display details method
    def display_details(self):
        print(super().display_details())
        return f"The employee id is {self.emp_id}, and selected branch is {self.branch} and subject is {self.subject}"
    

# university class
class University:
    def __init__(self, university_name:str, courses:list[str]):
        self.uni_name = university_name
        self.courses = courses
        self.students_table = dict()
        self.emp_table = dict()

        pass

    # add student method take student object as parameter
    def addStudent(self, std_obj):
        if std_obj.roll_no not in self.students_table:
            self.students_table[std_obj.roll_no] = [std_obj.name, std_obj.branch, std_obj.email]
            return f"Successfully {std_obj.name} added to univirsity"
        else:
            return "Student id already existed"

        

    # add employee method take employe onject as parameter
    def addEmployee(self,emp_obj):
        if emp_obj.emp_id not in self.emp_table:
            self.emp_table[emp_obj.emp_id] = [emp_obj.name, emp_obj.branch, emp_obj.subject, emp_obj.salary]
            return f"Successfully {emp_obj.name} added to university"
        else:
            return "Employee id already existed"

        

    # add course to current course list
    def addCourse(self, new_course):
        self.courses.append(new_course)
        

    # total student list, (based on requirement it returns)
    def totalStudents(self, search_branch:str = None):
        if search_branch:
            for item in self.students_table.items():
                if item[1][1] == search_branch:
                    print(item)
        

    # total employee list, (based on requirement it returns)
    def totalEmployes(self):
        for item in self.emp_table.items():
            print(item)


# main function
if __name__ == "__main__":
    uni = University("Codegnan",['PFS', 'JFS', 'DA', 'DS'])
    s1 = Student('prerana', '4h2', 'PFS', 'prerana@gmail.com')
    print(uni.uni_name)
    print(uni.addStudent(s1))
    print(uni.totalStudents())