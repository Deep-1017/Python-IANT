# entry point, imports & runs functions 

from employee_repository import ( 
    add_employee, 
    get_all_employees, 
    get_one_employee, 
    update_salary, 
    delete_employee 
) 

# add_employee("John", "IT", 25000.00)

print("\nAll employees:") 
for emp in get_all_employees(): 
    print(emp) 
    
  
# print("\nEmployee with id=1:") 
# print(get_one_employee(1)) 

# update_salary(1, 30000.00)

# delete_employee(3)