from gpiozero import LED
from time import sleep

led = LED(17)

for i in range(5):
    led.on()
    sleep(1)
    led.off()
    sleep(1)

led.close()