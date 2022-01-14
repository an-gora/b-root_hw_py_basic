# Write a script that creates a
# new output file called myfile.txt
# and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and
# reads and prints its contents. Run your two scripts from
# the system command line.


say_greetings = 'hello file world!'
with open('myfile.txt', 'w') as file_object:
    file_object.write(say_greetings)

with open('myfile.txt', 'r') as file_object:
    greetings = file_object.readline()

print(greetings)
