# 🐍 Python – Functions Practice Questions

## Easy

**Q1.** Write a function `greet(name)` that takes a name as an argument and prints `"Hello, <name>! Welcome."`.

**Q2.** Write a function `is_even(n)` that returns `True` if `n` is even, else returns `False`.

**Q3.** Write a function `area_of_rectangle(length, width)` that returns the area of a rectangle.

**Q4.** Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit and returns the result.
*(Formula: F = (C × 9/5) + 32)*

**Q5.** Write a function `max_of_three(a, b, c)` that returns the largest of three numbers without using the built-in `max()`.

**Q6.** Write a function `is_palindrome(s)` that returns `True` if the string is a palindrome, else `False`.

**Q7.** Write a function `factorial(n)` that returns the factorial of `n` using a loop.

**Q8.** Write a function `count_vowels(s)` that takes a string and returns the count of vowels in it.

**Q9.** Write a function `sum_list(numbers)` that takes a list of numbers and returns their sum without using `sum()`.

**Q10.** Write a function with a **default parameter**: `power(base, exp=2)` that returns `base` raised to `exp`. Call it both with and without the second argument.

---

## Intermediate

**Q11.** Write a function `is_prime(n)` that returns `True` if `n` is prime, else `False`. Then write another function `primes_in_range(start, end)` that uses `is_prime()` to return a list of all primes in that range.

**Q12.** Write a function `flatten(nested_list)` that takes a nested list and returns a flat list.
*(Example: `[[1, 2], [3, [4, 5]]]` → `[1, 2, 3, 4, 5]`)*

**Q13.** Write a function `word_frequency(sentence)` that takes a sentence and returns a dictionary with each word as a key and its frequency as the value.

**Q14.** Write a function using `*args` called `total(*numbers)` that accepts any number of arguments and returns their total.

**Q15.** Write a function using `**kwargs` called `display_info(**details)` that accepts any number of keyword arguments and prints each key-value pair on a new line.

**Q16.** Write a function `remove_duplicates(lst)` that takes a list and returns a new list with duplicates removed while maintaining the original order. *(Do not use `set()` directly on the whole list)*

**Q17.** Write a higher-order function `apply_twice(func, value)` that applies `func` to `value` twice and returns the result.
*(Example: if `func` doubles a number, `apply_twice(double, 3)` → 12)*

**Q18.** Write a function `calculator(a, b, operation)` where `operation` is a string (`"add"`, `"subtract"`, `"multiply"`, `"divide"`). Use a dictionary mapping strings to lambda functions to perform the operation.

---

## Hard

**Q19.** Write a **recursive** function `fibonacci(n)` that returns the `n`th Fibonacci number.
Then improve it using **memoization** (store already-computed values in a dictionary) and compare the speed for large `n` like 35.

**Q20.** Write a function `merge_sort(lst)` that implements the Merge Sort algorithm using recursion and returns the sorted list.

**Q21.** *(Bonus)* Write a function `make_counter()` that uses a **closure** to return an inner function. Each time the inner function is called, it should return the next count (starting from 1), without using any global variable.

```python
counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```
