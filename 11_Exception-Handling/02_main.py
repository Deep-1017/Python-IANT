try:
    num = int("abc")
    print(num)
except ValueError as e:
    print("Value is not valid", e)