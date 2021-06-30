import pygame
import sys
import pygame.freetype

class NameInput:
    """name input box and originally intended scoring system."""

    def __init__(self,quiz):
        self.settings = quiz.settings
        self.screen = quiz.screen

        self.input_rect = pygame.Rect(120,300,140,56)
        self.color_active = pygame.Color(85, 205, 252)

        self.base_font = pygame.font.Font(None,48)
        self.user_text = ''
        self.filename = 'results.txt'
        self.active = False
        pygame.freetype.init()
        self.FONT = pygame.freetype.SysFont(None, 32)

    #get user text input, check it for score, and save both inputs in .txt list.
    def get_name(self):
        names = []
        self.name = self.user_text
        self.score = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_rect.collidepoint(event.pos):
                    self.active = True
                    print('active!') #only then possible to type.
                else:
                    self.active = False

            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.user_text)
                        self.user_text = ''
                        names.append(self.name)
                        print(names)
                        if self.name == self.name.lower():
                                self.score -= 1
                        elif self.name == self.name.title():
                                self.score == self.score
                        elif self.name == self.name.upper():
                                self.score += 1
                        print(self.score)
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode

        for name in names:
            with open(self.filename, 'a') as file_object:
                file_object.write(name)
                file_object.write(": ")
                file_object.write(str(self.score))
                file_object.write("\n")


    def draw(self):
        self.screen.fill((247, 168, 184))
        self.FONT.render_to(self.screen, (120,50), 'enter your name and press enter :)', pygame.Color(85, 205, 252))
        self.FONT.render_to(self.screen, (119,49), 'enter your name and press enter :)', pygame.Color(255, 255, 255))
        # Render the current text.
        txt_surface = self.base_font.render(self.user_text, True, (255,255,255))
        # Resize the box if the text is too long.
        self.width = max(200, txt_surface.get_width()+10)
        self.input_rect.w = self.width
        # Blit the text.
        self.screen.blit(txt_surface, (self.input_rect.x+5, self.input_rect.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(self.screen, self.color_active, self.input_rect, 2)
