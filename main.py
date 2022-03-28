import sqlite3

con = sqlite3.connect("employee.db")
cursor = con.cursor()

# sqlite_query = '''CREATE TABLE employee(
#                  id INT PRIMARY KEY,
#                  empcode INT NOT NULL,
#                  empname TEXT NOT NULL,
#                  emp_salary INT NOT NULL,
#                  designation TEXT NOT NULL);'''
# cursor.execute(sqlite_query)
def add():

    id = input("ID : ")
    empcode = input("Code : ")
    empname = input("Name : ")
    salary = int(input("Salary : "))
    designation = input("Enter Designation : ")

    cursor.execute("INSERT INTO employee VALUES(?,?,?,?,?)",(id,empcode,empname,salary,designation))
    print("INSERTED SUCCESSFULLY!")
    con.commit()

def view():
    sql_view = "Select * FROM employee"
    cursor.execute(sql_view)

    records = cursor.fetchall()

    for item in records:
        print(item)

    con.commit()

while(True):
    print('''
          1. Add Employee
          2. View Employee
          3. EXIT ''')
    choice = int(input("Select an option : "))

    functions =[add,view]
    a = functions[choice-1]()
    ch = input("\n Press enter to continue OR press N to discontinue!")
    if (ch == "n" or ch == "N"):
        break
    else:
        pass