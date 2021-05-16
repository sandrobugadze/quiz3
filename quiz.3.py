import requests
import json
import sqlite3

url = "https://api.vatcomply.com/currencies"
davaleba = requests.get(url)
# print(davaleba.text)
# print(davaleba.headers)
# print(davaleba.status_code)


davaleba2 = davaleba.json()
# with open("jemali.json","w") as jemali:
#     json.dump(davaleba2,jemali,indent=4)


# for x in davaleba2:
#     print(davaleba2[x]["name"]+", "+davaleba2[x]["symbol"])

kavshiri = sqlite3.connect("folder.sqlite")
cursor = kavshiri.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS lol
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50),
                symbol VARCHAR(255))
''')

rito = []

for y in davaleba2:
    name = davaleba2[y]["name"]
    symbol = davaleba2[y]["symbol"]
    mini_rito = [name,symbol]
    rito.append(mini_rito)

cursor.executemany('''INSERT INTO lol (name,symbol)
                      VALUES (?,?)''',rito)

kavshiri.commit()
kavshiri.close()

