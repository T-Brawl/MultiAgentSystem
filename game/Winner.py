from core import Agent

class Winner(Agent.Agent):
    """docstring for Wall"""
    def __init__(self, x,y):
        super(Winner, self).__init__()
        self.x = x
        self.y = y

    def isWall(self) :
        return False

    def isAvatar(self) :
        return False

    def decide(self) :
        pass
        
    def update(self) :
        pass

    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul='#00BFFF')