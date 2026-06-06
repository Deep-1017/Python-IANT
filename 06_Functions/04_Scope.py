y = 10

def myfunc():
  global x
  x = 300
  print(x)

# myfunc()
# print(y)
# print(x)



def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())