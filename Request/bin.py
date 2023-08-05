import requests

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

# response = requests.get("https://httpbin.org/headers", headers=headers)   # отправляем те данные, которые сайт будет получать
# print(response.text)


data = {
    "comments": "",
    "custemail": "lol@gmail.com",
    "custname": "Keka",
    "custtel": "24234265",
    "delivery": "",
    "size": "small",
    "topping": [
      "bacon",
      "cheese"
    ]
  }

response = requests.post('https://httpbin.org/post', data=data, headers=headers)
print(response.text)