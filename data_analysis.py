
CONN = "postgres://postgres:KiKNhAaC5btNsNf8@35.184.19.121:5432/SQL_Homework"
print("Database opened succesfully")

cur = CONN.cursor()
cur.execute('''SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary;''')

SELECT (emp_no, last_name, first_name, sex);
FROM employees
# FROM employees JOIN salaries ON employees.emp_no = salaries.emp_no;

# Data Analysis
# Once you have a complete database, do the following:

# List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
FROM employees JOIN salaries ON employees.emp_no = salaries.emp_no;

# List first name, last name, and hire date for employees who were hired in 1986.
SELECT first_name, last_name, hire_date
FROM employees2
WHERE hire_date BETWEEN '01/01/1986' and '01/01/1987';
# List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

# List the department of each employee with the following information: employee number, last name, first name, and department name.

# List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

# List all employees in the Sales department, including their employee number, last name, first name, and department name.

# List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

# In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.