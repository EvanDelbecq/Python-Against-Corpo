import pygame 
class Drawer:
    def __init__(self, type, x, y):
        self.sprite = pygame.image.load(f"assets/images/drawer-{type}.png")
        self.type = type
        self.sprite = pygame.transform.scale(self.sprite, (65.8,100))
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.soundCorrect = pygame.mixer.Sound("assets/sounds/correct.mp3")
        self.soundCorrect.set_volume(0.8)
        self.soundWrong = pygame.mixer.Sound("assets/sounds/wrong.mp3")
        self.soundWrong.set_volume(0.8)

    def changpos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def play_sound(self, correct):
        if correct:
            self.soundCorrect.play()
        else:
            self.soundWrong.play()