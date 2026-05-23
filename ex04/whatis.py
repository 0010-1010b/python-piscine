import sys as sy

if len(sy.argv) <= 1:
    sy.exit()

if len(sy.argv) > 2:
    print(AssertionError("AssertionError: more than one argument is provided"))
    sy.exit()

try:    
    value = int(sy.argv[1])
except ValueError:
    print(AssertionError("AssertionError: argument is not an integer"))
    sy.exit()

if value > 9223372036854775807:
    print(AssertionError("AssertionError: integer is too big (sy.maxsize)"))
    sy.exit()

if value == 0:
    print("I'm Even.")
elif value % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")