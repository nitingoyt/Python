import requests
from bs4 import BeautifulSoup

# response = requests.get('https://google.com')
# # print(response.status_code)
# # print(response.text)


# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://httpbin.org/post', data=payload)
# print(response.text)


# payload = {'key1': 'value1', 'key2': 'value'}
# response = requests.put('https://httpbin.org/put', data=payload)
# print(response.text)


# response = requests.delete('https://httpbin.org/delete')
# print(response.text)


url = "https://momperfume.in/checkouts/cn/Z2NwLWFzaWEtc291dGhlYXN0MTowMUo0RVdHSlBaVktaSDg4TTlLVzNEWFYwRQ"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)