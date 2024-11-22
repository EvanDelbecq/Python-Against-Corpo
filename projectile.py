import pygame
import random

class Projectile:
    def __init__(self, type , x, y, direction):
        self.sprite = pygame.image.load(f"assets/images/projectile-{type}.png")
        self.type = type
        self.sprite = pygame.transform.scale(self.sprite, (50,50))
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = 10
        self.sounds = [pygame.mixer.Sound("assets/sounds/throw1.mp3"), pygame.mixer.Sound("assets/sounds/throw2.mp3")]

    def move(self):
        if self.direction == "up":
            self.rect.y -= self.speed
        if self.direction == "down":
            self.rect.y += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
    def play_sound(self):
        random.choice(self.sounds).play()