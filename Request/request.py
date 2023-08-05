import requests

params = {'v': 'lOfm04oLD1U'}    # запрос на ютюб

response = requests.get("https://www.youtube.com/watch", params=params)      # Получаем get запрос сайта

# print(response.status_code)    # Просмотреть статус страницы
# print(response.headers)        # служебная информация
# print(response.content)        # строка ввиде последовательности байтов
# print(response.text)           # HTML код ввиде текста