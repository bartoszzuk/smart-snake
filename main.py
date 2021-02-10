from configparser import ConfigParser

import pygame

import game
import simulation
from utils import tuple_converter

config = ConfigParser(converters={'tuple': tuple_converter})
config.read('configuration.ini')


def initialize():
    size = config['main'].gettuple('window-size')
    step = config['main'].getint('step')
    offset = config['main'].getint('offset')

    pygame.init()
    pygame.display.set_caption('Smart Snake')
    board = game.Board(size, step, offset)
    clock = pygame.time.Clock()
    return board, clock


def main():
    board, clock = initialize()
    simulation.run(board, clock)


if __name__ == '__main__':
    main()
