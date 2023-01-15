import sys
import pygame
from pygame.locals import *
from pygame import font
import time
import random

class game:
    def __init__(self):
        self.file = "music_arcade.mp3"
        self.ecran = pygame.display.set_mode((1000,800))
        pygame.display.set_caption("Flappy Bird")
        self.ecran_color = (240,230,220)
        self.max_y = 850
        self.min_y = 50
        self.max_x = 950
        self.min_x = 50
        self.hard = False
        self.hard2 = False
        self.hard3 = False
        self.hard4 = False
        self.flappy_position_x = 350
        self.flappy_position_y = 60
        self.jeu_en_cours = True
        self.acceleration = 1
        self.direction_bas = True
        self.direction_haut = False
        self.clock = pygame.time.Clock()
        self.key = ''
        self.space_pyl = 200
        self.pylone = [0, 1030, self.space_pyl]
        self.pylone2 = [0, 1030, self.space_pyl]
        self.pylone3 = [0, 1030, self.space_pyl]
        self.pylone[0] = random.randrange(20,700 - self.pylone[2] ,1)
        self.pylone2[0] = random.randrange(20,700 - self.pylone2[2] ,1)
        self.pylone3[0] = random.randrange(20,700 - self.pylone3[2] ,1)
        self.count = 0
        self.count2 = 0
        self.score = 0
        self.image = pygame.image.load("oiseau_v12.png").convert_alpha()
        self.image2 = pygame.image.load("oiseau_v22.png").convert_alpha()
        self.image3 = pygame.image.load("oiseau_mort-removebg-preview.png").convert_alpha()
        self.image4 = pygame.image.load("tueur-removebg-preview.png").convert_alpha()
        self.image =pygame.transform.scale(self.image,(50,50)) 
        self.image2 =pygame.transform.scale(self.image2,(50,50)) 
        self.image3 =pygame.transform.scale(self.image3,(70,70)) 
        self.image4 =pygame.transform.scale(self.image4,(70,70)) 
        self.nge1 = pygame.image.load("nge.png").convert_alpha()
        self.nge1_y = random.randrange(0,650,10)
        self.t_nge1 = (random.randrange(700,900,10), random.randrange(200,300,10))
        self.nge1 =pygame.transform.scale(self.nge1,self.t_nge1) 
        self.nge1_x = 1000
        self.nge2 = pygame.image.load("nge.png").convert_alpha()
        self.nge2_y = random.randrange(0,650,10)
        self.t_nge2 = (random.randrange(500,600,10), random.randrange(100,200,10))
        self.nge2 =pygame.transform.scale(self.nge1,self.t_nge2) 
        self.nge2_x = 1000
        self.nge3 = pygame.image.load("nge.png").convert_alpha()
        self.nge3_y = random.randrange(0,650,10)
        self.t_nge3 = (random.randrange(200,300,10), random.randrange(50,150,10))
        self.nge3 =pygame.transform.scale(self.nge1,self.t_nge3) 
        self.nge3_x = 1000
        self.tueur_x = 0
        self.tueur_y = self.flappy_position_y
        self.fps = 27
        self.p1 = True
        self.p2 = True
        self.p3 = True
        self.noir = (80,80,80)
        self.gris = (150,150,150)
        self.blanc = (255,255,255)
        self.trait = 3
        self.rouge = (0,0,0)
        pygame.font.init()
        self.font1 = pygame.font.Font("game_over.ttf", 80)
        self.little_f1 = pygame.font.Font("game_over.ttf", 50)
        self.traine = []

#############################################################################################################################################################################################

    def intro(self):
        while True:
            pygame.display.set_caption("Menu jeu")
            pygame.font.init()
            
            italic = pygame.font.Font("Fast Forward.ttf",16)

            
            #Chargement et collage du fond
            fond = pygame.image.load("nuagez.jpg").convert()
            fond = pygame.transform.scale(fond,(1000,800))
            self.ecran.blit(fond, (0,0))

            font_play = pygame.font.Font("game_over.ttf",500)
            font_play2 = pygame.font.Font("game_over.ttf",150)
            font_play3 = pygame.font.Font("game_over.ttf",100)

            text = font_play.render("FLAPPY", False, (0,0,0))
            self.ecran.blit(text, [100,50])
            text2 = font_play2.render("PLAY", False, (0,0,0))
            text3 = font_play3.render("PRESS [ SPACE ]", False, (0,0,0))
            text4 = font_play2.render("EXIT", False, (0,0,0))
            text5 = font_play3.render("PRESS [ ESC ]", False, (0,0,0))
            
            self.ecran.blit(text2, [420,350])
            self.ecran.blit(text3, [350,430])
            self.ecran.blit(text4, [420,510])
            self.ecran.blit(text5, [380,590])
            pygame.init()
            for evenement in pygame.event.get():
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_SPACE:
                        game().prcpl()
                    if evenement.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

