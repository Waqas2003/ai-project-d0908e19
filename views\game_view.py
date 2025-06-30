import pygame
from config.settings import WIDTH, HEIGHT, BLOCK_SIZE
from models.game import Game

class GameView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.game = Game()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for pos in self.game.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.game.food.position[0], self.game.food.position[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.game.snake.direction != 'DOWN':
                    self.game.snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.game.snake.direction != 'UP':
                    self.game.snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and self.game.snake.direction != 'RIGHT':
                    self.game.snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.game.snake.direction != 'LEFT':
                    self.game.snake.direction = 'RIGHT'
        return True
```

**utils/draw_utils.py:**