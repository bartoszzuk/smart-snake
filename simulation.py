import pygame

from game import Board, random_food
from model import Direction, Snake, Square

keys_to_direction = {
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT
}


def handle_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            snake.move(keys_to_direction[event.key])


def food_consumed(snake: Snake, food: Square) -> bool:
    return snake.head.position == food.position


def overlaps(snake: Snake):
    unique = set(square.position for square in snake.squares)
    return len(unique) != len(snake.squares)


# TODO clean this function
def run(board: Board, clock):
    snake = Snake(board.start, length=2)
    food = random_food(board, exclude=snake.squares)
    while True:
        board.fill('black')
        handle_events(snake)
        if food_consumed(snake, food):
            food = random_food(board, exclude=snake.squares)
            snake.grow()
        if overlaps(snake):
            board.draw(snake, color='green')
        else:
            board.draw(snake, color='white')
        board.draw(food, color='red')
        pygame.display.update()
        clock.tick(60)

