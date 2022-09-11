from gui import *

player_idle = [
            pygame.image.load('assets/player/cat_idle_0.png'),
            pygame.image.load('assets/player/cat_idle_1.png'),
            pygame.image.load('assets/player/cat_idle_2.png'),
            pygame.image.load('assets/player/cat_idle_3.png'),
        ]

player_idle_big = [
            pygame.transform.scale(player_idle[0], (64, 64)),
            pygame.transform.scale(player_idle[1], (64, 64)),
            pygame.transform.scale(player_idle[2], (64, 64)),
            pygame.transform.scale(player_idle[3], (64, 64)),
        ]

player_idle_left = [
            pygame.transform.flip(player_idle[0], True, False),
            pygame.transform.flip(player_idle[1], True, False),
            pygame.transform.flip(player_idle[2], True, False),
            pygame.transform.flip(player_idle[3], True, False),
        ]

player_idle_left_big = [
            pygame.transform.scale(player_idle_left[0], (64, 64)),
            pygame.transform.scale(player_idle_left[1], (64, 64)),
            pygame.transform.scale(player_idle_left[2], (64, 64)),
            pygame.transform.scale(player_idle_left[3], (64, 64)),
        ]

player_jump = [
            pygame.image.load('assets/player/cat_jump_0.png'),
            pygame.image.load('assets/player/cat_jump_1.png'),
            pygame.image.load('assets/player/cat_jump_2.png'),
            pygame.image.load('assets/player/cat_jump_3.png'),
            pygame.image.load('assets/player/cat_jump_4.png'),
            pygame.image.load('assets/player/cat_jump_5.png'),
            pygame.image.load('assets/player/cat_jump_6.png'),
        ]

player_jump_big = [
            pygame.transform.scale(player_jump[0], (64, 64)),
            pygame.transform.scale(player_jump[1], (64, 64)),
            pygame.transform.scale(player_jump[2], (64, 64)),
            pygame.transform.scale(player_jump[3], (64, 64)),
            pygame.transform.scale(player_jump[4], (64, 64)),
            pygame.transform.scale(player_jump[5], (64, 64)),
            pygame.transform.scale(player_jump[6], (64, 64)),
        ]

player_jump_left = [
            pygame.transform.flip(player_jump[0], True, False),
            pygame.transform.flip(player_jump[1], True, False),
            pygame.transform.flip(player_jump[2], True, False),
            pygame.transform.flip(player_jump[3], True, False),
            pygame.transform.flip(player_jump[4], True, False),
            pygame.transform.flip(player_jump[5], True, False),
            pygame.transform.flip(player_jump[6], True, False),
        ]

player_jump_left_big = [
            pygame.transform.scale(player_jump_left[0], (64, 64)),
            pygame.transform.scale(player_jump_left[1], (64, 64)),
            pygame.transform.scale(player_jump_left[2], (64, 64)),
            pygame.transform.scale(player_jump_left[3], (64, 64)),
            pygame.transform.scale(player_jump_left[4], (64, 64)),
            pygame.transform.scale(player_jump_left[5], (64, 64)),
            pygame.transform.scale(player_jump_left[6], (64, 64)),
        ]

player_run = [
            pygame.image.load('assets/player/cat_run_0.png'),
            pygame.image.load('assets/player/cat_run_1.png'),
            pygame.image.load('assets/player/cat_run_2.png'),
            pygame.image.load('assets/player/cat_run_3.png'),
            pygame.image.load('assets/player/cat_run_4.png'),
            pygame.image.load('assets/player/cat_run_5.png'),
            pygame.image.load('assets/player/cat_run_6.png'),
            pygame.image.load('assets/player/cat_run_7.png'),
        ]

player_run_big = [
            pygame.transform.scale(player_run[0], (64, 64)),
            pygame.transform.scale(player_run[1], (64, 64)),
            pygame.transform.scale(player_run[2], (64, 64)),
            pygame.transform.scale(player_run[3], (64, 64)),
            pygame.transform.scale(player_run[4], (64, 64)),
            pygame.transform.scale(player_run[5], (64, 64)),
            pygame.transform.scale(player_run[6], (64, 64)),
            pygame.transform.scale(player_run[7], (64, 64)),
        ]

player_run_left = [
            pygame.transform.flip(player_run[0], True, False),
            pygame.transform.flip(player_run[1], True, False),
            pygame.transform.flip(player_run[2], True, False),
            pygame.transform.flip(player_run[3], True, False),
            pygame.transform.flip(player_run[4], True, False),
            pygame.transform.flip(player_run[5], True, False),
            pygame.transform.flip(player_run[6], True, False),
            pygame.transform.flip(player_run[7], True, False),
        ]

player_run_left_big = [
            pygame.transform.scale(player_run_left[0], (64, 64)),
            pygame.transform.scale(player_run_left[1], (64, 64)),
            pygame.transform.scale(player_run_left[2], (64, 64)),
            pygame.transform.scale(player_run_left[3], (64, 64)),
            pygame.transform.scale(player_run_left[4], (64, 64)),
            pygame.transform.scale(player_run_left[5], (64, 64)),
            pygame.transform.scale(player_run_left[6], (64, 64)),
            pygame.transform.scale(player_run_left[7], (64, 64)),
        ]

player_climb = pygame.image.load('assets/player/cat_climb_1.png')
player_climb_big = pygame.transform.scale(player_climb, (64, 64))
player_climb_left_big = pygame.transform.flip(player_climb_big, True, False)


