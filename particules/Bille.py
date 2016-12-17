import random
import State as s
from core import Agent


class Bille(Agent.Agent):
    """
    docstring for Bille

    Une bille possède une couleur 

    """
    def __init__(self,indice, x,y,env,trace):
        super(Bille, self).__init__()
        self.color = "#%06x" % random.randint(0, 0xFFFFFF)
        self.indice = indice
        lesDirections = [(0,-1),(0,1),(1,-1),(1,1),(1,-1),(1,1),(-1,-1),(-1,1)]
        direction = random.choice(lesDirections)
        self.state = s.State(x,y,direction)
        self.env = env
        self.trace = trace

    def getx(self) :
        return self.state.x

    def gety(self) :
        return self.state.y

    def update(self):
        if self.state.bougera :
            self.env.grille[self.state.y][self.state.x] = None
            self.env.grille[self.futurY][self.futurX] = self
            self.state.x = self.futurX
            self.state.y = self.futurY
    
    def collision(self,bille) :
        '''
        En cas de collision avec une autre bille les deux
        s'échangent leur direction. 
        '''
        if self.trace :
            print("Colision de la bille "+str(self.indice)+" avec la bille "+str(bille.indice)+" en ("+str(bille.state.x)+","+str(bille.state.y)+")")
        self.state.bougera = False
        bille.state.bougera = False
        direction_tmp = self.state.direction
        self.state.direction = bille.state.direction
        bille.state.direction = direction_tmp 


    def nextPos(self) :
        '''
        Une direction est un couple d'int qui est sauvegardé dans l'objet State.
        '''
        (futurX,futurY) = (self.state.x + self.state.direction[0],self.state.y + self.state.direction[1])
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
            list_direction = list(self.state.direction)
            if futurX == -1 :
                futurX = 1
                list_direction[0] = - list_direction[0]
            if futurX == len(self.env.grille[0]) :
                futurX = len(self.env.grille[0]) - 2
                list_direction[0] = - list_direction[0]
            if futurY == -1 :
                futurY = 1  
                list_direction[1] = - list_direction[1]
            if futurY == len(self.env.grille) :
                futurY = len(self.env.grille) - 2
                list_direction[1] = - list_direction[1]
            self.state.direction = tuple(list_direction)

        return (futurX,futurY)
        
    def decide(self) :
        """
        Deux cas de figure, la bille perçoit où elle doit aller :
            soit c'est libre : elle garde sa direction et avancera à l'update
            soit c'est occupé : elle inverse sa direction et n'avancera pas à l'update
        """
        futurX,futurY = self.nextPos()
        if self.env.grille[futurY][futurX] == None :
            #signifie donc que la voie est libre !
            self.state.bougera = True
        else :
            #du coup occupé
            self.state.bougera = False
            self.collision(self.env.grille[futurY][futurX])
        self.futurX = futurX
        self.futurY = futurY
        self.update()


    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.state.x*fenetre.caseX + fenetre.caseX/2, self.state.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul=self.color)
        if(not (self.indice == None)):
            fenetre.can.create_text(self.state.x*fenetre.caseX + fenetre.caseX/2,self.state.y * fenetre.caseY + fenetre.caseY / 2,text=str(self.indice),tag='text')

