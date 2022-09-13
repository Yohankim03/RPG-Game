import pygame, sys
from settings import *
from level import Level
from inventory import *
import random

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("RPG Game")
        self.clock = pygame.time.Clock()

        self.level = Level()

        self.player_inventory = Inventory()
        self.selected = None

        # Sound
        sound_track = pygame.mixer.Sound("audio/main.ogg")
        sound_track.set_volume(0.5)
        sound_track.play(loops = -1)


    def run(self):
        # Event Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    if event.key == pygame.K_i:
                        self.level.toggle_inventory()
                    if event.key == pygame.K_r and self.level.game_over:
                        self.level.game_over = False
                        pygame.mixer.stop()
                        game = Game()
                        game.run()
                if self.level.inventory_open:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #if right clicked, get a random item
                        if event.button == 3:
                            self.selected = [Item(random.randint(0,3)),1]
                        elif event.button == 1:
                            pos = self.player_inventory.mouse_pos()
                            if self.player_inventory.In_grid(pos[0],pos[1]):
                                if self.selected:
                                    selected = self.player_inventory.Add(selected,pos)
                                elif self.player_inventory.items[pos[0]][pos[1]]:
                                    selected = self.player_inventory.items[pos[0]][pos[1]]
                                    self.player_inventory.items[pos[0]][pos[1]] = None

            
            if self.level.game_over:
                self.level.toggle_death_screen()
            if self.level.inventory_open:
                self.player_inventory.draw()
                mousex, mousey = pygame.mouse.get_pos()
                self.player_inventory.display(mousex, mousey)
            else:
                self.screen.fill(WATER_COLOR)
                self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)
    
if __name__ == "__main__":
    game = Game()
    game.run()
