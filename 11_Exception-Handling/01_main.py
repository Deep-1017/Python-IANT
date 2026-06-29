n = 10

# print(n / 0)

try:
    res = n / 0
    print(res)
except ZeroDivisionError:
    print("Divison by zero is not possible.")
finally:
    print("This prints whether there is an error or not")

print("Hello")
print("How are you?")
print("I am learning python")