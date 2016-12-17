from core import AgentCreator
import Avatar as a
import Wall as w
import Hunter as h

class GameAgentCreator(AgentCreator.AgentCreator):

    def __init__(self, gridSizeX,gridSizeY, nbWalls, nbHunters, hunterSpeed, avatarSpeed, enoughDefenders):
        super(GameAgentCreator, self).__init__()
        self.nbWalls = nbWalls
        self.nbAvatar = 1
        self.nbHunters = nbHunters
        self.hunterSpeed = hunterSpeed
        self.avatarSpeed = avatarSpeed
        self.enoughDefenders = enoughDefenders

    def create(self,x,y,env,trace,indice=-1):
        if self.nbWalls > 0 :
            self.nbWalls -= 1
            return w.Wall(x,y)
        elif self.nbHunters > 0 :
            self.nbHunters -=1
            return h.Hunter(x,y,env,self.hunterSpeed)
        else :
            return a.Avatar(x,y,env,self.avatarSpeed,self.enoughDefenders)