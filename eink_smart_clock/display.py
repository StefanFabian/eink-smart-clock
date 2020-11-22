from PIL import Image,ImageDraw,ImageFont

class Display:
    def __init__(self, epd, two_color=False):
        self.epd = epd
        self.width = epd.width
        self.height = epd.height
        self.two_color = two_color
        self.widgets = []

    def add_widget(self, widget):
        """
        docstring
        """
        pass

    def draw(self):
        black_image = Image.new('1', (self.epd.width, self.epd.height), 255)  # 255: clear the frame
        black_image_draw = ImageDraw.Draw(black_image)
        if self.two_color:
            accent_image = Image.new('1', (self.epd.width, self.epd.height), 255)  # 255: clear the frame
            accent_image_draw = ImageDraw.Draw(accent_image)
        else:
            accent_image_draw = None
        
        for widget in self.widgets:
            widget.draw(black_image_draw, accent_image_draw)
        
        if self.two_color:
            self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(accent_image))
        else:
            self.epd.display(self.epd.getbuffer(black_image))
