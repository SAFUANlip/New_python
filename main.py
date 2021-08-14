import requests


API_link = "https://api.telegram.org/bot1731536279:AAFAJ2f6CyZfindrLVuXc7bRA8bXTo4HY7Y"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()  #-1 значит, что мы берём последний update

print(updates)

message = updates['result'][0]['message'] #берём сообщение из последнего update

chat_id = message["chat"]["id"]
text = message["text"]

sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Ciri {text}")