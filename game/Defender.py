from core import Agent

class Defender(Agent.Agent):
    """docstring for Wall"""
    def __init__(self, x,y,z,t,env,defenderLife=None):
        super(Defender, self).__init__()
        self.x = x
        self.y = y
        self.env = env
        self.time = z + t if (defenderLife == None) else defenderLife
        self.cpt = 0

    def isWall(self) :
        return False

    def isAvatar(self) :
        return False

    def decide(self) :
        self.cpt += 1
        self.update()
        
    def update(self) :
        if(self.cpt == self.time):
            self.env.kill(self)

    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul='green')