class Player(pygame.sprite.Sprite):
    def __init__(self, level):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_idle_big[0]
        self.rect = self.image.get_rect()
        self.level = level
        self.hitbox = pygame.Rect(self.rect.x + 17, self.rect.y + 11, 29, 32)

        # Posición y dirección
        self.pos = vec(level.start_x, level.start_y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
        self.ground_y = self.pos.y

        # Movimiento
        self.jumping = False
        self.running = False
        self.move_frame = 0

    def gravity_check(self, ground, coins):
        hitscoin = pygame.sprite.spritecollide(self, coins, False, collided)
        if hitscoin:
            self.level.coins_collected += 1
            print("coins", self.level.coins_collected)
            label_coins_counter.set_text(str(self.level.coins_collected))
            hitscoin[0].kill()

        hits = pygame.sprite.spritecollide(self, ground, False, collided)
        if self.vel.y > 0:
            if hits:
                # print("Colisión", hits)
                if len(hits) == 2:
                    if hits[0].hitbox.left == hits[1].hitbox.left and hits[0].hitbox.right == hits[1].hitbox.right:
                        if self.hitbox.left > hits[0].hitbox.left:
                            self.image = player_climb_big
                        else:
                            self.image = player_climb_left_big

                for hit in hits:
                    # print("--------------------")
                    # print("hit", hit)
                    # print("pos-left", self.hitbox.left, " -> hit-left", hit.hitbox.left)
                    # print("pos-right", self.hitbox.right, " -> hit-right", hit.hitbox.right)
                    # print("pos-top", self.hitbox.top, " -> hit-top", hit.hitbox.top)
                    # print("pos-bottom", self.hitbox.bottom, " -> hit-bottom", hit.hitbox.bottom)
                    # print("pos-y", self.pos.y)
                    # print("++++++++++++++++++++")
                    if self.hitbox.left < hit.hitbox.right and self.hitbox.bottom > hit.hitbox.top + 10 and self.hitbox.top < hit.hitbox.bottom - 20 and self.vel.x < 0:
                        # print("Colisión derecha", self.vel.x)
                        self.pos.x = hit.rect.right + 15
                        self.vel.x = 0
                    elif self.hitbox.right > hit.hitbox.left and self.hitbox.bottom > hit.hitbox.top + 10 and self.hitbox.top < hit.hitbox.bottom - 20 and self.vel.x > 0:
                        # print("Colisión izquierda", self.vel.x)
                        self.pos.x = hit.rect.left - 15
                        self.vel.x = 0
                    if self.hitbox.bottom < hit.hitbox.top + 20 and self.hitbox.bottom > hit.hitbox.top:
                        # print("Colisión abajo")
                        self.pos.y = hit.hitbox.top + 1
                        self.vel.y = 0
                        self.jumping = False
        elif self.vel.y <= 0:
            if hits:
                for hit in hits:
                    # print("--------------------")
                    # print("hit", hit)
                    # print("pos-left", self.hitbox.left, " -> hit-left", hit.hitbox.left)
                    # print("pos-right", self.hitbox.right, " -> hit-right", hit.hitbox.right)
                    # print("pos-top", self.hitbox.top, " -> hit-top", hit.hitbox.top)
                    # print("pos-bottom", self.hitbox.bottom, " -> hit-bottom", hit.hitbox.bottom)
                    # print("pos-y", self.pos.y)
                    # print("++++++++++++++++++++")
                    if  self.hitbox.top > hit.hitbox.bottom - 10 and self.hitbox.top < hit.hitbox.bottom and (self.hitbox.right > hit.hitbox.left + 10 and self.hitbox.left < hit.hitbox.right) and self.hitbox.left < hit.hitbox.right - 10:
                        # print("Colisión arriba1")
                        self.pos.y = hit.hitbox.bottom + 30
                        self.vel.y = 0
                    elif self.hitbox.right > hit.hitbox.left and self.hitbox.bottom > hit.hitbox.top + 10 and self.hitbox.top < hit.hitbox.bottom - 20 and self.vel.x > 0:
                        # print("Colisión izquierda1", self.vel.x)
                        self.pos.x = hit.rect.left - 15
                        self.vel.x = 0
                    elif self.hitbox.left < hit.hitbox.right and self.hitbox.bottom > hit.hitbox.top + 10 and self.hitbox.top < hit.hitbox.bottom - 20 and self.vel.x < 0:
                        # print("Colisión derecha1", self.vel.x)
                        self.pos.x = hit.rect.right + 15
                        self.vel.x = 0

    def move(self):
        # Constant acceleration of 0.5 (gravity)
        self.acc = vec(0, GRAVITY)

        if abs(self.vel.x) > ACC:
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
        if not self.vel.y >= MAX_SPEED:
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
            if self.move_frame >= len(player_run) * 2:
                self.move_frame = 0
            if self.vel.x > 0:
                self.image = player_run_big[self.move_frame // 2]
            else:
                self.image = player_run_left_big[self.move_frame // 2]
            self.move_frame += 1

        elif self.jumping:
            if self.move_frame >= len(player_idle) * 8:
                self.move_frame = len(player_idle) * 8
            if self.direction == "RIGHT":
                self.image = player_jump_big[self.move_frame // 8]
            else:
                self.image = player_jump_left_big[self.move_frame // 8]
            self.move_frame += 1

        if abs(self.vel.x) < 0.2 and self.move_frame != 0 and self.jumping == False:
            if self.move_frame >= len(player_idle) * 4:
                self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = player_idle_big[self.move_frame // 4]
            else:
                self.image = player_idle_left_big[self.move_frame // 4]
            self.move_frame += 1
        if self.level.coins_collected == self.level.coins:
            label_completed.show()
            print("You win!")

    def jump(self, ground):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, ground, False, collided)
        self.rect.x -= 1
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -10