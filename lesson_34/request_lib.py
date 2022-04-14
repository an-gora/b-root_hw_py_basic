import requests

#через контекстый менеджер сохранить в файл
url = "https://ru.wikipedia.org/robots.txt"
resp = requests.get(url)
print(type(resp.text))

with open('file.txt', 'w') as file:
    file.write(resp.text)