import pygame
from pygame import Vector2, Surface
from models import Direction, Snake, Square, random_food
from utils import compute_coordinate

keys_to_direction = {
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT
}


def start_position(screen: Surface, step: int, offset: int) -> Vector2:
    size = screen.get_size()
    x = compute_coordinate(size[0] // 2, step, offset)
    y = compute_coordinate(size[1] // 2, step, offset)
    return Vector2(x, y)


def handle_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            snake.move(keys_to_direction[event.key])


def food_consumed(snake: Snake, food: Square) -> bool:
    return snake.head.position == food.position


# TODO clean this function
def run(screen, clock):
    start = start_position(screen, 20, 2)
    snake = Snake(start)
    food = random_food(screen, snake, 20, 2)
    while True:
        screen.fill('black')
        handle_events(snake)
        if food_consumed(snake, food):
            snake.grow()
            food = random_food(screen, snake, 20, 2)
        snake.draw(screen, color='white')
        food.draw(screen, color='red')
        pygame.display.update()
        clock.tick(60)

