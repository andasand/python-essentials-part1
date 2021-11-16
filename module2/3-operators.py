# operators and their priorities

# left sided binding (exception being exponent)
# hierarchy of priorities --> multiplication precedes addition
# the binding of the operator determines the order of computations
print (2 * 3 % 5)

# operators and parentheses
# subexpressions in parentheses are always calculated first
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# an expression is a combination of values (variables, operators, calls to functions) which evaluate to a value
print (1 + 2)

# operators are special symbols or  keywords which are able to operate on the values and perform (mathematical) operations
# x * y --> the * operator multiplies values x and y

# a unary operator is an operator with only one operand (e.g. -1 or + 3)
# a binary operator is an operator with two operands (e.g. 4 + 5 or 12 % 5)

# some operators act before others - the hierarchy of priorities
# unary + and - have the highest priorities
# **, *, /, % and then the lowest priority: binary + and -

# subexpressions in parentheses are always calculated first 
print (15 - 1 * (5 * (1 + 2)) == 0)

# exponentiation operator uses right-sided binding
print (2 ** 2 ** 3 == 256)
