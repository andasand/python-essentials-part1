print("Hello, World!")

# the word print is a function name
'''
A function 
1. causes some effect
    a. send text to the terminal
    b. create a file
    c. draw an image
    d. play a sound
2. evaluate a value and return it as the function's result
    a. square root of a value
    b. length of a given text
'''

# where do functions come from?
# 1. from python itself --> built-in
# 2. from modules 
# 3. written by myself

# name of the function should be significant

# functions take in arguments (as many as necessary to perform their tasks)
# python functions strongly demand the prescence of a pair of parentheses - opening and closing ones
# arguments are placed inside the parentheses
# the print function above has taken a string value as data

# the print() function invocation
# 1. python checks if the name specified is legal --> it browses its internal dta in order to find an existing function of the name; if this search fails, python aborts the code
# 2. python checks if the function's requirements for the number of arguments allows you to invoke the function in this way
# 3. python leaves your code for a moment and jumps into the function you want to invoke
# 4. the function executes its code, causes the desired effect, evaluates the desired result and finishes its task
# 5. python returns to your code and resumes its execution

# what is the effect the print() function causes?
# python sends the resulting data to the output device

# what argument does print() expect?
# virtually all types of data (strings, characters, logical values, objects)

# what value does the print() function return?
# none.  only has an effect.

# key takeaways
# 1. print() function is a built-in function
# 2. the 69 built-in functions in python 3.8 (which is what the course is based on) are always available and don't have to be imported
# 3. to call a function (i.e. function invocation or function call), you need to use the function name followed by parentheses
# 4. python strings are delimited with quotes
# 5. computer programs are collections of instructions
# 6. an instruction is a command to perform a specific task when executed
# 7. in python strings, the backslash (\) is a special character which announces that the next character has a different meaning
# 8. positional arguments are the ones whose meaning is dictated by their position
# 9. keyword arguments are the ones whose meaning is not dictated by their position
# print("H","E","L","L","O", sep="-") 
#  strings "H","E","L","L","O" are positional arguments
#  sep="-" is keyword argument
# positional arguments follow keyword arguments