#############################################################################################################################################################################################

    def mort(self):
        self.acceleration = 40
        pygame.mixer.init()
        self.file = "j_perdu2.mp3"
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()
        while self.tueur_x < 1000:
            fond = pygame.image.load("nuagez.jpg").convert()
            fond = pygame.transform.scale(fond,(1000,800))
            italic = pygame.font.Font("Fast Forward.ttf",13)
            self.ecran.blit(fond, (0,0))
            self.tueur_y = self.flappy_position_y
            
            text = self.font1.render("Score : " + str(self.score), False, (0,0,0))
            self.ecran.blit(text, [10,8])
            if self.hard:
                pygame.draw.rect(self.ecran, (100,100,200), (380,58, 150,40))
                self.fps = 39
                text_hard = self.font1.render("H A R D", False, (255,0,0))
                self.ecran.blit(text_hard, [400,50])
            if self.hard2:
                pygame.draw.rect(self.ecran, (100,100,200), (280,58, 380,40))
                self.fps = 41
                text_hard = self.font1.render("V R A I M E N T  H A R D", False, (255,0,0))
                self.ecran.blit(text_hard, [300,50])
            if self.hard3:
                pygame.draw.rect(self.ecran, (255,0,0), (280,58, 380,40))
                self.fps = 45
                text_hard = self.font1.render("S A L E M E N T  H A R D", False,(100,100,200))
                self.ecran.blit(text_hard, [300,50])
            if self.hard4:
                italic = pygame.font.Font("Fast Forward.ttf",13)
                pygame.draw.rect(self.ecran, (100,0,0), (280,58, 410,40))
                pygame.draw.rect(self.ecran, (200,200,200), (530,630, 400 ,360))
                self.fps = 48
                text_hard = self.font1.render("H A R D E M E N T  H A R D", False,(255,255,255))
                self.ecran.blit(text_hard, [300,50])
                text_hard = self.little_f1.render("+ de 75, bravo", False,(255,255,255))
                self.ecran.blit(text_hard, [550,650])
                text_hard = self.little_f1.render('Si tu veux, envoie ton score par sms', False,(255,255,255))
                self.ecran.blit(text_hard, [550,680])
                text_hard = self.little_f1.render("au 07 68 77 10 73, et n'oublie jamais :", False,(255,255,255))
                self.ecran.blit(text_hard, [550,710])
                text_hard = italic.render('<"J\'IRAI_OU_QUE_J\'AILLE">', False,(255,255,255))
                self.ecran.blit(text_hard, [550,755])


            
            game.mort_menu(self)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone[1],0, 30,self.pylone[0]))
            pygame.draw.rect(self.ecran, self.noir, (self.pylone[1], 50 +self.pylone[0] + self.pylone[2], 30, 800 - self.pylone[2] - self.pylone[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone[1], 50 + self.pylone[0] + self.pylone[2], 30, 800 - self.pylone[2] - self.pylone[0] ), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone2[1],0, 30,self.pylone2[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone2[1],0, 30,self.pylone2[0]), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2], 30, 800 - self.pylone2[2] - self.pylone2[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2], 30, 800 - self.pylone2[2] - self.pylone2[0] ), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone3[1],0, 30,self.pylone3[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone3[1],0, 30,self.pylone3[0]), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone3[1], 50 + self.pylone3[0] + self.pylone3[2], 30, 800 - self.pylone3[2] - self.pylone3[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone3[1], 50 + self.pylone3[0] + self.pylone3[2], 30, 800 - self.pylone3[2] - self.pylone3[0] ), self.trait)
            points = [(self.pylone[1] + 30, 2), (self.pylone[1] + 30, self.pylone[0]), (self.pylone[1] + 30 + 20, self.pylone[0] - 20), (self.pylone[1] + 30 + 20, 2)]  # The corner points of the polygon.
            pygame.draw.polygon(self.ecran, self.gris, points)
            pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
            
            points2 = [(self.pylone[1] + 30, 50 + self.pylone[0] + self.pylone[2]), (self.pylone[1] + 30, 800 ), (self.pylone[1] + 30+20, 800 ), (self.pylone[1] + 30 + 20, 50 + self.pylone[0]+ self.pylone[2] - 20)]
            pygame.draw.polygon(self.ecran, self.gris, points2)
            pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
            
            points3 = [(self.pylone[1], 50 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 30, 50 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 30 + 20, 50 - 20 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 20, 50 - 20 + self.pylone[0]+ self.pylone[2])]
            pygame.draw.polygon(self.ecran, self.blanc, points3)
            pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)

            if self.count > 177/3:
                points = [(self.pylone2[1] + 30, 2), (self.pylone2[1] + 30, self.pylone2[0]), (self.pylone2[1] + 30 + 20, self.pylone2[0] - 20), (self.pylone2[1] + 30 + 20, 2)]
                pygame.draw.polygon(self.ecran, self.gris, points)
                pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
                points2 = [(self.pylone2[1] + 30, 50 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 30, 800), (self.pylone2[1] + 30+20, 800), (self.pylone2[1] + 30 + 20, 50 + self.pylone2[0]+ self.pylone2[2] - 20)]
                pygame.draw.polygon(self.ecran, self.gris, points2)
                pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
                points3 = [(self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2]), (self.pylone2[1] + 30, 50 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 30 + 20, 50 - 20 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 20, 50 - 20 + self.pylone2[0]+ self.pylone2[2])]
                pygame.draw.polygon(self.ecran, self.blanc, points3)
                pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)
                
            if self.count > 177*(2/3):
                points = [(self.pylone3[1] + 30, 2), (self.pylone3[1] + 30, self.pylone3[0]), (self.pylone3[1] + 30 + 20, self.pylone3[0] - 20), (self.pylone3[1] + 30 + 20, 2)]
                pygame.draw.polygon(self.ecran, self.gris, points)
                pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
                points2 = [(self.pylone3[1] + 30, 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30, 800 ), (self.pylone3[1] + 30+20, 800 ), (self.pylone3[1] + 30 + 20, 50 + self.pylone3[0]+ self.pylone3[2] - 20)]
                pygame.draw.polygon(self.ecran, self.gris, points2)
                pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
                points3 = [(self.pylone3[1], 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30, 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30 + 20, 50 - 20 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 20, 50 - 20 + self.pylone3[0]+ self.pylone3[2])]
                pygame.draw.polygon(self.ecran, self.blanc, points3)
                pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)
            self.clock.tick(20)
            if self.tueur_x < self.flappy_position_x + 30:
                self.ecran.blit(self.image, (self.flappy_position_x, self.flappy_position_y))
            else:
                self.ecran.blit(self.image3, (self.flappy_position_x, self.flappy_position_y))
            self.ecran.blit(self.image4, (self.tueur_x, self.tueur_y))
            self.tueur_x += (self.acceleration +2)*3
            self.acceleration = self.acceleration/(1.17 )
            pygame.display.flip()

        self.acceleration = 1
        while self.flappy_position_y < 700:
            fond = pygame.image.load("nuagez.jpg").convert()
            fond = pygame.transform.scale(fond,(1000,800))
            self.ecran.blit(fond, (0,0))
            text = self.font1.render("Score : " + str(self.score), False, (0,0,0))
            self.ecran.blit(text, [10,8])
            if self.hard:
                pygame.draw.rect(self.ecran, (100,100,200), (380,58, 150,40))
                self.fps = 39
                text_hard = self.font1.render("H A R D", False, (255,0,0))
                self.ecran.blit(text_hard, [400,50])
            if self.hard2:
                pygame.draw.rect(self.ecran, (100,100,200), (280,58, 380,40))
                self.fps = 41
                text_hard = self.font1.render("V R A I M E N T  H A R D", False, (255,0,0))
                self.ecran.blit(text_hard, [300,50])
            if self.hard3:
                pygame.draw.rect(self.ecran, (255,0,0), (280,58, 380,40))
                self.fps = 45
                text_hard = self.font1.render("S A L E M E N T  H A R D", False, (255,0,0))
                self.ecran.blit(text_hard, [300,50])
            if self.hard4:
                italic = pygame.font.Font("Fast Forward.ttf",13)
                pygame.draw.rect(self.ecran, (100,0,0), (280,58, 410,40))
                pygame.draw.rect(self.ecran, (200,200,200), (530,630, 400 ,360))
                self.fps = 48
                text_hard = self.font1.render("H A R D E M E N T  H A R D", False,(255,255,255))
                self.ecran.blit(text_hard, [300,50])
                text_hard = self.little_f1.render("+ de 75, bravo", False,(255,255,255))
                self.ecran.blit(text_hard, [550,650])
                text_hard = self.little_f1.render('Si tu veux, envoie ton score par sms', False,(255,255,255))
                self.ecran.blit(text_hard, [550,680])
                text_hard = self.little_f1.render("au 07 68 77 10 73, et n'oublie jamais :", False,(255,255,255))
                self.ecran.blit(text_hard, [550,710])
                text_hard = italic.render('<"J\'IRAI_OU_QUE_J\'AILLE">', False,(255,255,255))
                self.ecran.blit(text_hard, [550,755])
            game.mort_menu(self)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone[1],0, 30,self.pylone[0]))
            pygame.draw.rect(self.ecran, self.noir, (self.pylone[1], 50 +self.pylone[0] + self.pylone[2], 30, 800 - self.pylone[2] - self.pylone[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone[1], 50 + self.pylone[0] + self.pylone[2], 30, 800 - self.pylone[2] - self.pylone[0] ), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone2[1],0, 30,self.pylone2[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone2[1],0, 30,self.pylone2[0]), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2], 30, 800 - self.pylone2[2] - self.pylone2[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2], 30, 800 - self.pylone2[2] - self.pylone2[0] ), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone3[1],0, 30,self.pylone3[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone3[1],0, 30,self.pylone3[0]), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone3[1], 50 + self.pylone3[0] + self.pylone3[2], 30, 800 - self.pylone3[2] - self.pylone3[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone3[1], 50 + self.pylone3[0] + self.pylone3[2], 30, 800 - self.pylone3[2] - self.pylone3[0] ), self.trait)
            points = [(self.pylone[1] + 30, 2), (self.pylone[1] + 30, self.pylone[0]), (self.pylone[1] + 30 + 20, self.pylone[0] - 20), (self.pylone[1] + 30 + 20, 2)]  # The corner points of the polygon.
            pygame.draw.polygon(self.ecran, self.gris, points)
            pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
            
            points2 = [(self.pylone[1] + 30, 50 + self.pylone[0] + self.pylone[2]), (self.pylone[1] + 30, 800 ), (self.pylone[1] + 30+20, 800 ), (self.pylone[1] + 30 + 20, 50 + self.pylone[0]+ self.pylone[2] - 20)]
            pygame.draw.polygon(self.ecran, self.gris, points2)
            pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
            
            points3 = [(self.pylone[1], 50 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 30, 50 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 30 + 20, 50 - 20 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 20, 50 - 20 + self.pylone[0]+ self.pylone[2])]
            pygame.draw.polygon(self.ecran, self.blanc, points3)
            pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)

            if self.count > 177/3:
                points = [(self.pylone2[1] + 30, 2), (self.pylone2[1] + 30, self.pylone2[0]), (self.pylone2[1] + 30 + 20, self.pylone2[0] - 20), (self.pylone2[1] + 30 + 20, 2)]
                pygame.draw.polygon(self.ecran, self.gris, points)
                pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
                points2 = [(self.pylone2[1] + 30, 50 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 30, 800), (self.pylone2[1] + 30+20, 800), (self.pylone2[1] + 30 + 20, 50 + self.pylone2[0]+ self.pylone2[2] - 20)]
                pygame.draw.polygon(self.ecran, self.gris, points2)
                pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
                points3 = [(self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2]), (self.pylone2[1] + 30, 50 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 30 + 20, 50 - 20 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 20, 50 - 20 + self.pylone2[0]+ self.pylone2[2])]
                pygame.draw.polygon(self.ecran, self.blanc, points3)
                pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)
                
            if self.count > 177*(2/3):
                points = [(self.pylone3[1] + 30, 2), (self.pylone3[1] + 30, self.pylone3[0]), (self.pylone3[1] + 30 + 20, self.pylone3[0] - 20), (self.pylone3[1] + 30 + 20, 2)]
                pygame.draw.polygon(self.ecran, self.gris, points)
                pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
                points2 = [(self.pylone3[1] + 30, 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30, 800 ), (self.pylone3[1] + 30+20, 800 ), (self.pylone3[1] + 30 + 20, 50 + self.pylone3[0]+ self.pylone3[2] - 20)]
                pygame.draw.polygon(self.ecran, self.gris, points2)
                pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
                points3 = [(self.pylone3[1], 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30, 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30 + 20, 50 - 20 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 20, 50 - 20 + self.pylone3[0]+ self.pylone3[2])]
                pygame.draw.polygon(self.ecran, self.blanc, points3)
                pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)
                
            self.clock.tick(20)
            self.ecran.blit(self.image3, (self.flappy_position_x, self.flappy_position_y))
            self.flappy_position_y += (self.acceleration +2)*3
            self.acceleration = self.acceleration*(1.2)
            pygame.display.flip()
        
        fond = pygame.image.load("nuagez.jpg").convert()
        fond = pygame.transform.scale(fond,(1000,800))
        self.ecran.blit(fond, (0,0))
        game.mort_menu(self)
        text = self.font1.render("Score : " + str(self.score), False, (0,0,0))
        if self.hard:
            pygame.draw.rect(self.ecran, (100,100,200), (380,58, 150,40))
            self.fps = 39
            text_hard = self.font1.render("H A R D", False, (255,0,0))
            self.ecran.blit(text_hard, [400,50])
        if self.hard2:
            pygame.draw.rect(self.ecran, (100,100,200), (280,58, 380,40))
            self.fps = 41
            text_hard = self.font1.render("V R A I M E N T  H A R D", False, (255,0,0))
            self.ecran.blit(text_hard, [300,50])
        if self.hard3:
            pygame.draw.rect(self.ecran, (255,0,0), (280,58, 380,40))
            self.fps = 45
            text_hard = self.font1.render("S A L E M E N T  H A R D", False, (100,100,200)) 
            self.ecran.blit(text_hard, [300,50])
        if self.hard4:
            italic = pygame.font.Font("Fast Forward.ttf",13)
            pygame.draw.rect(self.ecran, (100,0,0), (280,58, 410,40))
            pygame.draw.rect(self.ecran, (200,200,200), (530,630, 400 ,360))
            self.fps = 48
            text_hard = self.font1.render("H A R D E M E N T  H A R D", False,(255,255,255))
            self.ecran.blit(text_hard, [300,50])
            text_hard = self.little_f1.render("+ de 75, bravo", False,(255,255,255))
            self.ecran.blit(text_hard, [550,650])
            text_hard = self.little_f1.render('Si tu veux, envoie ton score par sms', False,(255,255,255))
            self.ecran.blit(text_hard, [550,680])
            text_hard = self.little_f1.render("au 07 68 77 10 73, et n'oublie jamais :", False,(255,255,255))
            self.ecran.blit(text_hard, [550,710])
            text_hard = italic.render('<"J\'IRAI_OU_QUE_J\'AILLE">', False,(255,255,255))
            self.ecran.blit(text_hard, [550,755])
        self.ecran.blit(text, [10,8])
        pygame.draw.rect(self.ecran, self.noir, (self.pylone[1],0, 30,self.pylone[0]))
        pygame.draw.rect(self.ecran, self.noir, (self.pylone[1], 50 +self.pylone[0] + self.pylone[2], 30, 800 - self.pylone[2] - self.pylone[0] ))
        pygame.draw.rect(self.ecran, self.rouge, (self.pylone[1], 50 + self.pylone[0] + self.pylone[2], 30, 800 - self.pylone[2] - self.pylone[0] ), self.trait)
        pygame.draw.rect(self.ecran, self.noir, (self.pylone2[1],0, 30,self.pylone2[0] ))
        pygame.draw.rect(self.ecran, self.rouge, (self.pylone2[1],0, 30,self.pylone2[0]), self.trait)
        pygame.draw.rect(self.ecran, self.noir, (self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2], 30, 800 - self.pylone2[2] - self.pylone2[0] ))
        pygame.draw.rect(self.ecran, self.rouge, (self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2], 30, 800 - self.pylone2[2] - self.pylone2[0] ), self.trait)
        pygame.draw.rect(self.ecran, self.noir, (self.pylone3[1],0, 30,self.pylone3[0] ))
        pygame.draw.rect(self.ecran, self.rouge, (self.pylone3[1],0, 30,self.pylone3[0]), self.trait)
        pygame.draw.rect(self.ecran, self.noir, (self.pylone3[1], 50 + self.pylone3[0] + self.pylone3[2], 30, 800 - self.pylone3[2] - self.pylone3[0] ))
        pygame.draw.rect(self.ecran, self.rouge, (self.pylone3[1], 50 + self.pylone3[0] + self.pylone3[2], 30, 800 - self.pylone3[2] - self.pylone3[0] ), self.trait)
        points = [(self.pylone[1] + 30, 2), (self.pylone[1] + 30, self.pylone[0]), (self.pylone[1] + 30 + 20, self.pylone[0] - 20), (self.pylone[1] + 30 + 20, 2)]  # The corner points of the polygon.
        pygame.draw.polygon(self.ecran, self.gris, points)
        pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
            
        points2 = [(self.pylone[1] + 30, 50 + self.pylone[0] + self.pylone[2]), (self.pylone[1] + 30, 800 ), (self.pylone[1] + 30+20, 800 ), (self.pylone[1] + 30 + 20, 50 + self.pylone[0]+ self.pylone[2] - 20)]
        pygame.draw.polygon(self.ecran, self.gris, points2)
        pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
            
        points3 = [(self.pylone[1], 50 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 30, 50 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 30 + 20, 50 - 20 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 20, 50 - 20 + self.pylone[0]+ self.pylone[2])]
        pygame.draw.polygon(self.ecran, self.blanc, points3)
        pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)

        if self.count > 177/3:
            points = [(self.pylone2[1] + 30, 2), (self.pylone2[1] + 30, self.pylone2[0]), (self.pylone2[1] + 30 + 20, self.pylone2[0] - 20), (self.pylone2[1] + 30 + 20, 2)]
            pygame.draw.polygon(self.ecran, self.gris, points)
            pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
            points2 = [(self.pylone2[1] + 30, 50 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 30, 800), (self.pylone2[1] + 30+20, 800), (self.pylone2[1] + 30 + 20, 50 + self.pylone2[0]+ self.pylone2[2] - 20)]
            pygame.draw.polygon(self.ecran, self.gris, points2)
            pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
            points3 = [(self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2]), (self.pylone2[1] + 30, 50 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 30 + 20, 50 - 20 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 20, 50 - 20 + self.pylone2[0]+ self.pylone2[2])]
            pygame.draw.polygon(self.ecran, self.blanc, points3)
            pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)
                
        if self.count > 177*(2/3):
            points = [(self.pylone3[1] + 30, 2), (self.pylone3[1] + 30, self.pylone3[0]), (self.pylone3[1] + 30 + 20, self.pylone3[0] - 20), (self.pylone3[1] + 30 + 20, 2)]
            pygame.draw.polygon(self.ecran, self.gris, points)
            pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
            points2 = [(self.pylone3[1] + 30, 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30, 800 ), (self.pylone3[1] + 30+20, 800 ), (self.pylone3[1] + 30 + 20, 50 + self.pylone3[0]+ self.pylone3[2] - 20)]
            pygame.draw.polygon(self.ecran, self.gris, points2)
            pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
            points3 = [(self.pylone3[1], 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30, 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30 + 20, 50 - 20 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 20, 50 - 20 + self.pylone3[0]+ self.pylone3[2])]
            pygame.draw.polygon(self.ecran, self.blanc, points3)
            pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)
        
        if self.hard4:
            italic = pygame.font.Font("Fast Forward.ttf",13)
            pygame.draw.rect(self.ecran, (100,0,0), (280,58, 410,40))
            pygame.draw.rect(self.ecran, (200,200,200), (530,630, 400 ,360))
            self.fps = 48
            text_hard = self.font1.render("H A R D E M E N T  H A R D", False,(255,255,255))
            self.ecran.blit(text_hard, [300,50])
            text_hard = self.little_f1.render("+ de 75, bravo", False,(255,255,255))
            self.ecran.blit(text_hard, [550,650])
            text_hard = self.little_f1.render('Si tu veux, envoie ton score par sms', False,(255,255,255))
            self.ecran.blit(text_hard, [550,680])
            text_hard = self.little_f1.render("au 07 68 77 10 73, et n'oublie jamais :", False,(255,255,255))
            self.ecran.blit(text_hard, [550,710])
            text_hard = italic.render('<"J\'IRAI_OU_QUE_J\'AILLE">', False,(255,255,255))
            self.ecran.blit(text_hard, [550,755])
            
        self.flappy_position_y = 700
        self.ecran.blit(self.image3, (self.flappy_position_x, self.flappy_position_y))
        pygame.display.flip()
        def perdu(self):
            while self.jeu_en_cours:
                for evenement in pygame.event.get():
                    if evenement.type == pygame.KEYDOWN:
                        if evenement.key == pygame.K_SPACE:
                            self.flappy_position_y = 60
                            self.acceleration = 1
                            self.pylone = [0, 1030, self.space_pyl]
                            self.pylone2 = [0, 1030, self.space_pyl]
                            self.pylone3 = [0, 1030, self.space_pyl]
                            self.pylone[0] = random.randrange(20,700 - self.pylone[2] ,1)
                            self.pylone2[0] = random.randrange(20,700 - self.pylone2[2] ,1)
                            self.pylone3[0] = random.randrange(20,700 - self.pylone3[2] ,1)
                            self.count = 0
                            self.count2 = 0
                            self.fps = 27
                            self.score = 0
                            self.tueur_x = 0
                            self.tueur_y = self.flappy_position_y
                            self.hard = False
                            self.hard2 = False
                            self.hard3 = False
                            self.hard4 = False
                            game.prcpl(self)
                        if evenement.key == pygame.K_ESCAPE:
                            game().intro()
        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.KEYDOWN:
                    perdu(self)
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

