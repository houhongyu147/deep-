import random

WIDTH = 20
HEIGHT = 20

DIRECTIONS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
}


class Snake:
    def __init__(self, name, start_pos, direction):
        self.name = name
        self.body = [start_pos]
        self.direction = direction
        self.grow = 0
        self.alive = True
        self.score = 0

    def head(self):
        return self.body[0]

    def change_dir(self, new_dir):
        if len(self.body) > 1:
            opposite = {
                'UP': 'DOWN',
                'DOWN': 'UP',
                'LEFT': 'RIGHT',
                'RIGHT': 'LEFT',
            }
            if opposite[self.direction] == new_dir:
                return
        self.direction = new_dir

    def move(self):
        if not self.alive:
            return
        dx, dy = DIRECTIONS[self.direction]
        x, y = self.head()
        new_head = (x + dx, y + dy)
        self.body.insert(0, new_head)
        if self.grow > 0:
            self.grow -= 1
        else:
            self.body.pop()

    def kill(self):
        self.alive = False


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snakes = [
            Snake('A', (1, 1), 'RIGHT'),
            Snake('B', (width - 2, height - 2), 'LEFT'),
        ]
        self.food = None
        self.spawn_food()

    def spawn_food(self):
        free = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
            if all((x, y) not in s.body for s in self.snakes)
        ]
        self.food = random.choice(free) if free else None

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def step(self):
        for snake in self.snakes:
            if not snake.alive:
                continue
            if self.food:
                fx, fy = self.food
                hx, hy = snake.head()
                choices = []
                if fx > hx:
                    choices.append('RIGHT')
                if fx < hx:
                    choices.append('LEFT')
                if fy > hy:
                    choices.append('DOWN')
                if fy < hy:
                    choices.append('UP')
                if choices:
                    random.shuffle(choices)
                    snake.change_dir(choices[0])
            snake.move()

        occupied = {}
        for snake in self.snakes:
            if not snake.alive:
                continue
            head = snake.head()
            if not self.in_bounds(head) or head in snake.body[1:]:
                snake.kill()
                continue
            if head in occupied:
                other = occupied[head]
                snake.kill()
                other.kill()
            else:
                occupied[head] = snake

        for snake in self.snakes:
            if not snake.alive:
                continue
            for other in self.snakes:
                if snake is other:
                    continue
                if snake.head() in other.body:
                    snake.kill()

        for snake in self.snakes:
            if not snake.alive:
                continue
            if snake.head() == self.food:
                snake.score += 1
                snake.grow += 1
                self.spawn_food()

    def run(self, steps):
        for _ in range(steps):
            living = [s for s in self.snakes if s.alive]
            if len(living) <= 1:
                break
            self.step()
        for snake in self.snakes:
            status = 'alive' if snake.alive else 'dead'
            print(f'{snake.name}: score={snake.score}, status={status}')


if __name__ == '__main__':
    random.seed(0)
    game = Game(WIDTH, HEIGHT)
    game.run(200)
