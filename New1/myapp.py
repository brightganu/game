#snake game

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init __(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
    
    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes=false):
        pass
    
    
class snake(object):
    def __init__(self, color, pos):
        pass
    
    def move(slef)
        pass
    
    def reset(self, pos):
        pass
    
    def addCube(self):
        pass
    
    def draw(self, surface):
        pass
        
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        
        pygame.draw.line(surface, (255,255,255,), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255,), (0,y), (w,y))
        
    
    
    
def redrawWindow(surface):
    global rows, width
    win.fill((0,0,0))
    drawGrid(width,rows,surface)
    pygame.display.update()
    
def randomSnack(rows, items):
    pass
    
def message_box(subject, content):
    pass
    
def main():
    global width, rows
    width = 500
    heigh = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake ((255,0,0) (10,10))
    flag = True
    
    clock = pygame.time.clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        reddrawWindow(win)
        
        
        pass

rows =
w =
h =

cube.rows = rows
cube.w = w

main()  
    