#from m5stack import rtc

#rtc.setTime(2022, 3, 9, 1, 19, 52)

#year, month, day, hour, minute, second = rtc.now()

#lcd.text(10, 10, "{}:{}:{}".format(hour, minute, second))

import m5stick as stick
from m5stack import lcd
from m5stack import M5Led
import time

stick.set_screen_color(80, 0, 100)
lcd.text(10, 40, "Hello!", color=0x0000FF)

count = 0

while count < 10:
  count += 1
  M5Led.on()
  time.sleep_ms(500)
  M5Led.off()
  time.sleep_ms(500)