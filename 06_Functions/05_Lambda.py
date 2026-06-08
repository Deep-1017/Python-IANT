# sum = lambda x, y : x + y
# print(sum(10, 20))

# def sum(x, y):
#     print(x)
#     print(y)
#     return x + y

def myfunc(n):
  return lambda a : a * n

result = myfunc(3)

value = result(2)
print(value)