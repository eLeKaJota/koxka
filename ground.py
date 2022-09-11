import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/ground.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 400
        self.hitbox = self.rect.inflate(0, 5)

    def render(self, screen):
        screen.blit(self.image, self.rect)

class Ground4(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/ground4.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = self.rect.inflate(0, 5)

    def render(self, screen):
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        screen.blit(self.image, self.rect)