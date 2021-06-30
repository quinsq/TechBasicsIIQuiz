import pygame
import sys
import random
import pygame.font
import pygame.freetype

class MultipleChoice:

    def __init__(self,quiz):
        self.settings = quiz.settings
        self.screen = quiz.screen
        pygame.freetype.init()
        self.FONT = pygame.freetype.SysFont(None, 32)

        self.rect1 =  pygame.Rect(120, 120, 80, 300)
        self.rect2 =  pygame.Rect(120, 220, 80, 300)
        self.rect3 =  pygame.Rect(120, 320, 80, 300)
        #create text rects and save in list.
        self.rects = []
        x = 120
        y = 120
        for n in range(3):
            rect = pygame.Rect(x, y, 80, 300)
            self.rects.append(rect)
            y += 100
        #list of names to be displayed.
        self.names = [
            	'Zephyr',
                'Riley',
                'Tennessee'
                ]

    def start(self, *args):
        pass
    #draw rects, names and text on screen.
    def draw(self):
        self.FONT.render_to(self.screen, (120,50), 'which name do you like best?', pygame.Color(85, 205, 252))
        self.FONT.render_to(self.screen, (119,49), 'which name do you like best?', pygame.Color(255, 255, 255))
        self.screen.blit(self.screen, (0,0))

        n = 1
        i=0
        for rect in self.rects:
            self.FONT.render_to(self.screen, (rect.x+30, rect.y+30), str(self.names[i]), pygame.Color(247, 168, 184))
            self.FONT.render_to(self.screen, (rect.x+29, rect.y+29), str(self.names[i]), pygame.Color(255, 255, 255))
            i+=1
            n += 1

    #score name choice. dysfunctional because the rects aren't recognized.
    def score_name(self):

        self.score = 0
        for event in pygame.event.get():
            #for rect in self.rects:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect1.collidepoint(event.pos):
                #if rect.collidepoint(event.pos):
                    #if rect == self.rects[0]:
                    self.score == 1
                    print("rect1", self.score)
                elif self.rect2.collidepoint(event.pos):
                    #elif rect == self.rects[1]:
                    self.score == 2
                    print("rect2", self.score)
                elif self.rect3.collidepoint(event.pos):
                    #elif rect == self.rects[2]:
                    self.score == 3
                    print("rect3", self.score)
                #print(self.score)
                        #print(self.rects)
                        #pygame.draw.rect(self.screen, pygame.Color('darkgrey'), self.rects[i])
