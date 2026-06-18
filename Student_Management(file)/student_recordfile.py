import json
class Student:
    def __init__(self, StudentID, name, age, course):
        self.StudentID = StudentID
        self.name = name
        self.age = age
        self.course = course
students=[];
try:
    with open("students.text", "r") as file:
        for line in file:
            sid, name, age, course = line.strip().split(",")
            students.append({
                "StudentID": sid,
                "name": name,
                "age": int(age),
                "course": course
            })
    print("Data loaded from file")

except FileNotFoundError:
    print("No file found")

def showmenu():
    print("Manage Student Records\n");
    print("1)Add a student\n");
    print("2)View student\n");
    print("3)Search student\n");
    print("4)Update student details\n");
    print("5)Delete student\n")
    print("6)Save to file\n")
def addstudent():
    s = Student(
        input("enter the studentID\n"),
        input("enter the name of the student\n"),
        int(input("enter the age\n")),
        input("enter the course\n")
     )

    student = {
        "StudentID": s.StudentID,
        "name": s.name,
        "age": s.age,
        "course": s.course
    }

    students.append(student)
    print("Student added")
        
def viewstudent():
        if not students:
                print("no data entered yet\n");
        else:
            print("\nStudent List: ");
            for student in students:
                    print(f"ID: {student['StudentID']}")
                    print(f"Name: {student['name']}")
                    print(f"Age: {student['age']}")
                    print(f"Course: {student['course']}")
                    print()
def searchstudent():
     stID=input("enter the ID of the student to search\n");
     for student in students :
          if student["StudentID"]==stID:
               print(f"Student name={student['name']},student age={student['age']},student course={student['course']}");
               return student
     print("StudentID not found\n");
     return None
def updatestudent():
     student=searchstudent();
     if student is None:
        return
     print("what do u intend to update?\n");
     print("1.Name\n");
     print("2.Age\n");
     print("3.Course\n")
     n=int(input("enter your choice\n"));
     if n==1 :
          student["name"]= input("enter new name ");
          print("Name updated");
     elif n==2 :
          student["age"]=int(input("enter new age "));
          print("age updated");
     elif n==3 :
          student["course"]=input("enter new course ");
          print("Course updated")   
     else:
          print("Invalid choice");     
def deletestudent():
     student=searchstudent();
     if student:
        students.remove(student);
        print("Student deleted\n")
def savestudent():
     with open("students.text", "w") as file:
         for student in students:
             file.write(f"{student['StudentID']}, {student['name']} ,{student['age']},{student['course']}\n")
     print("Saved to file\n")     

     

     
while True:
      showmenu()
      c=int(input("enter your choice\n"));
      if c == 1:
        addstudent();
      elif c== 2:
        viewstudent();
      elif c== 3:
        searchstudent();
      elif c==4:
        updatestudent();
      elif c==5:
        deletestudent();
      elif c==6:
          savestudent();
      else :
        print("Exit");
        break

     
