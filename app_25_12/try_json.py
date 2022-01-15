import json
import pathlib

path_to_this_file = pathlib.Path(__file__)
path_to_parent = path_to_this_file.parent
path_to_json_with_users = path_to_parent.joinpath('list_of_users.json')

list_of_users = {
    'user_1': 'tom',
    'user_2': 'mary',
    'user_3': 'bob',
}

# with open('list_of_users.json', 'w') as file_for_users:
with open(path_to_json_with_users, 'w') as file_for_users:
    json.dump(list_of_users, file_for_users, indent=4)


def delete_user(user_list, id_to_delete):
    user_list.pop(id_to_delete)
    with open('list_of_users.json', 'w') as file_for_users_in_funct:
        json.dump(user_list, file_for_users_in_funct, indent=4)
    return user_list
# если мне не нужен return?


def add_user(user_list, key_value: dict):
    user_list.update(key_value)
    with open('list_of_users.json', 'w') as file_for_users_in_funct:
        json.dump(user_list, file_for_users_in_funct, indent=4)
    return user_list
# если мне не нужен return?


def print_json(file_name):
    with open('list_of_users.json', 'r') as file_object:
        users = json.load(file_object)
    for k, v in users.items():
        print(k, ':', v)


def main():
    print('list_of_users.json after creation')
    print_json('list_of_users.json')
    delete_user(list_of_users, 'user_1')
    add_user(list_of_users, {'user_4': 'tony'})
    print('list_of_users.json after deleting and adding')
    print_json('list_of_users.json')


if __name__ == '__main__':
    main()
