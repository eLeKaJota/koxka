from settings import *
from sprites import *

VirtualWindow = pygame.Surface.get_rect(screen)

class Camera:
    def __init__(self, player, map_size, enemy):
        self.player = player
        self.enemy = enemy
        self.map_size = map_size
        self.method = None

    def setmethod(self, method):
        self.method = method

    def update(self):
        VirtualWindow.center = self.player.rect.center
        if VirtualWindow.top < self.map_size.top:
            VirtualWindow.top = self.map_size.top

        if VirtualWindow.bottom > self.map_size.bottom:
            VirtualWindow.bottom = self.map_size.bottom

        if VirtualWindow.left < self.map_size.left:
            VirtualWindow.left = self.map_size.left

        if VirtualWindow.right > self.map_size.right:
            VirtualWindow.right = self.map_size.right

        for a in background_layer:
            if a.rect.colliderect(VirtualWindow):
                screen.blit(a.image, [(a.rect.x - VirtualWindow.x), (a.rect.y - VirtualWindow.y)])

        for a in walls_floor_layer:
            if a.rect.colliderect(VirtualWindow):
                screen.blit(a.image, [(a.rect.x - VirtualWindow.x), (a.rect.y - VirtualWindow.y)])

        for a in coins_layer:
            if a.rect.colliderect(VirtualWindow):
                screen.blit(a.image, [(a.rect.x - VirtualWindow.x), (a.rect.y - VirtualWindow.y)])

                # coins hitbox
                # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(a.hitbox.x-VirtualWindow.x,a.hitbox.y-VirtualWindow.y,a.hitbox.width,a.hitbox.height), 2)

        screen.blit(self.player.image, [(self.player.rect.x - VirtualWindow.x), (self.player.rect.y - VirtualWindow.y)])
        screen.blit(self.enemy.image, [(self.player.rect.x - 45 -VirtualWindow.x), (self.player.rect.y - VirtualWindow.y)])
        # Player hitbox
        # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.player.hitbox.x-VirtualWindow.x,self.player.hitbox.y-VirtualWindow.y,self.player.hitbox.width,self.player.hitbox.height), 2)
