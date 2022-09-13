from re import X
import pygame
from settings import *

class Screen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, 80)


    def display_death_screen(self):
        x = self.display_surface.get_size()[0] // 2 
        y = self.display_surface.get_size()[1]

        player_surf = pygame.image.load("graphics/player/dead.png").convert_alpha()
        player_surf = pygame.transform.scale2x(player_surf)
        player_rect = player_surf.get_rect(center = (x, (y // 2)-50))

        death_surf = self.font.render("Game Over!",False,"white")
        death_rect = death_surf.get_rect(center = (x,100))

        respawn_message1 = self.font.render("Press 'r'",False,"white")
        respawn_message2 = self.font.render("to restart" ,False,"white")
        respawn_message_rect1 = respawn_message1.get_rect(center = (x, y - 100))
        respawn_message_rect2 = respawn_message2.get_rect(center = (x, y - 190))


        self.display_surface.fill("black")
        self.display_surface.blit(death_surf, death_rect)
        self.display_surface.blit(player_surf, player_rect)
        self.display_surface.blit(respawn_message1, respawn_message_rect1)
        self.display_surface.blit(respawn_message2, respawn_message_rect2)

