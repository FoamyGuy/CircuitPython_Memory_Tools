import json

import websocket

ws = websocket.WebSocket()
ws.connect("ws://localhost:8000")
data_obj = {"job": {"uuid": "sldjfksdlkufoiu", "module_name": "adafruit_mpr121",
                    "mpy_file": "https://blahblah.com/adafruit_mpr121.py"}}

data_str = json.dumps(data_obj)
print(data_str)
print("after load?")
print(json.loads(data_str))
ws.send(data_str)

ws.close()
