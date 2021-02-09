import pygame
from pygame import Vector2, Surface
from models import Direction
import models
from utils import compute_coordinate


def start_position(screen: Surface, step: int, offset: int) -> Vector2:
    size = screen.get_size()
    x = compute_coordinate(size[0] // 2, step, offset)
    y = compute_coordinate(size[1] // 2, step, offset)
    return Vector2(x, y)


def stop():
    return any(event.type == pygame.QUIT for event in pygame.event.get())


def handle_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.move(Direction.UP)
            elif event.key == pygame.K_DOWN:
                snake.move(Direction.DOWN)
            elif event.key == pygame.K_LEFT:
                snake.move(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.move(Direction.RIGHT)


def run(screen, clock):
    start = start_position(screen, 20, 2)
    snake = models.Snake(start)
    food = models.random_food(screen, 20, 2)
    while True:
        screen.fill('black')
        handle_events(snake)
        snake.draw(screen, color='white')
        food.draw(screen, color='red')
        pygame.display.update()
        clock.tick(60)
