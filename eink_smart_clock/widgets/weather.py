from PIL import Image,ImageDraw,ImageFont
from eink_smart_clock import Widget
from eink_smart_clock.layout import fit_font
import logging
import time


class WeatherWidget(Widget):
    def __init__(self, x, y, width, height, font, api_key):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = fit_font(width, height, font, "00:00")
        self.api_key = api_key
        if api_key is None:
            logging.error("You have to set the OpenWeatherMap api key in the config for the weather widget to work!")
    
    def draw(self, image_black, image_red=None):
        current_time = time.strftime("%H:%M", time.localtime())
        size = self.font.getsize(current_time)
        image_black.text((self.x + (self.width - size[0]) / 2, self.y + (self.height - size[1]) / 2), current_time, font = self.font, fill = 0)
        logging.debug("Drawing {} with size {}, {} at {}, {}".format(current_time, size[0], size[1], self.x, self.y))
