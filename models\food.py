import random

class Food:
    def __init__(self):
        self.position = (random.randint(0, 39) * 20, random.randint(0, 29) * 20)
```

**models/game.py:**