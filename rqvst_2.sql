1 SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name FROM employees JOIN departments ON employees.department_id = departments.department_id;
2 SELECT employees.first_name, employees.last_name, departments.depart_name, locations.city, locations.state_province FROM employees JOIN departments
ON employees.department_id = departments.department_id  JOIN locations ON departments.location_id = locations.location_id;
3 SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name FROM employees JOIN departments
ON employees.department_id = departments.department_id  JOIN locations ON departments.location_id = locations.location_id AND employees.department_id IN(80,40);
4 SELECT employees.first_name, employees.last_name, departments.department_id, departments.department_name FROM employees RIGHT JOIN departments
ON employees.department_id = departments.department_id;
5
6 SELECT job_title, first_name ||' '|| last_name AS Employee_name, max_salary-salary AS salary_difference FROM employees
JOIN jobs;
7 SELECT job_title, AVG(salary) FROM employees LEFT JOIN jobs GROUP BY job_title;
8 SELECT first_name||' '||last_name AS Employee_name, salary FROM employees
JOIN departments USING (department_id) JOIN  locations USING (location_id) WHERE  city = 'London';
9 SELECT departments.depart_name,employees.* FROM departments JOIN
(SELECT count(employee_id), department_id
FROM employees GROUP BY department_id) employees USING (department_id);
