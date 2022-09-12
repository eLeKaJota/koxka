import pygame
import pygame_gui


# Vectors
vec = pygame.math.Vector2

# Window dimensions
WIDTH = 1000
HEIGHT = 800
SCALE = 80

# FPS
FPS = 30

# Physics
GRAVITY = 0.6
ACC = 1.2
MAX_SPEED = 14
FRICTION = -0.2
JUMP = -14

# Color palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
H_FA2F2F = (250, 47, 47)
H_50D2FE = (94, 210, 254)


pygame.init()

# Window create
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Koxka")

# Gui Manager
manager = pygame_gui.UIManager((WIDTH, HEIGHT), './assets/gui/gui_theme.json')


# Utilities
def collided(this, other):
    return this.hitbox.colliderect(other.hitbox)
