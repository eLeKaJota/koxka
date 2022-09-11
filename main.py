import sys
from level1 import *

# Clock
clock = pygame.time.Clock()

# Bucle principal
while True:
    time_delta = clock.tick(FPS) / 1000.0
    player.gravity_check(walls_floor_layer, coins_layer)
    # clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump(walls_floor_layer)
        manager.process_events(event)

    manager.update(time_delta)
    screen.fill(BLACK)


    # Update player
    player.move()
    player.update(screen)

    # Update camera
    camera.update()

    # Update gui
    manager.draw_ui(screen)

    # Refresh screen
    pygame.display.flip()
