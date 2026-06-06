# 🐍 Python – Conditionals Practice Questions

## Easy

**Q1.** Write a program to check whether a number entered by the user is positive, negative, or zero.

**Q2.** Take two numbers as input and print the greater one.

**Q3.** Write a program to check if a number is even or odd.

**Q4.** Ask the user for their age. If age is 18 or above, print `"You can vote."` otherwise print `"You cannot vote yet."`

**Q5.** Write a program that takes a character as input and checks if it is a vowel or a consonant.

**Q6.** Take three numbers and print the largest among them.

**Q7.** Write a program to check whether a given year is a leap year or not.
*(A year is a leap year if divisible by 4, but not by 100, except if divisible by 400)*

**Q8.** Ask the user to enter a number between 1–7 and print the corresponding day of the week.
*(1 → Monday, 2 → Tuesday, ... 7 → Sunday)*

**Q9.** Write a program to check if a number is divisible by both 3 and 5.

**Q10.** Take two numbers and an operator (`+`, `-`, `*`, `/`) as input and perform the corresponding operation using conditionals (simple calculator).

---

## Intermediate

**Q11.** Write a program that takes a student's marks (0–100) and prints the grade:
- 90–100 → `A`
- 75–89 → `B`
- 60–74 → `C`
- 40–59 → `D`
- Below 40 → `F`

**Q12.** Write a BMI calculator. Take weight (kg) and height (m) as input, calculate BMI, and classify it:
- Below 18.5 → Underweight
- 18.5–24.9 → Normal
- 25–29.9 → Overweight
- 30+ → Obese

**Q13.** Take three sides of a triangle as input. Check:
1. Whether it forms a valid triangle
2. If valid, whether it is Equilateral, Isosceles, or Scalene

**Q14.** Write a login system simulation. Store a hardcoded username and password. Ask the user for input and print `"Login Successful"` or `"Invalid Credentials"`. After 3 failed attempts, print `"Account Locked"`.

**Q15.** Write a program that takes a number and checks:
- Is it a perfect square?
- Is it a prime number?
- Is it a palindrome number?
Print all applicable properties.

**Q16.** A cinema hall has the following ticket pricing:
- Children (age < 12): ₹100
- Adults (12–59): ₹200
- Seniors (60+): ₹150
- On weekends, add 20% surcharge for all.

Take age and day (weekday/weekend) as input and print the ticket price.

**Q17.** Write a program to determine the quadrant of a point `(x, y)` in a 2D plane, or whether it lies on an axis or at the origin.

---

## Hard

**Q18.** Implement a simple number guessing game using only conditionals (no loops):
- The secret number is hardcoded (e.g., 42).
- The user enters 3 guesses.
- After each guess, tell them `"Too High"`, `"Too Low"`, or `"Correct!"`.
- Use only `if/elif/else` (no loops).

**Q19.** Write a program to determine the type of a number:
- Is it Armstrong? *(e.g., 153 = 1³ + 5³ + 3³)*
- Is it Perfect? *(sum of divisors equals the number, e.g., 6 = 1+2+3)*
- Is it Prime?
- Is it Fibonacci?

**Q20.** You are building a shipping cost calculator:
- Weight ≤ 1 kg → ₹50
- 1–5 kg → ₹50 + ₹30 per kg above 1 kg
- 5–20 kg → ₹170 + ₹20 per kg above 5 kg
- Above 20 kg → ₹470 + ₹15 per kg above 20 kg
- If destination is international, add 40% extra.
- If the user is a premium member, give 10% discount at the end.

Take weight, destination (`domestic`/`international`), and membership (`yes`/`no`) as input and print the final cost.
