#SpaceRider

import math


#PRINCIAL CLASS
class Player():
    #Set PRINCIPAL values ----> Position, Activation keys and color
    derweg = []
    x = ""
    y = ""
    tasten = ""
    farbe = ""
    def __init__(self, tastenstr, farbliste):
        self.tasten = tastenstr.split(" ")
        print self.tasten
        self.farbe = farbliste
    
    #For rendering onto the world
    def present(self, x, y):
        fill(self.farbe[0], self.farbe[1], self.farbe[2])
        circle(x, y, 20)
        self.x = x
        self.y = y
    
    def getpos(self):
        return self.x, self.y
    
    def keyboardbewegung(self, key):
        if key == self.tasten[0]:
            self.x = self.x - 1
        if key == self.tasten[1]:           
            self.y = self.y - 1
        if key == self.tasten[2]:
            self.x = self.x + 1
        if key == self.tasten[3]:
            self.y = self.y + 1
        
        self.present(self.x, self.y)
        self.derweg.append([self.x, self.y])
        print self.derweg
    
    def mousebewegung(self, v):
        #KATETEN
        varx = mouseX - self.x 
        vary = mouseY - self.y
        distance = math.sqrt(varx**2 + vary**2)
        
        schrittn = distance / v
        xschritt = varx/v
        yschritt = vary/v
        
        self.x = self.x + xschritt
        self.y = self.y + yschritt
        self.present(self.x, self.y)
        self.derweg.append([self.x, self.y])
        print self.derweg
                
Yassin = Player("a w d s", (255, 0, 0))
Esteban = Player("", (0, 0, 255))

def setup():
    size(500, 500)
    background(255)
    
    Yassin.present(height,0 )
    Esteban.present(height, -width)
    
    
def draw():
    Esteban.mousebewegung(1)
    if keyPressed == True:
        print "--"
        Yassin.keyboardbewegung(key)
        
    if Yassin.getpos() == Esteban.getpos():
        print "VERLOREN"
