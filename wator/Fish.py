from core import Agent
import random as r

class Fish(Agent.Agent):
    """docstring for Fish"""
    def __init__(self,x,y,env,trace,fishBreedTime):
        super(Fish, self).__init__()
        self.env = env
        self.x = x
        self.y = y
        self.trace = trace
        self.fishBreedTime = fishBreedTime
        self.fishBreedTimeCPT = fishBreedTime
        self.bougera = True
        self.naissance = False
        self.futurX = None
        self.futurY = None
        self.age = 0
        self.color = "green"

    def isFish(self):
        return True

    def randomNextPos(self) :
        lesPas = [-1,0,1]
        lesPas2LeRetour = [-1,1]
        futurX = self.x + r.choice(lesPas)
        if futurX == self.x :
            futurY = self.y + r.choice(lesPas2LeRetour)
        else :
            futurY = self.y + r.choice(lesPas)
        if self.env.torique :
            if futurY == -1 :
                futurY = len(self.env.grille)-1
            if futurY == len(self.env.grille) :
                futurY = 0
            if futurX == -1 :
                futurX = len(self.env.grille[0]) -1
            if futurX == len(self.env.grille[0]) :
                futurX = 0
        else :
            if futurY == -1 :
                futurY = 1
            if futurY == len(self.env.grille) :
                futurY = len(self.env.grille)-2
            if futurX == -1 :
                futurX = 1
            if futurX == len(self.env.grille[0]) :
                futurX = len(self.env.grille[0])-2
        return (futurX,futurY)

    def decide(self) :
        """
        on choisis un pas random et on observe si il y a un obstacle ou pas
        """
        (self.futurX,self.futurY) = self.randomNextPos()
        if self.fishBreedTimeCPT == 0 :
            self.naissance = True
            self.fishBreedTimeCPT = self.fishBreedTime
        else :
            self.fishBreedTimeCPT = self.fishBreedTimeCPT - 1

        if self.env.grille[self.futurY][self.futurX] == None :
            self.bougera = True
        else :
            self.bougera = False

        self.update()



    def update(self) :
        """
        """
        if self.bougera :

            self.env.grille[self.y][self.x] = None

            if self.naissance :
                babyRage = Fish(self.x,self.y,self.env,self.trace,self.fishBreedTime)
                self.env.ajouteAgent(babyRage)
                self.naissance = False

            self.env.grille[self.futurY][self.futurX] = self
            self.x = self.futurX
            self.y = self.futurY

        self.age += 1
        self.color = "blue"

        
        
    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul=self.color)