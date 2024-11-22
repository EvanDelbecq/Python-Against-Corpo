import pygame
from consts import SHOOT_COOLDOWN
class Player:
    def __init__(self):
        self.sprite = pygame.image.load("assets/images/player.png")
        self.sprite = pygame.transform.scale(self.sprite, (57.7,100))
        self.rect = self.sprite.get_rect()
        self.rect.x = 100
        self.rect.y = 600
        self.speed = 7
        self.shoot_cooldown = SHOOT_COOLDOWN

    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed
