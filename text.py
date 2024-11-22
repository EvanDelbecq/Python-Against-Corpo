import pygame
class Text:
    def __init__(self, text, color, x, y):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        pygame.font.init()
        self.gameFont = pygame.font.SysFont("Impact",  20)
        self.gameText = self.gameFont.render(self.text, True, self.color)
        self.cooldown = 120
    def draw(self, screen):
        screen.blit(self.gameText, (self.x, self.y))