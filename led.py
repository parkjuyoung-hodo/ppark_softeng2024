import lgpio

# GPIO 핀 설정
LED_PIN = 17

# GPIO 핸들 열기
h = lgpio.gpiochip_open(0)

# LED_PIN을 출력 모드로 설정
lgpio.gpio_claim_output(h, LED_PIN)

# LED 켜기
lgpio.gpio_write(h, LED_PIN, 1)  # HIGH 신호
print("LED ON")

# LED 끄기
lgpio.gpio_write(h, LED_PIN, 0)  # LOW 신호
print("LED OFF")

# GPIO 핸들 닫기
lgpio.gpiochip_close(h)
