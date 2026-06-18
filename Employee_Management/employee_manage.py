import json
class Employee:
    def __init__(self, empID, name, dept, salary):
        self.empID = empID
        self.name = name
        self.dept = dept
        self.salary = salary
employees=[];        
def load_employees():
    try:
        with open("employee.json", "r") as file:
            data = json.load(file)
            for emp in data :
                e=Employee(
                    emp["empID"],
                    emp["name"],
                    emp["department"],
                    emp["salary"]

                )
                employees.append(e)
        print("Data loaded from JSON file\n")   
    except FileNotFoundError:
        print("No JSON file found")
  
def showmenu():
    print("Employement Payroll Management System\n");
    print("1)Add a employee\n");
    print("2)View Employee\n");
    print("3)Search Employee\n");
    print("4)Update employee details\n");
    print("5)Delete employee\n")
    print("6)Save to JSON file\n")
    print("7)Calculate gross salary\n")
    print("8)Department wise employee list\n")
    print("9)Calculate highest paid employee\n")
    print("10)Find total emp,avg , lowest and highest salary\n")
def add_employee():
    e = Employee(
        input("enter the employeeID\n"),
        input("enter the name of the employee\n"),
        input("enter the department\n"),
        int(input("enter the salary\n")),
     )

    employees.append(e)
    print("Employee added")
        
def view_employee():
        if not employees:
                print("no data entered yet\n");
        else:
            print("\n---Employee List---\n ");
            print("-------------------------------------------------------\n");
            print("ID\t\tName\t\tDepartment\t\tSalary\t\t\n");
            print("-------------------------------------------------------\n");
            for e in employees:
                    print(f"{e.empID}\t\t{e.name}\t\t{e.dept}\t\t{e.salary}\t\t\n");
            print("-------------------------------------------------------\n");
def search_employee():
     eID=input("enter the ID of the employee to search\n");
     for e in employees :
          if e.empID==eID:
              print("Employee found\n")
              print(f"ID:{e.empID}\t\tNAME:{e.name}\t\tDept:{e.dept}\t\tSalary:{e.salary}\t\t\n");
              return e
     print("employee ID not found\n");
     return None
def update_employee():
     e=search_employee();
     if employees is None:
        return
     print("what do u intend to update?\n");
     print("1.Name\n");
     print("2.Department\n");
     print("3.Salary\n")
     n=int(input("enter your choice\n"));
     if n==1 :
          e.name = input("enter new name ");
          print("Name updated");
     elif n==2 :
          e.dept=int(input("enter new department "));
          print("Department updated");
     elif n==3 :
          e.salary=input("enter new salary ");
          print("Salary updated")   
     else:
          print("Invalid choice");  
def delete_employee():
     e=search_employee();
     if employees is None:
        return
     if employees:
        employees.remove(e);
        print("Employee deleted\n")
def save_employee():
    data = []

    for e in employees:
        data.append({
            "empID": e.empID,
            "name": e.name,
            "department": e.dept,
            "salary": e.salary
        })

    with open("employee.json", "w") as file:
        json.dump(data, file, indent=4)

   
    print("\nSaved to json file\n")   
def calc_salary():
    e=search_employee()
    basic = e.salary;
    hra = basic * 0.20;
    bonus=basic * 0.10;
    g_sal= basic + hra + bonus  
    print(f"gross salary ={g_sal}"); 
def dept_emp():
    deptname=input("enter the department name\n")
    for e in employees:
        if e.dept==deptname:
            print(e.name);
def highpaid_emp():
    highest=employees[0];
    for e in employees:
        if e.salary>highest.salary:
            highest=e;
    print(highest.name);
    print(highest.salary);
def salary_report():
    if not employees:
        print("No employees found")
        return

    total_salary = 0
    highest = employees[0].salary
    lowest = employees[0].salary

    for e in employees:
        total_salary += e.salary

        if e.salary > highest:
            highest = e.salary

        if e.salary < lowest:
            lowest = e.salary

    report = {
        "Total Employees": len(employees),
        "Average Salary": total_salary / len(employees),
        "Highest Salary": highest,
        "Lowest Salary": lowest
    }

    print("\nSalary Report")
    print("----------------")
    for key, value in report.items():
        print(f"{key}: {value}")   
     

    
load_employees()
while True:
      
    showmenu()
    c=int(input("enter your choice\n"));
    if c == 1:
        add_employee();
    elif c== 2:
        view_employee();
    elif c==3:
        search_employee();
    elif c==4:
        update_employee();
    elif c==5:
        delete_employee();
    elif c==6:
          save_employee();
    elif c==7:
          calc_salary();
    elif c==8:
          dept_emp();
    elif c==9:
         highpaid_emp();
    elif c==10:
         salary_report();
          
    else :
        print("Exit");
        break

     
