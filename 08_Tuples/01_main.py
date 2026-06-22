# Ordered Collection
# Immutable (Unchangeble)
# Allow Duplicates

number = (1, 2, 3, 4, 5)
# print(number[0])
# print(len(number))

fruits = ("mango",)
# print(type(fruits))

student_age = tuple((23, 24, 23, 21))
student_age_list = list(student_age)
print(type(student_age_list))

print("Before: ", student_age_list)

print("----------------------------------------")

student_age_list[2] = 100
print("After: ", student_age_list)

student_age = tuple(student_age_list)
print(student_age)