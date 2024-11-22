import pygame
import random
from consts import MAIL_COOLDOWN
class Mail:
    def __init__(self):
        self.sprite = pygame.image.load("assets/images/mail.png")
        self.sprite = pygame.transform.scale(self.sprite, (50,50))
        self.sound = pygame.mixer.Sound("assets/sounds/mail.mp3")
        self.rect = self.sprite.get_rect()
        self.speed = 7
        self.shoot_direction = random.randint(0, 3)
        match self.shoot_direction:
            case 0:
                self.rect.x = 0
                self.rect.y = random.randint(0, 720)
            case 1:
                self.rect.x = 800
                self.rect.y = random.randint(0, 720)
            case 2:
                self.rect.x = random.randint(0, 1080)
                self.rect.y = 0
            case 3:
                self.rect.x = random.randint(0, 1080)
                self.rect.y = 800
        self.cooldown = MAIL_COOLDOWN

    def shoot(self):
        match self.shoot_direction:
            case 0:
                self.rect.x += self.speed
            case 1:
                self.rect.x -= self.speed
            case 2:
                self.rect.y += self.speed
            case 3:
                self.rect.y -= self.speed

    def play_sound(self):
        self.sound.play()