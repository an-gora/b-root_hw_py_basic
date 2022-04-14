import json
import requests


# см в лмс пример файлом такой был

def get_data(base_url, params):
    reqt = requests.get(base_url, params)
    return reqt.json()


def save_to_json(data):
    with open('r_comments.json', 'w') as file:
        json.dump(data['data'], file, indent=4)


def main():
    url = 'https://api.pushshift.io/reddit/comment/search/'
    params = {'subreddit': 'ClashMini', 'sort': 'desc', 'sort_type': 'created_utc'}
    data = get_data(base_url=url, params=params)
    save_to_json(data=data)


if __name__ == '__main__':
    main()
