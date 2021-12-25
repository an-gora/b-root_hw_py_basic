# greetings = 'hello file world!'
#
# with open('greetings.txt', 'w') as file_object:
#     file_object.write(greetings)

with open('greetings.txt') as file_object:
    greetings = file_object.read()

print('whatsapp?' + greetings)
