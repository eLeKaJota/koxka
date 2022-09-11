import csv, os
from sprites import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, number, x, y, spritesheet, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(number, width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = self.rect.inflate(0, 5)

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        screen.blit(self.image, self.rect)

class TileCoin(pygame.sprite.Sprite):
    def __init__(self, number, x, y, spritesheet, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(number, width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = pygame.Rect(self.rect.x + 24, self.rect.y + 24, 16, 16)

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        screen.blit(self.image, self.rect)

class Tilemap():
    def __init__(self, filename, spritesheet, layer):
        self.map_height = 0
        self.map_width = 0
        self.coins = 0
        self.coins_collected = 0
        self.tile_size = 64
        self.start_x = 0
        self.start_y = 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename, layer)
        self.map_surface = pygame.Surface((self.map_width, self.map_height))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def render(self, screen):
        screen.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.render(self.map_surface)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename, layer):
        tiles = []
        map = self.read_csv(filename)
        x = 0
        y = 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '74':
                    self.start_x = (x + 0.5) * self.tile_size
                    self.start_y = (y + 1) * self.tile_size
                if tile != '-1':
                    if layer == 0:
                        tile_tmp = Tile(tile, x * self.tile_size, y * self.tile_size, self.spritesheet, self.tile_size,
                                        self.tile_size)
                        walls_floor_layer.add(tile_tmp)
                    elif layer == 1:
                        tile_tmp = Tile(tile, x * self.tile_size, y * self.tile_size, self.spritesheet, self.tile_size, self.tile_size)
                        background_layer.add(tile_tmp)
                    elif layer == 2:
                        tile_tmp = TileCoin(tile, x * self.tile_size, y * self.tile_size, self.spritesheet, self.tile_size, self.tile_size)
                        self.coins += 1
                        coins_layer.add(tile_tmp)
                    tiles.append(tile_tmp)
                x += 1
            y += 1
        self.map_width = x * self.tile_size
        self.map_height = y * self.tile_size
        print(self.map_width, self.map_height)
        return tiles
