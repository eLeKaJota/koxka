import pygame
from settings import *

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.number_of_frames = 0
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite

    def parse_sprite(self, number, width, height):
        image_width = self.sprite_sheet.get_width()
        image_height = self.sprite_sheet.get_height()
        sprites_per_row = image_width // width
        sprites_per_column = image_height // height
        sprite_number = 0
        for row in range(sprites_per_column):
            for column in range(sprites_per_row):
                if sprite_number == int(number):
                    x = column * width
                    y = row * height
                    return self.get_sprite(x, y, width, height)
                sprite_number += 1

    def get_animation(self, direction, number_of_frames, width, height, scale_width, scale_height):
        self.number_of_frames = number_of_frames
        animation_list = []
        for frame in range(number_of_frames):
            sprite_tmp = self.parse_sprite(frame, width, height)
            sprite_tmp_scaled = pygame.transform.scale(sprite_tmp, (scale_width, scale_height))
            if direction == 'left':
                sprite_tmp_scaled = pygame.transform.flip(sprite_tmp_scaled, True, False)
            animation_list.append(sprite_tmp_scaled)
        return animation_list
