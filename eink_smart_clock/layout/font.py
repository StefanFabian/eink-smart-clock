from PIL import ImageFont
import logging

def fit_font(width, height, fontpath, text):
    fontsize = 1
    font = ImageFont.truetype(fontpath, fontsize)
    size = font.getsize(text)
    while size[0] < width and size[1] < height:
        fontsize += 1
        font = ImageFont.truetype(fontpath, fontsize)
        size = font.getsize(text)
    fontsize -= 1
    logging.debug("Determined font size for w={}, h={}, text={} as {}".format(width, height, text, fontsize))
    return ImageFont.truetype(fontpath, fontsize)
