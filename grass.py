from os.path import dirname, join

from pico2d import load_image


class Grass:
    def __init__(self):
        self.x, self.y = x, y
        self.image = load_image(join(dirname(__file__), 'grass.png'))

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass
