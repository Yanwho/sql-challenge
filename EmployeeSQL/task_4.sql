SELECT  dept_emp.emp_no, departments.dept_name, employees.last_name, employees.first_name
FROM employees JOIN dept_emp ON dept_emp.emp_no = employees.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no;