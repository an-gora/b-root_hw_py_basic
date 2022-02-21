import requests

#через контекстый менеджер сохранить в файл
url = "https://ru.wikipedia.org/robots.txt"

requests.get(url)
resp = requests.get(url)
print(resp.text)