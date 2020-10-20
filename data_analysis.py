
CONN = "postgres://postgres:KiKNhAaC5btNsNf8@35.184.19.121:5432/SQL_Homework"
print("Database opened succesfully")

cur = con.cursor()
cur.execute('''SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary;''')

# SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
# FROM employees JOIN salaries ON employees.emp_no = salaries.emp_no;