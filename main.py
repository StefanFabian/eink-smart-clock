#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import datetime
import logging
import os
from time import sleep
# Replace following by your epd
from waveshare_epd import epd7in5b_HD

from eink_smart_clock import Display, WEATHER_API_KEY
from eink_smart_clock.widgets import ClockWidget

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    epd = epd7in5b_HD.EPD()
    logging.info("Initializing.")
    epd.init()
    logging.info("Clear screen.")
    epd.Clear()
    logging.info("Setting up widgets.")
    d = Display(epd, two_color=True)
    d.add_widget(ClockWidget(0, 0, d.width, d.height, os.path.join(os.curdir, "font/Roboto-Medium.ttf")))
    logging.info("Setup finished. Starting draw loop.")
    try:
        while True:
            d.draw()
            sleeptime = 60 - datetime.utcnow().second
            sleep(sleeptime)
    except KeyboardInterrupt:
        epd7in5b_HD.epdconfig.module_exit()
