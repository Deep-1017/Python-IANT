def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Age is set to:", age)
        
set(-5)