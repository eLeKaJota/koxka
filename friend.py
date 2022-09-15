from gui import *
from spritesheet import *

friend_idle = Spritesheet('./assets/sprites/cat04_spritesheets/cat_sit.png')
friend_idle_R = friend_idle.get_animation('left', 8, 40, 32, 80, 80)
friend_idle_L = friend_idle.get_animation('right', 8, 40, 32, SCALE, SCALE)

friend_jump = Spritesheet('./assets/sprites/cat04_spritesheets/cat04_jump_strip4.png')
friend_jump_left = friend_jump.get_animation('left', 4, 40, 32, SCALE, SCALE)
friend_jump_right = friend_jump.get_animation('right', 4, 40, 32, SCALE, SCALE)

friend_fall = Spritesheet('./assets/sprites/cat04_spritesheets/cat04_fall_strip3.png')
friend_fall_left = friend_fall.get_animation('left', 3, 40, 32, SCALE, SCALE)
friend_fall_right = friend_fall.get_animation('right', 3, 40, 32, SCALE, SCALE)

friend_run = Spritesheet('./assets/sprites/cat04_spritesheets/cat04_run_strip4.png')
friend_run_right = friend_run.get_animation('right', 4, 40, 32, SCALE, SCALE)
friend_run_left = friend_run.get_animation('left', 4, 40, 32, SCALE, SCALE)

friend_climb = pygame.image.load('assets/player/cat_climb_1.png')
friend_climb_big = pygame.transform.scale(friend_climb, (SCALE, SCALE))
friend_climb_left_big = pygame.transform.flip(friend_climb_big, True, False)

class Friend(pygame.sprite.Sprite):

    def __init__(self, level):
        pygame.sprite.Sprite.__init__(self)
        self.image = friend_idle_R[0]
        self.rect = self.image.get_rect()
        self.level = level
        self.hitbox = pygame.Rect(self.rect.x + 17, self.rect.y + 11, 29, 32)

        self.pos = vec(50 , 50)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
        self.ground_y = self.pos.y

        self.jumping = False
        self.running = False
        self.move_frame = 0

    def move(self, player):
        # Constant acceleration of 0.5 (gravity)
        self.acc = vec(0, GRAVITY)

        if abs(player.vel.x) > ACC:
            self.running = True
        else:
            self.running = False

        # Capture key
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc.x = -ACC
        if keys[pygame.K_d]:
            self.acc.x = ACC

        # Formulas to calculate velocity while accounting for friction
        self.acc.x += self.vel.x * FRICTION
        if not player.vel.y >= MAX_SPEED:
            self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc # Update player position

        # Warp on end screen
        # if self.pos.x > WIDTH:
        #     self.pos.x = 0
        # if self.pos.x < 0:
        #     self.pos.x = WIDTH

        # Update rect position
        self.rect.midbottom = self.pos
        self.hitbox.midbottom = self.pos

    def update(self, screen):
       if self.vel.x > 0:
           self.direction = "RIGHT"
       else:
           self.direction = "LEFT"
       if self.jumping == False and self.running == True:
           if self.move_frame >= len(friend_run_right) * 2:
               self.move_frame = 0
           if self.vel.x > 0:
               self.image = friend_run_right[self.move_frame // 2]
           else:
               self.image = friend_run_left[self.move_frame // 2]
           self.move_frame += 1

       elif self.jumping:
            if self.vel.y < 0:
                if self.move_frame >= len(friend_jump_right) * 4:
                    self.move_frame = len(friend_jump_right) * 3
                if self.direction == "RIGHT":
                    self.image = friend_jump_right[self.move_frame // 4]
                else:
                    self.image = friend_jump_left[self.move_frame // 4]
                self.move_frame += 1
            else:
                if self.move_frame >= len(friend_fall_right) * 4:
                    self.move_frame = len(friend_fall_right) * 3
                if self.direction == "RIGHT":
                    self.image = friend_fall_right[self.move_frame // 4]
                else:
                    self.image = friend_fall_left[self.move_frame // 4]
                self.move_frame += 1

       if abs(self.vel.x) < 0.2 and self.move_frame != 0 and self.jumping == False:
            if self.vel.y < 0:
                if self.move_frame >= len(friend_fall_right) * 4:
                    self.move_frame = len(friend_fall_right) * 3
                if self.direction == "RIGHT":
                    self.image = friend_fall_right[self.move_frame // 4]
                else:
                    self.image = friend_fall_left[self.move_frame // 4]
                self.move_frame += 1
            else:
                if self.move_frame >= len(friend_idle_R) * 4:
                    self.move_frame = 0
                if self.direction == "RIGHT":
                    self.image = friend_idle_R[self.move_frame // 4]
                else:
                    self.image = friend_idle_L[self.move_frame // 4]
                self.move_frame += 1