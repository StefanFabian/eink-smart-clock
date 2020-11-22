#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import datetime
import os
from time import sleep
# Replace following by your epd
from waveshare_epd import epd7in5b_HD

from eink_smart_clock import Display
from eink_smart_clock.widgets import ClockWidget

if __name__ == "__main__":
    
    epd = epd7in5b_HD.EPD()
    epd.init()
    epd.Clear()
    d = Display(epd, two_color=True)
    d.add_widget(ClockWidget(0, 0, d.width, d.height, os.path.join(os.curdir, "font/Roboto-Medium.ttf")))
    try:
        while True:
            d.draw()
            sleeptime = 60 - datetime.utcnow().second
            sleep(sleeptime)
    except KeyboardInterrupt:
        pass
