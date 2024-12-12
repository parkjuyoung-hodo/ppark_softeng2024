import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# I2C 초기화
i2c = busio.I2C(board.SCL, board.SDA)

# OLED 디스플레이 초기화 (주소 0x3C)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

# 화면 초기화
oled.fill(0)
oled.show()

# 텍스트 출력
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.text((0, 0), "Hello, OLED!", font=font, fill=255)
oled.image(image)
oled.show()
