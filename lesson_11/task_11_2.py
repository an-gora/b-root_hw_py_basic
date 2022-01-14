# username = input('name')
# with open('user_info.txt', 'w') as file_object:
#     file_object.write(username)


with open('user_info.txt', 'r') as file_object:
    username = file_object.read()

print('hi ' + username)
