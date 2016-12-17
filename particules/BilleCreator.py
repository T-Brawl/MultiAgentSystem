from particules import Bille as b
from core import AgentCreator

class BilleCreator(AgentCreator.AgentCreator):
    """docstring for BilleCreator"""
    def __init__(self):
        super(BilleCreator, self).__init__()

    def create(self,x,y,env,trace,indice=-1) :
        return b.Bille(indice,x,y,env,trace)
        