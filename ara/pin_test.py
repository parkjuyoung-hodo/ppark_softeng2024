from gpiozero import led
from time import sleep

led = LED(17)
try:
    led.on()
    print("LED ON")
    sleep(2)
    led.off()
    print("LED OFF")
finally:
    led.close()