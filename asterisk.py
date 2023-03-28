"""
Outer loop iteration 1 (x = 0):

Inner loop iteration 1 (y = 0):
*  # prints an asterisk followed by a space, with no newline character

Inner loop iteration 2 (y = 1):
*  # prints another asterisk followed by a space, with no newline character

Inner loop iteration 3 (y = 2):
*  # prints another asterisk followed by a space, with no newline character

Inner loop iteration 4 (y = 3):
*  # prints another asterisk followed by a space, with no newline character

Inner loop iteration 5 (y = 4):
*  # prints another asterisk followed by a space, with no newline character

End of inner loop

Print a newline character to move to the next line:
# prints a newline character to the console

"""
#Square pattern
for x in range(5):
    for y in range(5):
        print("*",end=" ")
    print()

#Ascending triangle
# for x in range(5):
#     for y in range(x+1):
#         print("*",end=" ")
#     print()

#Descending triangle
# for x in range(5):
#     for y in range(5-x):
#         print("*",end=" ")
#     print()


