# a literal is data whose values are determined by the literal itself.
# numbers can be integers or floats (contain fractional parts)

# integers
print(type(111111))
print(type(11_111_11))

# floats
print(type(111111.05))
print(type(11_111_11.05))

# scintific notation --> floats
print(type(3E8))
print(type(3.2e8))

# strings --> need quotes the way floats need points :-)
# escape character --> played by backslash --> \
print("I like \"oat meal\".")
# apostraphe instead of a quote --> requires consistency
print('I like "oat meal".')

# boolean values --> truthfulness --> boolean algebra by way of The Laws of Thought
# use of only two distinct values (True and False), denoted as 1 and 0
# programmers write programs.  programs ask questions.  python runs the program and provides answers.
# only 2 types of answers.  yes, this is true.  no, this is false.

# python is a binary reptile
print(True > False) # 1 > 0
print(True < False) # 1 < 0

# binary system is a system of numbers that employs 2 as the base
# a binary number is made up of 0s and 1s only
# octals and hexadecimal numeration systems employ 8 and 16 as their bases respectively

# None literal represents the abscence of a value
print(type(None))