import pygame
import random
from map import Map
from player import Player
from projectile import Projectile
from consts import *
from drawer import Drawer
from notif import Notif
from mail import Mail
from text import Text
pygame.mixer.init()
pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = FPS
        self.bg_color = (0, 0, 0)
        self.bg = pygame.image.load("assets/images/bg.jpg")
        self.bg = pygame.transform.scale(self.bg, (SCREEN_W,SCREEN_H))
        self.player = Player()
        self.inventory = [1,2,3]
        self.projectiles = []
        self.drawers = [Drawer(1, 100, 100),Drawer(2, 400, 100),Drawer(3, 700, 100)]
        self.notif_cooldown = 100
        self.notifs = []
        self.mail_cooldown = MAIL_COOLDOWN
        self.mails = []
        self.map = Map(self.bg)
        self.score = 2000
        self.texts = []
        self.textscoodlow = 60
                
        pygame.font.init()
        self.gameFont = pygame.font.SysFont("Impact",  32)
        self.gameText = self.gameFont.render(f"Salaire: {self.score}$", True, (255,255,255))
    
    def manage_sprites(self):
        '''Gère l'affichage des sprites a chaque frame'''
        self.screen.blit(self.bg,(0,0))
        self.screen.blit(self.player.sprite, (self.player.rect.x,self.player.rect.y))
        for drawer in self.drawers:
            self.screen.blit(drawer.sprite, (drawer.rect.x, drawer.rect.y))
        for projectile in self.projectiles:
            projectile.move()
            self.screen.blit(projectile.sprite, (projectile.rect.x, projectile.rect.y))
        for notif in self.notifs:
            self.screen.blit(notif.sprite, (notif.rect.x, notif.rect.y))
        for mail in self.mails:
            mail.shoot()
            self.screen.blit(mail.sprite, (mail.rect.x, mail.rect.y))
        next_projectile_sprite = pygame.image.load(f"assets/images/projectile-{self.inventory[0]}.png")
        next_projectile_sprite = pygame.transform.scale(next_projectile_sprite, (50,50))
        self.screen.blit(next_projectile_sprite, (1000,10))
        for text in self.texts:
            text.draw(self.screen)
            if text.cooldown <= 0:
                self.texts.remove(text)
            else:
                text.cooldown -= 1
    
    def player_movement(self):
        '''Gère les déplacements du joueur'''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move_up()
        if keys[pygame.K_s]:
            self.player.move_down()
        if keys[pygame.K_a]:
            self.player.move_left()
        if keys[pygame.K_d]:
            self.player.move_right()
    
    def shoot(self, direction):
        '''Fonction de tir du joueur'''
        if self.player.shoot_cooldown > 0:
            return
        new_projectile = Projectile(self.inventory[0], self.player.rect.x, self.player.rect.y, direction)
        new_projectile.play_sound()
        random.shuffle(self.inventory)
        self.projectiles.append(new_projectile)
        self.player.shoot_cooldown = 20
    
    def check_collisions(self):
        '''Vérifie les collisions a chaque frames entre les différents sprites'''
        player_colliding, rect = self.map.check_collision(self.player.rect)
        if player_colliding:
            if self.player.rect.right > rect.left and self.player.rect.left < rect.left:
                self.player.rect.right = rect.left
            elif self.player.rect.left < rect.right and self.player.rect.right > rect.right:
                self.player.rect.left = rect.right
            elif self.player.rect.bottom > rect.top and self.player.rect.top < rect.top:
                self.player.rect.bottom = rect.top
            elif self.player.rect.top < rect.bottom and self.player.rect.bottom > rect.bottom:
                self.player.rect.top = rect.bottom

        for projectile in self.projectiles:
            if self.map.check_collision(projectile.rect)[0]:
                self.projectiles.remove(projectile)
                self.texts.append(Text("-10$", "red", projectile.rect.x, projectile.rect.y,))
                self.score -= 10

            for drawer in self.drawers:
                if projectile.rect.colliderect(drawer.rect):
                    self.projectiles.remove(projectile)
                    if projectile.type == drawer.type:
                        self.score += 100
                        self.texts.append(Text("+100$", "green", projectile.rect.x, projectile.rect.y,))
                        drawer.play_sound(True)
                    else:
                        self.score -= 100
                        self.texts.append(Text("-100$", "red", projectile.rect.x, projectile.rect.y,))
                        drawer.play_sound(False)
                    print(self.score)
                    drawer.changpos(random.randint(0,SCREEN_W-drawer.rect.width), random.randint(0,SCREEN_H-drawer.rect.height))
        
        for mail in self.mails:
            if self.player.rect.colliderect(mail.rect):
                mail.play_sound()
                self.mails.remove(mail)
                self.score -= 200
                self.texts.append(Text("-200$", "red", self.player.rect.x, self.player.rect.y,))
                print(self.score)

    def cooldown_decrement(self):
        '''Réduit le cooldown du tir du joueur a chque frame'''
        if self.player.shoot_cooldown > 0:
            self.player.shoot_cooldown -= 1
    
    def spawn_notif(self):
        '''Fait apparaitre une notification teams a intervalles réguliers'''
        if self.notif_cooldown > 0:
            self.notif_cooldown -= 1
        else:
            new_notif = Notif(random.randint(0,SCREEN_W), random.randint(0,SCREEN_H))
            new_notif.play_sound()
            self.notifs.append(new_notif)
            self.notif_cooldown = random.randint(800, 1200)

    def notifs_stalking(self):
        '''Fait suivre le joueur par les notifications'''
        for notif in self.notifs:
            notif.follow(self.player.rect.x, self.player.rect.y)
            self.score -= 2.5

    def spawn_mail(self):
        '''Fait apparaitre un mail a intervalles réguliers'''
        if self.mail_cooldown > 0:
            self.mail_cooldown -= 1
        else:
            new_mail = Mail()
            self.mails.append(new_mail)
            self.mail_cooldown = MAIL_COOLDOWN  
    
    def check_click(self):
        '''Vérifie si le joueur clique sur une notification'''
        for notif in self.notifs:
            if notif.rect.collidepoint(pygame.mouse.get_pos()):
                self.notifs.remove(notif)

    
    def run(self):
        '''Boucle principale'''
        self.map.draw()
        while self.running:
            self.clock.tick(self.fps)

            self.manage_sprites()

            self.player_movement()

            self.check_collisions()
            
            self.cooldown_decrement()

            self.spawn_notif()

            self.notifs_stalking()

            self.spawn_mail()

            self.gameText = self.gameFont.render(f"Salaire: {self.score}$", True, (255,255,255))
            self.screen.blit(self.gameText, (10,10))


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.shoot("up")
                    if event.key == pygame.K_DOWN:
                        self.shoot("down")
                    if event.key == pygame.K_LEFT:
                        self.shoot("left")
                    if event.key == pygame.K_RIGHT:
                        self.shoot("right")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click()
                if event.type == pygame.QUIT:
                    self.running = False

game = Game()  
game.run()
