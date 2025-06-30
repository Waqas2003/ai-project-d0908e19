import pygame
from views.game_view import GameView

def main():
    pygame.init()
    game_view = GameView()
    running = True
    while running:
        running = game_view.handle_events()
        if not game_view.game.update():
            break
        game_view.draw()
        pygame.time.delay(100)
    pygame.quit()

if __name__ == '__main__':
    main()
```

**requirements.txt:**