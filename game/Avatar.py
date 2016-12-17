from core import Agent
import Wall
import Hunter
import Defender
import Winner

class Avatar(Agent.Agent):

    def __init__(self, x,y,env,pace,enoughDefenders=4):
        super(Avatar, self).__init__()
        self.x = x
        self.y = y
        self.env = env
        self.bougera = True
        self.futurX = None
        self.futurY = None

        self.dirX = 0
        self.dirY = 0
        self.quatreDir = [(0,1),(0,-1),(-1,0),(1,0)]

        self.invincibility = False
        self.invincibilityCPT = 0

        self.defendersEaten = 0
        self.enoughDefenders = enoughDefenders
        self.hasWon = False

        self.pace = pace
        self.paceCPT = 0 

        self.calculeScore()

    def isWall(self) :
        return False
    def isAvatar(self) :
        return True

    def getVoisins(self,x,y) :
        lesVoisins = []
        for (pasX,pasY) in self.quatreDir :
            (futurX,futurY) = (pasX + x, pasY + y)
            if not ((futurX == -1) or (futurY == -1) or (futurX == len(self.env.grille[0])) or (futurY == len(self.env.grille))) :
                if self.env.score[futurY][futurX] == None :
                    lesVoisins.append((futurX,futurY))
        return lesVoisins

    def calculeScore(self) :
        '''
        
        '''
        self.env.score = []
        for i in range(len(self.env.grille)) :
            self.env.score.append([None] * len(self.env.grille[0]))
        self.env.score[self.y][self.x] = 0
        positions = [(self.x,self.y)]
        while not positions == []:
            tmp = []
            for (x,y) in positions :
                lesVoisins = self.getVoisins(x,y)
                for (futurX,futurY) in lesVoisins :
                    if self.env.grille[futurY][futurX] == None or not self.env.grille[futurY][futurX].isWall:
                        self.env.score[futurY][futurX] = self.env.score[y][x] + 1
                        tmp.append((futurX,futurY))
            positions = tmp[:]

    def noticeAvatar(self,dirX,dirY):
        self.dirX = dirX
        self.dirY = dirY

    def decide(self):
        
        if ((self.paceCPT % self.pace) > 0):
            self.update()
            self.bougera = False
            return

        (self.futurX,self.futurY) = (self.x + self.dirX, self.y + self.dirY)

        if self.env.torique :
            if self.futurY == -1 :
                self.futurY = len(self.env.grille)-1
            if self.futurY == len(self.env.grille) :
                self.futurY = 0
            if self.futurX == -1 :
                self.futurX = len(self.env.grille[0]) -1
            if self.futurX == len(self.env.grille[0]) :
                self.futurX = 0
        else :
            if ((self.futurY == -1) or (self.futurY == len(self.env.grille)) or (self.futurX == -1) or (self.futurX == len(self.env.grille[0]))) :
                self.bougera = False
                self.update()
                return

        if (isinstance(self.env.grille[self.futurY][self.futurX],Wall.Wall)):
            self.bougera = False
        else:
            self.bougera = True

        self.update()


    def update(self) :

        self.paceCPT += 1

        if(self.invincibility):
            if(self.invincibilityCPT == 0):
                self.invincibility = False
                for agent in self.env.lesAgents:
                    if(isinstance(agent,Hunter.Hunter)):
                        agent.doitFuir = False  

        if(self.invincibility > 0):
            self.invincibilityCPT -= 1

        if self.bougera :

            if ((self.env.grille[self.futurY][self.futurX] != None) and isinstance(self.env.grille[self.futurY][self.futurX],Hunter.Hunter)):
                chasseur = self.env.grille[self.futurY][self.futurX]
                if(chasseur.doitFuir):
                    self.env.kill(chasseur)
                else:
                    self.env.kill(self)
                    return

            if ((self.env.grille[self.futurY][self.futurX] != None) and isinstance(self.env.grille[self.futurY][self.futurX],Defender.Defender)):
                powerUp = self.env.grille[self.futurY][self.futurX]
                self.invincibilityCPT = len(self.env.grille[0]) + len(self.env.grille)
                self.invincibility = True
                self.env.kill(powerUp)
                self.defendersEaten += 1
                for agent in self.env.lesAgents:
                    if(isinstance(agent,Hunter.Hunter)):
                        agent.doitFuir = True      

            if ((self.env.grille[self.futurY][self.futurX] != None) and isinstance(self.env.grille[self.futurY][self.futurX],Winner.Winner)):
                self.env.kill(self.env.grille[self.futurY][self.futurX])
                self.hasWon = True              

            self.env.grille[self.y][self.x] = None
            self.env.grille[self.futurY][self.futurX] = self
            self.x = self.futurX
            self.y = self.futurY
            self.calculeScore()


    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul='#FFEE00')