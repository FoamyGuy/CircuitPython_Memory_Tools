import json

import serial


def get_ram_size(module_name, device_path):

    def try_read_ram_size(verbose=False):
        if ser.in_waiting:
            read = ser.readline()
            if read:
                if verbose:
                    print(read)
                try:
                    output = json.loads(read)
                    if "ram_size" in output:
                        if verbose:
                            print(output["ram_size"])
                        return output["ram_size"]
                except ValueError:
                    pass

    import_memory_test_script = b"""
import gc\r
import json\r
import time\r
time.sleep(0.2)\r
gc.collect()\r
time.sleep(0.2)\r
before = gc.mem_alloc()\r
gc.collect()\r
time.sleep(0.2)\r
import {module_name}\r
time.sleep(0.2)\r
print(json.dumps({"ram_size": gc.mem_alloc() - before}))\r\n
"""

    ser = serial.Serial(device_path, timeout=0.5)  # open serial port
    print(ser.name)  # check which port was really used
    ser.write(b'\x04')  # write a string
    #try_read_ram_size()
    ser.write(b'\x03')  # write a string
    #try_read_ram_size()
    ser.write(import_memory_test_script.replace(b"{module_name}", module_name))

    try:
        while True:
            size = try_read_ram_size(verbose=False)
            if size:
                return size

    except KeyboardInterrupt:
        pass

    print("closing")
    ser.close()  # close


if __name__ == '__main__':
    print(get_ram_size(b"adafruit_mpr121", '/dev/ttyACM0'))