from PIL import ImageFont

def fit_font(width, height, fontpath, text):
    fontsize = 1
    font = ImageFont.truetype(fontpath, fontsize)
    size = font.getsize(text)
    while size[0] < width and size[1] < height:
        fontsize += 1
        font = ImageFont.truetype(fontpath, fontsize)
        size = font.getsize(text)
    fontsize -= 1
    return ImageFont.truetype(fontpath, fontsize)
