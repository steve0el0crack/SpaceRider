#SpaceRider

#PRINCIAL CLASS
class Player():
    #Set PRINCIPAL values ----> Position, Activation keys and color
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
    
    
    def bewegung(self, key):
        if key == self.tasten[0]:
            print key
            self.x = self.x - 1
        if key == self.tasten[1]:
            print key
            self.y = self.y - 1
        if key == self.tasten[2]:
            print key
            self.x = self.x + 1
        if key == self.tasten[3]:
            print type(key)
            self.y = self.y + 1
        if type(key) == "unicode":
            self.present(mouseX, mouseY)
        
        self.present(self.x, self.y)
        #print type(key)
            
Yassin = Player("a w d s", (255, 0, 0))
Esteban = Player("j i l k", (0, 0, 255))

def setup():
    size(500, 500)
    background(255)
    
    Yassin.present(height,0 )
    Esteban.present(0, height)
    
    
def draw():
    if keyPressed == True:
        print "--"
        Yassin.bewegung(key)
    Esteban.bewegung(key)
        
