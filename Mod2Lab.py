# Student Achievment App
# Author: Dylan Barks
# This app accepts a student last name, first name, and GPA. 
# The students GPA will qualify them for either the Deans list, Honor Role or neither.
# The achievemnt of the student will be printed to the console.
# Type 'ZZZ' to stop entering students and exit program.

exit = "ZZZ"
while True: 
    lName = input("Enter student last name: ")
    
    if lName == exit:
        break
    fName = input("Enter student first name: ")
    gPA = float(input("Enter student GPA: "))
    
    if gPA >= 3.5:
        print(f"{fName} {lName} has made the Deans list!")
    elif gPA > 3.25: 
        print(f"{fName} {lName} has made the Honor Role.")
    else: 
        print(f"{gPA} does not make honors :(")
print("Exiting program")
