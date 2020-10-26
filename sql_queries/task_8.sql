SELECT last_name, count(last_name)
FROM employees
GROUP by last_name
ORDER BY count DESC, employees.last_name;