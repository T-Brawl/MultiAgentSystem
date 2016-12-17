from core import Environnement

class Labyrinth(Environnement.Environnement):
    """docstring for Labyrinth"""
    def __init__(self, tailleX, tailleY,torique=False):
        super(Labyrinth, self).__init__(tailleX,tailleY,torique)

    def ajouteAgent(self,agent):
        self.grille[agent.gety()][agent.getx()] = agent
        if not agent.isWall() :
            self.lesAgents.insert(0,agent) 
        #self.lesAgents.append(agent)