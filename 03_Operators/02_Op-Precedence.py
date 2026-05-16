# Precedence Order  &  Associativity Rule
# ()    -> Left to Right
# * / % -> L to R
# + -   -> L to R


eq = (10 + 2) - 5 * 7 / 2 + (12 * 4 - 6)
print(eq)


# 12 - 5 * 7 / 2 + (12 * 4 - 6)
# 12 - 5 * 7 / 2 + 42
# 12 - 35 / 2 + 42
# 12 - 17.5 + 42
# -5.5 + 42
# 36.5