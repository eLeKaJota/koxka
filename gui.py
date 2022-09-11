from settings import *

label_coins = pygame_gui.elements.ui_label.UILabel( pygame.Rect((WIDTH - 200, 0), (250, 50)), "Coins: ", manager)
label_coins_counter = pygame_gui.elements.ui_label.UILabel(pygame.Rect((WIDTH - 150, 0), (250, 50)), "0", manager)
label_completed = pygame_gui.elements.ui_label.UILabel(pygame.Rect((350, (HEIGHT / 2) - 50), (650, 80)), "¡Ya está! Compra el DLC", manager, None, None, "#win")
label_completed.hide()
