import os
import time
import requests

TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
MESSAGE = os.environ.get('MESSAGE_TEXT', 'Автосообщение')

url_send = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
url_delete = f"https://api.telegram.org/bot{TOKEN}/deleteMessage"

# Отправляем сообщение
resp = requests.post(url_send, json={'chat_id': CHAT_ID, 'text': MESSAGE})
data = resp.json()

if not data.get('ok'):
    print("Ошибка отправки:", data)
else:
    msg_id = data['result']['message_id']
    print(f"Отправлено: message_id={msg_id}")

    # Ждём 15 минут (900 секунд)
    time.sleep(900)

    # Удаляем сообщение
    resp_del = requests.post(url_delete, json={'chat_id': CHAT_ID, 'message_id': msg_id})
    print("Удалено:", resp_del.json())
  
