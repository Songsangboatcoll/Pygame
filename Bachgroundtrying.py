import pygame
from pygame.locals import*
import sys
import time
import random
import pyjokes

class Game:

    def __init__(self):
        self.w = 750
        self.h = 500
        self.reset = True #
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('images/type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        self.bg = pygame.image.load('images/background.jpg')
        self.bg = pygame.transform.scale(self.bg, (750, 500))
        
        pygame.mixer.init()  # Initialize the mixer

        self.screen = pygame.display.set_mode((self.w, self.h))
        self.typing_sound = pygame.mixer.Sound('sounds/typing.wav')  # Load the typing sound

        pygame.display.set_caption("Chandri's")
        


    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        sentence = pyjokes.get_joke()
        if len(sentence) <= 75:
            return sentence

    def show_results(self, screen):
        if(not self.end):

            #Calculate time
            self.total_time = time.time() - self.time_start

            #Calculate accuracy
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.word)*100

            #Calculate words per minute
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time:'+str(round(self.total_time)) + " secs   Accuracy:" + str(
                round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load('images/type-speed-open.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))

            #screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w/2-75, self.h-140))
            self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))

            print(self.results)
            pygame.display.update()

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        sentence = pyjokes.get_joke()
        if len(sentence) <= 75:
            return sentence

    def show_results(self, screen):
        if(not self.end):

            #Calculate time
            self.total_time = time.time() - self.time_start

            #Calculate accuracy
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.word)*100

            #Calculate words per minute
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time:'+str(round(self.total_time)) + " secs   Accuracy:" + str(
                round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load('images/type-speed-open.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))

            #screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w/2-75, self.h-140))
            self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))
    def run(self):
        while not self.end:
            self.reset_game()
            self.running = True
            while self.running:
                clock = pygame.time.Clock()
                self.screen.fill((0, 0, 0), (50, 250, 650, 50))
                pygame.draw.rect(self.screen, self.head_c, (50, 250, 650, 50), 2)
                # Update the caption
                pygame.display.set_caption('Type Speed test | Time left: ' +
                                           str(int(self.time_left)))
                self.draw_text(self.screen, self.word, 60, 80, self.word_font, (255, 255, 255))
                pygame.draw.rect(self.screen, (255, 192, 25), (50, 50, 650, 50), 2)

                # Update the total time text
                self.draw_text(self.screen, "Total time: " + str(int(self.total_time)), 60, 20, self.word_font, (255, 255, 255))

                self.screen.blit(self.h_image, (50, 50))
                self.screen.blit(self.h_image, (650, 50))
                self.draw_text(self.screen, self.input_text, 60, 274, self.result_font, (255, 255, 255))

                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.end = True
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        self.typing_sound.play()  # Play the typing sound
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            # Check if the input text matches the word
                            if self.input_text == self.word:
                                self.score += 1
                                self.total_time += round(time.time() - self.time_start, 2)
                            else:
                                print('Wrong input... try again')
                            self.reset_game()
                            break

                        # Join the input text
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

                pygame.display.update()

            # Calculate accuracy, words per minute and total time
            self.results = 'Total Time:' + str(round(self.total_time)) + " secs   Accuracy:" + str(
                self.accuracy) + "%" + '   Wpm: ' + str(self.wpm)

            # Show the results
            self.time_img = pygame.image.load('images/icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            # screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w/2-75, self.h-140))
            self.draw_text(screen, "Reset", self.h - 70, 26, 100, 100)


            print(self.results)
            pygame.display.update()


