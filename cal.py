basic_salary =0;da =0;hra =0;lta =0;gross_salary =0;bonus = 0;emp_exp=0;
fname = input("Enter First Name : ")
if fname == "":
    print("First name cannot be empty !")
    fname = input("Enter First Name : ")
lname = input("Enter Last Name : ")
if lname == "":
    print("Last name cannot be empty !")
    lname = input("Enter Last Name : ")
if fname or lname != "":
    Fullname = (fname +" "+lname)
desig = input("Enter Designation :")
emp_exp = int(input("Enter the experience of the employee : "))
basic_salary = float(input("Enter the salary : "))
da = float(15 * basic_salary) / 100.0
hra = float(20 * basic_salary) / 100.0
lta = float(10 * basic_salary) / 100.0
gross_salary = basic_salary + da + hra + lta
if (emp_exp >= 10):
    basic_salary = basic_salary + (basic_salary * 0.15)
    print(basic_salary)
elif (emp_exp == 5):
    basic_salary = basic_salary + (basic_salary * 0.10)
    print(basic_salary)
elif (emp_exp == 3):
    basic_salary = basic_salary + (basic_salary * 0.3)
    print(basic_salary)
else:
    basic_salary = basic_salary + 0
    print(basic_salary)