##############################################################################################################################################################################################

    def mort_menu(self):
        pygame.font.init()
        pygame.draw.rect(self.ecran, (20,150,20), (100,100, 300 ,600))
        pygame.draw.rect(self.ecran, (0,100,0), (300,100, 350 ,600))
        pygame.draw.rect(self.ecran, (20,150,20), (650,100, 250 ,600))
        pygame.draw.rect(self.ecran, (0,100,0), (100,100, 800 ,600), 10)
        font_menu = pygame.font.Font("game_over.ttf",150)
        font_menu1 = pygame.font.Font("game_over.ttf",80)
        text_menu1 = font_menu.render("GAME OVER", False, (200,200,200))
        text_menu2 = font_menu.render("Score : " + str(self.score), False, (200,200,200))
        text_menu3 = font_menu1.render("REPLAY :", False, (200,200,200))
        text_menu4 = font_menu1.render("PRESS [ SPACE ]", False, (200,200,200))
        text_menu5 = font_menu1.render("QUIT :", False, (200,200,200))
        text_menu6 = font_menu1.render("PRESS [ ESC ]", False, (200,200,200))
        if self.pylone[1] >= (1060*2)/3 - 6.66:
            self.ecran.blit(text_menu3, [650,self.pylone[0] + 30])
            self.ecran.blit(text_menu4, [650,self.pylone[0] + 90])

        elif self.pylone2[1] >= (1060*2)/3 - 6.66:
            self.ecran.blit(text_menu3, [650,self.pylone2[0] + 30])
            self.ecran.blit(text_menu4, [650,self.pylone2[0] + 90])

        elif self.pylone3[1] >= (1060*2)/3 - 6.66:
            self.ecran.blit(text_menu3, [650,self.pylone3[0] + 30])
            self.ecran.blit(text_menu4, [650,self.pylone3[0] + 90])

        if self.pylone3[1] >= 1060/3 - 10 and self.pylone3[1] < (1060*2)/3 - 6.66:
            self.ecran.blit(text_menu1, [300,self.pylone3[0] + 30])
            self.ecran.blit(text_menu2, [300,self.pylone3[0] + 100])
        elif self.pylone2[1] >= 1060/3 - 10 and self.pylone2[1] < (1060*2)/3 - 6.66:
            self.ecran.blit(text_menu1, [300,self.pylone2[0] + 30])
            self.ecran.blit(text_menu2, [300,self.pylone2[0] + 100])
        elif self.pylone[1] >= 1060/3 - 10 and self.pylone[1] < (1060*2)/3 - 6.66:
            self.ecran.blit(text_menu1, [300,self.pylone[0] + 30])
            self.ecran.blit(text_menu2, [300,self.pylone[0] + 100])

        if self.pylone3[1] < 1060/3 - 10:
            self.ecran.blit(text_menu5, [105,self.pylone3[0] + 30])
            self.ecran.blit(text_menu6, [105,self.pylone3[0] + 90])
        elif self.pylone2[1] < 1060/3 - 10:
            self.ecran.blit(text_menu5, [105,self.pylone2[0] + 30])
            self.ecran.blit(text_menu6, [105,self.pylone2[0] + 90])
        elif self.pylone[1] < 1060/3 - 10:
            self.ecran.blit(text_menu5, [105,self.pylone[0] + 30])
            self.ecran.blit(text_menu6, [105,self.pylone[0] + 90])

