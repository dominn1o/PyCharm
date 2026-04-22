import json

import requests

with open("isbnBookshop.json", "r", encoding='utf-8') as file:
    data = json.load(file)


# group all ids and isbns into a dictionary
data_length = len(data[2]['data'])
books = {}

for index in range(data_length):
    book_id = data[2]['data'][index]['id']
    book_isbn = data[2]['data'][index]['bookShopIsbn']
    books[book_id] = book_isbn

print(books)

#check all ids without an isbn
nullISBNs = []
for i in books:
    if books[i] == None:
        nullISBNs.append(i)

print(nullISBNs)

referer = {}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
           "Referer": "https://bookshop.org/",
           }
isbnNumber = '9780743262170'
url = f"https://bookshop.org/"

response = requests.get(url, headers=headers)
print(response)
print(response.content.decode())
print(response.cookies.get_dict())
print(response.status_code)
