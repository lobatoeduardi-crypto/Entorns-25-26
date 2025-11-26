import requests


url1 = "https://api.chucknorris.io/jokes/categories"
response = requests.get(url1)


if response.status_code == 200:
    print("✅ Èxit!")
    print(response.text)
else:
    print(f"❌ Error {response.status_code}")
