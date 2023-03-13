import pygame
from player import Player
from humberger import Humberger
from score import Score
from sound import Sound
from shop import Shop
class Game:
    def __init__(self):
        self.all_player = pygame.sprite.Group()
        ##generer notre jouer
        self.shop = Shop()
        self.score = Score()
        self.sound = Sound()
        self.player = Player(self)
        self.all_humberger = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_humberger()
        self.humberger = Humberger()
        self.time_click = 1
    def spawn_humberger(self):
        humberger = Humberger()
        self.all_humberger.add(humberger)