############################################################################################################################################################################################# 
    def prcpl(self):
        pygame.init()
        pygame.mixer.init()
        self.file = "music_arcade.mp3"
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play(-1)
        while self.jeu_en_cours:
            
            self.count += 1
            self.count2 += 1
            self.clock.tick(self.fps)
            fond = pygame.image.load("nuagez.jpg").convert()
            fond = pygame.transform.scale(fond,(1000,800))
            self.ecran.blit(fond, (0,0))
            italic = pygame.font.Font("Fast Forward.ttf",13)
            text = self.font1.render("Score : " + str(self.score), False, (0,0,0))
            self.ecran.blit(text, [10,8])

            self.ecran.blit(self.nge1, (self.nge1_x, self.nge1_y))
            self.ecran.blit(self.nge2, (self.nge2_x, self.nge2_y))
            self.ecran.blit(self.nge3, (self.nge3_x, self.nge3_y))

            self.nge3_x -= 3
            self.nge2_x -= 2
            self.nge1_x -= 1
            (a,b) = self.t_nge1
            
            if(self.nge1_x <= -a):
                self.nge1 = pygame.image.load("nge.png").convert_alpha()
                self.t_nge1 = (random.randrange(700,900,10), random.randrange(500,600,10))
                self.nge1 =pygame.transform.scale(self.nge1,self.t_nge1)
                self.nge1_y = random.randrange(0,650,10)
                self.nge1_x = 1000
            (a,b) = self.t_nge2
            if(self.nge2_x <= -a):
                self.nge2 = pygame.image.load("nge.png").convert_alpha()
                self.nge2 =pygame.transform.scale(self.nge2,self.t_nge2)
                self.t_nge2 = (random.randrange(500,600,10), random.randrange(200,300,10))
                self.nge2_y = random.randrange(0,650,10)
                self.nge2_x = 1000
            (a,b) = self.t_nge3
            if(self.nge3_x <= -a):
                self.nge3 = pygame.image.load("nge.png").convert_alpha()
                self.nge3 =pygame.transform.scale(self.nge3,self.t_nge3) 
                self.t_nge3 = (random.randrange(100,300,10), random.randrange(50,150,10))
                self.nge3_y = random.randrange(0,650,10)
                self.nge3_x = 1000
 
            if self.score >= 0:
                nb = random.randrange(0,3 ,1)
                if nb == 0:
                    if self.hard:
                        new_color = (255,255,0)
                    elif self.hard2:
                        new_color = (255,165,0)
                    elif self.hard3:
                        new_color = (255,0,0)
                    else:
                        new_color = (255,0,0)
                if nb == 1:
                    if self.hard:
                        new_color = (255,255,0)
                    elif self.hard2:
                        new_color = (255,165,0)
                    else:
                        new_color = (255,165,0)
                if nb == 2:
                    if self.hard4:
                        new_color = (165,0,255)
                    else:
                        new_color = (255,255,0)
                self.traine.append([self.flappy_position_x,self.flappy_position_y + 20, new_color,0 ])
                if len(self.traine) > 15:
                    while len(self.traine) > 15 :
                        self.traine.pop(0)
                for i in range(len(self.traine)):
                    k = len(self.traine) - i - 1
                    self.traine[k][0] -= i + 3
                    self.traine[k][3] = 10 / (16 - (len(self.traine) - i))*4
                for i in range(2,len(self.traine) - 1):
                    
                    if self.hard:
                        pygame.draw.rect(self.ecran, self.traine[i][2], (self.traine[i][0] + 5, self.traine[i][1]- 10, self.traine[i][3],self.traine[i][3]))
                        pygame.draw.rect(self.ecran, self.traine[i][2], (self.traine[i][0] + 5, self.traine[i][1] + 5, self.traine[i][3],self.traine[i][3]))
                    elif self.hard2 or self.hard3 or self.hard4:
                        pygame.draw.rect(self.ecran, self.traine[i][2], (self.traine[i][0] + 5, self.traine[i][1] + 10, self.traine[i][3],self.traine[i][3]))
                        pygame.draw.rect(self.ecran, self.traine[i][2], (self.traine[i][0] + 5, self.traine[i][1]- 10, self.traine[i][3],self.traine[i][3]))
                        pygame.draw.rect(self.ecran, self.traine[i][2], (self.traine[i][0] + 5, self.traine[i][1] + 5, self.traine[i][3],self.traine[i][3]))
                        

            if self.count2 == 300 and self.fps < 36:
                self.count2 = 0
                self.fps += 3
            
            if self.score == 30:
                self.hard = True
            if self.score == 50:
                self.hard2 = True
                self.hard = False
            if self.score == 65:
                self.hard3 = True
                self.hard2 = False
            if self.score == 75:
                self.hard4 = True
                self.hard3 = False

            if self.hard:
                pygame.draw.rect(self.ecran, (100,100,200), (380,58, 150,40))
                self.fps = 39
                text_hard = self.font1.render("H A R D", False, (255,0,0))
                self.ecran.blit(text_hard, [400,50])
            if self.hard2:
                pygame.draw.rect(self.ecran, (100,100,200), (280,58, 380,40))
                self.fps = 41
                text_hard = self.font1.render("V R A I M E N T  H A R D", False, (255,0,0))
                self.ecran.blit(text_hard, [300,50])
            if self.hard3:
                pygame.draw.rect(self.ecran, (255,0,0), (280,58, 380,40))
                self.fps = 45
                text_hard = self.font1.render("S A L E M E N T  H A R D", False, (100,100,255))
                self.ecran.blit(text_hard, [300,50])
            if self.hard4:
                italic = pygame.font.Font("Fast Forward.ttf",13)
                pygame.draw.rect(self.ecran, (100,0,0), (280,58, 410,40))
                pygame.draw.rect(self.ecran, (200,200,200), (530,630, 400 ,360))
                self.fps = 48
                text_hard = self.font1.render("H A R D E M E N T  H A R D", False,(255,255,255))
                self.ecran.blit(text_hard, [300,50])
                text_hard = self.little_f1.render("+ de 75, bravo", False,(255,255,255))
                self.ecran.blit(text_hard, [550,650])
                text_hard = self.little_f1.render('Si tu veux, envoie ton score par sms', False,(255,255,255))
                self.ecran.blit(text_hard, [550,680])
                text_hard = self.little_f1.render("au 07 68 77 10 73, et n'oublie jamais :", False,(255,255,255))
                self.ecran.blit(text_hard, [550,710])
                text_hard = italic.render('<"J\'IRAI_OU_QUE_J\'AILLE">', False,(255,255,255))
                self.ecran.blit(text_hard, [550,755])
            


            points = [(self.pylone[1] + 30, 2), (self.pylone[1] + 30, self.pylone[0]), (self.pylone[1] + 30 + 20, self.pylone[0] - 20), (self.pylone[1] + 30 + 20, 2)]  # The corner points of the polygon.
            pygame.draw.polygon(self.ecran, self.gris, points)
            pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
            
            points2 = [(self.pylone[1] + 30, 50 + self.pylone[0] + self.pylone[2]), (self.pylone[1] + 30, 800 ), (self.pylone[1] + 30+20, 800 ), (self.pylone[1] + 30 + 20, 50 + self.pylone[0]+ self.pylone[2] - 20)]
            pygame.draw.polygon(self.ecran, self.gris, points2)
            pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
            
            points3 = [(self.pylone[1], 50 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 30, 50 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 30 + 20, 50 - 20 + self.pylone[0]+ self.pylone[2]), (self.pylone[1] + 20, 50 - 20 + self.pylone[0]+ self.pylone[2])]
            pygame.draw.polygon(self.ecran, self.blanc, points3)
            pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)

            if self.count > 177/3:
                points = [(self.pylone2[1] + 30, 2), (self.pylone2[1] + 30, self.pylone2[0]), (self.pylone2[1] + 30 + 20, self.pylone2[0] - 20), (self.pylone2[1] + 30 + 20, 2)]
                pygame.draw.polygon(self.ecran, self.gris, points)
                pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
                points2 = [(self.pylone2[1] + 30, 50 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 30, 800), (self.pylone2[1] + 30+20, 800), (self.pylone2[1] + 30 + 20, 50 + self.pylone2[0]+ self.pylone2[2] - 20)]
                pygame.draw.polygon(self.ecran, self.gris, points2)
                pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
                points3 = [(self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2]), (self.pylone2[1] + 30, 50 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 30 + 20, 50 - 20 + self.pylone2[0]+ self.pylone2[2]), (self.pylone2[1] + 20, 50 - 20 + self.pylone2[0]+ self.pylone2[2])]
                pygame.draw.polygon(self.ecran, self.blanc, points3)
                pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)
                
            if self.count > 177*(2/3):
                points = [(self.pylone3[1] + 30, 2), (self.pylone3[1] + 30, self.pylone3[0]), (self.pylone3[1] + 30 + 20, self.pylone3[0] - 20), (self.pylone3[1] + 30 + 20, 2)]
                pygame.draw.polygon(self.ecran, self.gris, points)
                pygame.draw.polygon(self.ecran, self.rouge, points, self.trait)
                points2 = [(self.pylone3[1] + 30, 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30, 800 ), (self.pylone3[1] + 30+20, 800 ), (self.pylone3[1] + 30 + 20, 50 + self.pylone3[0]+ self.pylone3[2] - 20)]
                pygame.draw.polygon(self.ecran, self.gris, points2)
                pygame.draw.polygon(self.ecran, self.rouge, points2, self.trait)
                points3 = [(self.pylone3[1], 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30, 50 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 30 + 20, 50 - 20 + self.pylone3[0]+ self.pylone3[2]), (self.pylone3[1] + 20, 50 - 20 + self.pylone3[0]+ self.pylone3[2])]
                pygame.draw.polygon(self.ecran, self.blanc, points3)
                pygame.draw.polygon(self.ecran, self.rouge, points3, self.trait)
                
                
                

            if self.direction_bas:
                self.ecran.blit(self.image, (self.flappy_position_x, self.flappy_position_y))
            elif self.direction_haut:
                self.ecran.blit(self.image2, (self.flappy_position_x, self.flappy_position_y))

            
            
            if self.flappy_position_y > 850:
                self.flappy_position_y = 700
                game.mort(self)
           
            if self.flappy_position_y < 0:
                game.mort(self)

            if (self.flappy_position_x > self.pylone[1] - 40 and self.flappy_position_x < self.pylone[1]) and (self.flappy_position_y < self.pylone[0] - 10 or self.flappy_position_y > self.pylone[0] + self.pylone[2] + 10):
                game.mort(self)

            if (self.flappy_position_x > self.pylone2[1] - 40 and self.flappy_position_x < self.pylone2[1]) and (self.flappy_position_y < self.pylone2[0] - 10 or self.flappy_position_y > self.pylone2[0] + self.pylone2[2] + 10):
                game.mort(self)

            if (self.flappy_position_x > self.pylone3[1] - 40 and self.flappy_position_x < self.pylone3[1]) and (self.flappy_position_y < self.pylone3[0] - 10 or self.flappy_position_y > self.pylone3[0] + self.pylone3[2] + 10):
                game.mort(self)
            

            for evenement in pygame.event.get():
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_SPACE:
                        self.direction_bas = False
                        self.direction_haut = True
                        self.acceleration = 20
                    if evenement.key == pygame.K_b:
                        test = True
                        while test:
                            pygame.mixer.music.pause( ) 
                            for evenement2 in pygame.event.get():
                                if evenement2.type == pygame.KEYDOWN:
                                    if evenement2.key == pygame.K_SPACE:
                                        test = False
                        
                        pygame.mixer.music.unpause()

                    if evenement.key == pygame.K_ESCAPE:
                        game().intro()
                if evenement.type == pygame.QUIT:
                    self.hard = False
                    self.hard2 = False
                    self.hard3 = False
                    pygame.quit()
                    sys.exit()

            if self.direction_haut == True:
                self.flappy_position_y -= (self.acceleration - 2)*2
                self.acceleration = self.acceleration/(1.2)
                if self.acceleration <= 1:
                    self.direction_haut = False
                    self.direction_bas = True
                    self.acceleration = 1

            if self.direction_bas == True:
                self.flappy_position_y += (self.acceleration +2)*3
                self.acceleration = self.acceleration*(1.2)


            #pylones
            pygame.draw.rect(self.ecran, self.noir, (self.pylone[1],0, 30,self.pylone[0]))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone[1],0, 30,self.pylone[0]), self.trait)
            pygame.draw.rect(self.ecran, self.noir, (self.pylone[1], 50 + self.pylone[0] + self.pylone[2], 30, 800 - self.pylone[2] - self.pylone[0] ))
            pygame.draw.rect(self.ecran, self.rouge, (self.pylone[1], 50 + self.pylone[0] + self.pylone[2], 30, 800 - self.pylone[2] - self.pylone[0] ), self.trait)



            self.pylone[1] -= 6

            if self.pylone[1] < -30:
                self.pylone[1] = 1030
                self.pylone[0] = random.randrange(20,700 - self.pylone[2] ,1)
            
            #pylone2
            if self.count > 177/3:
                pygame.draw.rect(self.ecran,self.noir, (self.pylone2[1],0, 30,self.pylone2[0]))
                pygame.draw.rect(self.ecran,self.rouge, (self.pylone2[1],0, 30,self.pylone2[0]), self.trait)
                pygame.draw.rect(self.ecran, self.noir, (self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2], 30, 800 - self.pylone2[2] - self.pylone2[0] ))
                pygame.draw.rect(self.ecran, self.rouge, (self.pylone2[1], 50 + self.pylone2[0] + self.pylone2[2], 30, 800 - self.pylone2[2] - self.pylone2[0] ), self.trait)
                self.pylone2[1] -= 6

                if self.pylone2[1] < -30:
                    self.pylone2[1] = 1030
                    self.pylone2[0] = random.randrange(20,700 - self.pylone2[2] ,1)
                
            #pylone3
            if self.count > 177*(2/3):
                pygame.draw.rect(self.ecran, self.noir, (self.pylone3[1],0, 30,self.pylone3[0]))
                pygame.draw.rect(self.ecran, self.rouge, (self.pylone3[1],0, 30,self.pylone3[0]), self.trait)
                pygame.draw.rect(self.ecran, self.noir, (self.pylone3[1], 50 + self.pylone3[0] + self.pylone3[2], 30, 800 - self.pylone3[2] - self.pylone3[0] ))
                pygame.draw.rect(self.ecran, self.rouge, (self.pylone3[1], 50 + self.pylone3[0] + self.pylone3[2], 30, 800 - self.pylone3[2] - self.pylone3[0] ), self.trait)
                
                self.pylone3[1] -= 6

                if self.pylone3[1] < -30:
                    self.pylone3[1] = 1030
                    self.pylone3[0] = random.randrange(20,700 - self.pylone3[2] ,1)




            if self.pylone[1] <= 320 and self.pylone[1] > 50 and p1:
                p1 = False
                self.score += 1
            elif self.pylone[1] > 320:
                p1 = True

            if self.pylone2[1] <= 320 and self.pylone2[1] > 50 and p2:
                p2 = False
                self.score += 1
            elif self.pylone2[1] > 320:
                p2 = True

            if self.pylone3[1] <= 320 and self.pylone3[1] > 50 and p3:
                p3 = False
                self.score += 1
            elif self.pylone3[1] > 320:
                p3 = True

            pygame.display.flip()


game().intro()