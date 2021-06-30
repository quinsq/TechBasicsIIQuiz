import pygame
import sys
import webbrowser
import logging

from settings import Settings
from button import PlayButton
from name_input import NameInput
from img_choice import ImageChoice
from multiple_choice import MultipleChoice


class Quiz:
    """overall class to manage game."""

    def __init__(self):
        """intialize game and set variables."""
        pygame.init()
        self.settings = Settings()
        #display settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #self.screen = attribute, available in all methods of the class
        pygame.display.set_caption("quiz")
        #class variables
        self.play_button = PlayButton(self, "play!")
        self.name = NameInput(self)
        self.image = ImageChoice(self)
        self.mc = MultipleChoice(self)

    def run_game(self): #main method
        clock = pygame.time.Clock()
        done = False #running
        #start with play button NOT rounds
        self.round_name = False
        self.round_img = False
        self.round_mc = False


        while True:
            #initiate play button
            self.check_events()
            self.update_screen()
            #get user name input
            if self.round_name:
                self.name.draw()
                self.name.get_name()
                #set round_img to True
                self.next_round()
            #play round_img and set round_mc to True
            if self.round_img:
                self.image.__init__(self)
                self.next_round()
            #play round_mc and open playlist.
            if self.round_mc:
                self.mc.draw()
                self.mc.score_name()
                self.next_round()

            pygame.display.flip()

            clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_play_button(self, mouse_pos):
        """start game when player clicks play."""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked: #start with round_name (set to True)
            self.round_name = True
            self.round_img = False
            self.round_mc = False

    def next_round (self):
        """handles what happens after each round is done."""

        self.next_round_rect = pygame.Rect(600,550,140,32)
        self.button_color = (85, 205, 252)
        self.text_color = (255, 255, 255)
        self.base_font = pygame.font.Font(None,48)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.next_round_rect.collidepoint(event.pos):
                    if self.round_name:
                        self.round_name = False
                        self.round_img = True
                        self.round_mc = False
                    elif self.round_img:
                        self.round_name = False
                        self.round_img = False
                        self.round_mc = True
                    elif self.round_mc:
                        self.round_name = False
                        self.round_img = False
                        self.round_mc = False
                        webbrowser.open('https://open.spotify.com/playlist/2vZBxvnJjQpbPbSmLXXmc4?si=f50f9fabe2a14335')
        #draw onwards button
        self.screen.fill((255, 255, 255), self.next_round_rect)
        next_round_surface = self.base_font.render('onwards!', True, self.text_color, self.button_color)

        self.screen.blit(next_round_surface, (self.next_round_rect.x,self.next_round_rect.y))

    def update_screen(self):
        """update images on the screen, and flip to new screen."""
        #draw screen when first starting the game.
        self.screen.fill(self.settings.bg_color)
        #draw the play button if game is inactive.
        if not self.round_name or self.round_mc or self.round_img:
            self.play_button.draw_button()

if __name__ == '__main__':
    #make a game instance and run the game.
    quiz = Quiz()
    quiz.run_game()
