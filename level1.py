from player import *
from spritesheet import *
from tiles import *
from camera import Camera

# Carga el nivel
spritesheet = Spritesheet('assets/tileset/spritesheet.png')
level1 = Tilemap('assets/levels/level1_front.csv', spritesheet, 0)
level1.load_tiles('assets/levels/level1_bg.csv', 1)
level1.load_tiles('assets/levels/level1_coins.csv', 2)

# Map Size
MapSize = pygame.Rect(0, 0, level1.map_width, level1.map_height)

# Player
player = Player(level1)

# Camera
camera = Camera(player, MapSize)
