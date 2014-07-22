# Pygame imports
import pygame, pygame.mixer
from pygame import Surface
from pygame.image import load
from pygame.locals import *
from pygame.mixer import music
from pygame.rect import Rect
from pygame.sprite import Group, Sprite

# Path imports
from os.path import join

# Random imports
from random import randint, choice

# Microgame-specific imports
import locals
from microgame import Microgame

##### LOADER-REQUIRED FUNCTIONS ################################################

def make_game():
    # TODO: Return a new instance of your Microgame class.
    return Space()

def title():
    # TODO: Return the title of the game.
    return 'Space!!!'

def thumbnail():
    # TODO: Return a (relative path) to the thumbnail image file for your game.
    return join('games','SPACE','images', 'thumbnail.png')

def hint():
    # TODO: Return the hint string for your game.
    return 'Fly your ship to the planet'

################################################################################

def _load_image(name, x, y):
    '''
    Loads an image file, returning the surface and rectangle corresponding to
    that image at the given location.
    '''
    try:
        image = load(name)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, msg:
        print 'Cannot load image: {}'.format(name)
        raise SystemExit, msg
    rect = image.get_rect().move(x, y)
    return image, rect

##### MODEL CLASSES ############################################################

# TODO: put your Sprite classes here
X_VELOCITY = 0

class SpaceShip(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        shipPath =  join('games','SPACE', 'images', 'ship.png')
        self.image, self.rect = _load_image(shipPath, 300, 300)

    def _update_velocity(self):
        pass

class Background(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        shipPath =  join('games','SPACE', 'images', 'ship.png')
        self.image, self.rect = _load_image(shipPath, 300, 300)
##### MICROGAME CLASS ##########################################################

# TODO: rename this class to your game's name...
class Space(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        # TODO: Initialization code here

    def start(self):
        # TODO: Startup code here
        pass

    def stop(self):
        # TODO: Clean-up code here
        pass

    def update(self, events):
        # TODO: Update code here
        pass

    def render(self, surface):
        # TODO: Rendering code here
        pass

    def get_timelimit(self):
        # TODO: Return the time limit of this game (in seconds, 0 <= s <= 15)
        raise NotImplementedError("get_timelimit")
