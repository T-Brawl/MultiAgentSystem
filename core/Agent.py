class Agent(object):
    """docstring for Agent"""
    def __init__(self):
        super(Agent, self).__init__()

    def getx(self) :
        return self.x

    def gety(self) :
        return self.y
    
    def decide(self) :
        raise NotImplementedError
        
    def update(self) :
        raise NotImplementedError

    def place_agent(self,fenetre):
        raise NotImplementedError