import belay

device = belay.Device("/dev/ttyACM0")

@device.task
def measure(module_name):
    print(module_name)


measure("adafruit_mpr121")