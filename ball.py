from os.path import dirname, join

from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    SPEED = 10
    HALF_SIZE = 10

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.image = load_image(join(dirname(__file__), 'ball21x21.png'))

    def update(self):
        self.x += self.direction * self.SPEED
        if not self.is_on_screen():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)

    def is_on_screen(self):
        return -self.HALF_SIZE <= self.x <= get_canvas_width() + self.HALF_SIZE
