# all CRUD functions 

from db_connection import get_db_connection

# ---------- CREATE ---------- 
def add_employee(name, department, salary):
    conn = get_db_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE ems")
  
    cursor.execute( 
        "INSERT INTO employees (name, department, salary) \
        VALUES (%s, %s, %s)", 
        (name, department, salary) 
    ) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Added employee: {name}")

# ---------- READ (all) ---------- 
def get_all_employees():
    conn = get_db_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE ems")
    
    cursor.execute("SELECT * FROM employees") 
    rows = cursor.fetchall()
   
    cursor.close() 
    conn.close() 
    return rows

# ---------- READ (one) ---------- 
def get_one_employee(employee_id):
    conn = get_db_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE ems")
    
    cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,)) 
    rows = cursor.fetchone()
    
    cursor.close() 
    conn.close() 
    return rows

# ---------- UPDATE ----------
def update_salary(employee_id, new_salary): 
    conn = get_db_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE ems")
  
    cursor.execute( 
        "UPDATE employees SET salary = %s WHERE id = %s", 
        (new_salary, employee_id) 
    ) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Updated employee {employee_id}'s salary to {new_salary}") 

# ---------- DELETE ---------- 
def delete_employee(employee_id): 
    conn = get_db_connection() 
    cursor = conn.cursor() 
  
    cursor.execute("USE ems")
    cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,)) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Deleted employee {employee_id}") 
