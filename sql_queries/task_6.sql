SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name 
FROM departments JOIN dept_emp ON departments.dept_no = dept_emp.dept_no
JOIN employees ON dept_emp.emp_no = employees.emp_no WHERE departments.dept_no = 'd007';