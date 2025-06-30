class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def update(self):
        self.snake.move()
        if self.snake.eat(self.food):
            self.score += 1
            self.food = Food()
        else:
            if (self.snake.body[0][0] < 0 or
                self.snake.body[0][0] >= 800 or
                self.snake.body[0][1] < 0 or
                self.snake.body[0][1] >= 600 or
                self.snake.body[0] in self.snake.body[1:]):
                return False
        return True
```

**views/game_view.py:**