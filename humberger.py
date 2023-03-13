import pygame
class Humberger(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.click_max = 30
        self.click_auto = open("auto_click.txt", "r")
        self.score_auto = self.click_auto.readline()
        self.click_auto.close()

        self.image = pygame.image.load('hamburger.png')
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = (1920/2)-(500/2)
        self.rect.y = (1080/2)-(500/2)
    def forward(self):
        self.rect = self.rect




