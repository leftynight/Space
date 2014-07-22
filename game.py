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
    return SpaceGame()

def title():
    # TODO: Return the title of the game.
    #raise NotImplementedError("title")
    return "Space!!!"

def thumbnail():
    # TODO: Return a (relative path) to the thumbnail image file for your game.
    #raise NotImplementedError("thumbnail")
    return join("games","space","images","thumbnail.png")

def hint():
    # TODO: Return the hint string for your game.
    #raise NotImplementedError("hint")
    return "Fly the spaceship to the planet!"
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
VELOCITY_INC = 15

class SpaceshipSprite(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        shippath = join("games","space","images","spaceship.png")
        self.image, self.rect = _load_image(shippath, 400 , 600)
        self.x_velocity = 0

    def update(self):
        self.rect.x += self.x_velocity

BG_VELOCITY = 2
class Background(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        bgPath =  join('games','space', 'images', 'space.png')
        self.image, self.rect = _load_image(bgPath, 0, -1152)
    
    def update(self):
        self.rect = self.rect.move(0, BG_VELOCITY)

##### MICROGAME CLASS ##########################################################

# TODO: rename this class to your game's name...
class SpaceGame(Microgame):
    def __init__(self):
        Microgame.__init__(self)
        # TODO: Initialization code here
        self.spaceship = SpaceshipSprite()
        self.bg = Background()
        self.sprites = Group(self.bg, self.spaceship)

    def start(self):
        # TODO: Startup code here
        pass

    def stop(self):
        # TODO: Clean-up code here
        pass

    def update(self, events):
        # TODO: Update code here
        self.sprites.update()

        #Check for hit of sides of screen 
        x_ship_left, _ = self.spaceship.rect.bottomleft
        x_ship_right, _ = self.spaceship.rect.bottomright
        if x_ship_left <= 0:
            self.spaceship.x_velocity = 0
        elif x_ship_right >= 1010:
            self.spaceship.x_velocity = 0   

        #Process user input
        for event in events:
            if event.type == KEYDOWN and event.key == K_LEFT:
                if x_ship_left <= 0:
                    pass
                else:
                    self.spaceship.x_velocity -= VELOCITY_INC
            elif event.type == KEYUP and event.key == K_LEFT:
                self.spaceship.x_velocity = 0
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                if x_ship_right >= 1010:
                    pass
                else:
                    self.spaceship.x_velocity += VELOCITY_INC
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.spaceship.x_velocity = 0

    def render(self, surface):
        # TODO: Rendering code here
        surface.fill(Color(0, 0, 0))
        self.sprites.draw(surface)

    def get_timelimit(self):
        # TODO: Return the time limit of this game (in seconds, 0 <= s <= 15)
        #raise NotImplementedError("get_timelimit")
        return 15
