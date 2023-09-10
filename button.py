import pygame as pg
pg.font.init()
buttonFont = pg.font.SysFont('Times New Roman', 50)
def buttonText(string, color):
    return buttonFont.render(string, True, color)

class Button():
    def __init__(self,x,y,width,height,bgColor,text,buttonCol):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.buttonCol = buttonCol
        self.rect = pg.Rect(x,y,width,height)
        self.bgColor = bgColor
        
    
    def draw(self,surface):
        pg.draw.rect(surface,self.bgColor,self.rect)
        surface.blit(buttonText(self.text,self.buttonCol),((self.x+10),(self.y+self.height/8)))
        