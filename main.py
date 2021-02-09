from configparser import ConfigParser
from utils import tuple_converter, compute_coordinate
import pygame
import simulation

config = ConfigParser(converters={'tuple': tuple_converter})
config.read('configuration.ini')


def adjust_size(size, step, offset):
    x = compute_coordinate(size[0], step, offset)
    y = compute_coordinate(size[1], step, offset)
    return x, y


def initialize():
    size = config['main'].gettuple('window-size')
    step = config['main'].getint('step')
    offset = config['main'].getint('offset')
    size = adjust_size(size, step, offset)

    pygame.init()
    pygame.display.set_caption('Smart Snake')
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    return screen, clock


def main():
    screen, clock = initialize()
    simulation.run(screen, clock)


if __name__ == '__main__':
    main()
