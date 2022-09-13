import pygame
from settings import *
from random import *


class Item:
    def __init__(self,id):
        weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon["graphic"]
            weapon  = pygame.image.load(path).convert_alpha()
            weapon_graphics.append(weapon)
        self.id = id
        self.surface = weapon_graphics[id]
    
    def resize(self,size):
        return pygame.transform.scale(self.surface,(size,size))

class Inventory:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()
        self.x = 50
        self.y = 50
        self.box_size = 40
        self.border_size = 3
        self.row = 1
        self.col = 6
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.items = [[None for _ in range(self.row)] for _ in range(self.col)]
        self.selected = None

    def draw(self):
        pygame.draw.rect(self.display_surf,(100,100,100),(self.x,self.y,(self.box_size + self.border_size)*self.col + self.border_size,(self.box_size + self.border_size) + self.border_size))
        for x in range(self.col):
            for y in range(self.row):
                rect = (self.x + (self.box_size + self.border_size)*x + self.border_size,self.x + (self.box_size + self.border_size)*y + self.border_size,self.box_size,self.box_size )
                pygame.draw.rect(self.display_surf,(180,180,180),rect)
                if self.items[x][y]:
                    self.display_surf.blit(self.items[x][y][0].resize(self.box_size),rect)
                    obj = self.font.render(str(self.items[x][y][1]),True,(0,0,0))
                    self.display_surf.blit(obj,(rect[0] + self.box_size//2, rect[1] + self.box_size//2))
       
    def mouse_pos(self):
        mouse = pygame.mouse.get_pos()
        x = mouse[0] - self.x
        y = mouse[1] - self.y
        x = x//(self.box_size + self.border_size)
        y = y//(self.box_size + self.border_size)
        return (x,y)

    def add(self,Item,xy):
        x, y = xy
        if self.items[x][y]:
            if self.items[x][y][0].id == Item[0].id:
                self.items[x][y][1] += Item[1]
            else:
                temp = self.items[x][y]
                self.items[x][y] = Item
                return temp
        else:
            self.items[x][y] = Item

    def In_grid(self,x,y):
        if 0 > x > self.col-1:
            return False
        if 0 > y > self.row-1:
            return False
        return True


    def display(self, mousex, mousey):
        self.draw()
        mousex, mousey = pygame.mouse.get_pos()

        if self.selected:
            self.display_surf.blit(self.selected[0].resize(30),(mousex,mousey))
            obj = self.font.render(str(self.selected[1]),True,(0,0,0))
            self.display_surf.blit(obj,(mousex + 15, mousey + 15))

        
            