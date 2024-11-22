import pygame

class Notif:
    def __init__(self, x, y):
        self.sprite = pygame.image.load("assets/images/microsoft-teams.png")
        self.size = 100
        self.sprite = pygame.transform.scale(self.sprite, (self.size,self.size))
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = pygame.mixer.Sound("assets/sounds/notification.mp3")
        self.sound.set_volume(2)

    def follow(self, x, y):
        if abs(x - self.rect.x) > 1:
            self.rect.x += (x - self.rect.x) * 0.05
        else:
            self.rect.x = x

        if abs(y - self.rect.y) > 1:
            self.rect.y += (y - self.rect.y) * 0.05
        else:
            self.rect.y = y
    def play_sound(self):
        self.sound.play()