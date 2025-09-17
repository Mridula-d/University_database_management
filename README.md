University Management System (OOP in Python)

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python through a simple **University Management System**.  
It includes classes for **Person, Student, Employee, and University** with inheritance, method overriding, and data management.  

---

## 🚀 Features
- **Person class** – Base class with common attributes.  
- **Student class** – Inherits from Person, stores roll number, branch, and email.  
- **Employee class** – Inherits from Person, stores employee details like ID, branch, subject, and salary.  
- **University class** – Manages courses, students, and employees.  

---

## 📌 Functionalities
- Add new students and employees.  
- Maintain records in dictionary-based tables.  
- Add new courses dynamically.  
- Retrieve student/employee lists by branch or ID.  

---

## 🛠️ Tech Stack
- **Language:** Python 3  

---

## ▶️ Example Usage
```python
if __name__ == "__main__":
    uni = University("Codegnan", ['PFS', 'JFS', 'DA', 'DS'])
    s1 = Student('Prerana', '4h2', 'PFS', 'prerana@gmail.com')
    
    print(uni.uni_name)
    print(uni.addStudent(s1))
    uni.totalStudents()
