import pygame
import sys

class ImageChoice:
    def __init__(self,quiz):
        self.settings = quiz.settings
        self.screen = quiz.screen
        self.FONT = pygame.freetype.SysFont(None, 32)
        image1 = pygame.image.load('dandelion.jpg')
        image2 = pygame.image.load('dan2.jpg')
        img1_rect = image1.get_rect()
        img2_rect = image2.get_rect()
        img1_rect.center = (187.5,350)
        img2_rect.center = (562.5,350)
        self.score = 0

        #detect image club and add to hypothetical score.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if img1_rect.collidepoint(event.pos):
                    self.score = 1
                elif img2_rect.collidepoint(event.pos):
                    self.score = 2
                print(self.score)
        #draw images and text on screen.
        self.screen.fill((85, 205, 252))
        self.screen.blit(image1, img1_rect)
        self.screen.blit(image2, img2_rect)
        self.FONT.render_to(self.screen, (120,50), 'in bloom or make-a-wish?', pygame.Color(247, 168, 184))
        self.FONT.render_to(self.screen, (119,49), 'in bloom or make-a-wish?', pygame.Color(255, 255, 255))
