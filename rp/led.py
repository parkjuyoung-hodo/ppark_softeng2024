from gpiozero import LED
from time import sleep

led= LED(17)

led.blink(on_time = 1, off_time =1, n=5)

led.close()



