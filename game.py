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
    #raise NotImplementedError("make_game")
    return LumberjackGame()

def title():
    # TODO: Return the title of the game.
    #raise NotImplementedError("title")
    return "Lumberjack"

def thumbnail():
    # TODO: Return a (relative path) to the thumbnail image file for your game.
    #raise NotImplementedError("thumbnail")
    return join("games", "lumberjack","images", "thumbnail.png")

def hint():
    # TODO: Return the hint string for your game.
    #raise NotImplementedError("hint")
    return "Cut down the tree!"

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
class LumberjackSprite(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		lumberjackpath = join("games","lumberjack","images","thumbnail.png")
		self.image, self.rect = _load_image(lumberjackpath, 300, 200)

class TreeblockSprite(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		treeblockpath = join("games", "lumberjack", "tree-block.png")
		self.image, self.rect = _load_image(treeblockpath, 300, 100)

##### MICROGAME CLASS ##########################################################

# TODO: rename this class to your game's name...
class LumberjackGame(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        # TODO: Initialization code here
        self.lumberjack = LumberjackSprite()
        self.treeblock = TreeblockSprite()
        self.sprites = Group(self.lumberjack, self.treeblock)

    def start(self):
        # TODO: Startup code here
        pass

    def stop(self):
        # TODO: Clean-up code here
        pass

    def update(self, events):
        # TODO: Update code here
        self.sprites.update()

    def render(self, surface):
        # TODO: Rendering code here
        surface.fill(Color(255, 255, 255))
        self.sprites.draw(surface)

    def get_timelimit(self):
        # TODO: Return the time limit of this game (in seconds, 0 <= s <= 15)
        #raise NotImplementedError("get_timelimit")
        return 15
