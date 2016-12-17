from core import Agent

class Wall(Agent.Agent):
    """docstring for Wall"""
    def __init__(self, x,y):
        super(Wall, self).__init__()
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

    def place_agent(self,fenetre):
        fenetre.can.create_rectangle(self.x*fenetre.caseX,self.y * fenetre.caseY,(self.x + 1) * fenetre.caseX,(self.y + 1) * fenetre.caseY,fill='#20265A', tag='agent')