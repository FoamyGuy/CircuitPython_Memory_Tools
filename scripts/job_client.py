import json
import traceback

import websocket

from scripts.on_device_ram_check import get_ram_size

ws = websocket.WebSocket()
ws.connect("ws://localhost:8000")
#ws.send("Hello world different?")

try:
    while True:
        data = ws.recv()
        if data:
            #print(data)
            #print(type(data))
            try:
                data_obj = json.loads(data)
                #print(data_obj)
                if "job" in data_obj:
                    ram_size = get_ram_size(data_obj["job"]["module_name"].encode(), '/dev/ttyACM0')
                    #print(data_obj)
                    if ram_size:
                        ws.send(json.dumps({"ram_size": ram_size}))
            except ValueError as e:
                #print(e)
                #traceback.print_exc()
                pass

except KeyboardInterrupt:
    pass
ws.close()
