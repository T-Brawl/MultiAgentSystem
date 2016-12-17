from core import Agent
import random

class Shark(Agent.Agent):
    """docstring for Shark"""
    def __init__(self, x,y,env,trace,sharkBreedTime,dontStarve):
        super(Shark, self).__init__()
        self.env = env
        self.x = x
        self.y = y
        self.trace = trace
        self.sharkBreedTime = sharkBreedTime
        self.sharkBreedTimeCPT = sharkBreedTime
        self.dontStarve = dontStarve
        self.dontStarveCPT = dontStarve
        self.bougera = True
        self.naissance = False
        self.killMe = False
        self.futurX = None
        self.futurY = None
        self.age = 0
        self.color = "HotPink1"

    def isFish(self) :
        return False

    
    def genereListPasAlea(self):
        ref = [0,1,-1]
        resultat = []
        for x in ref :
            for y in ref :
                if x == y == 0 :
                    continue
                resultat.append((x,y))
        random.shuffle(resultat)
        return resultat

    
    def pasToPosition(self,listePas) :
        '''
        transforme une liste de pas en une liste de position relative à self et l'environnement
        il peut y avoir plusieurs position qui se répète dans un monde non torique mais c'est pas grave
        '''
        resultat = []
        for (pasX,pasY) in listePas :
            futurX = self.x + pasX
            futurY = self.y + pasY
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
            resultat.append((futurX,futurY))
        return resultat

    def randomNextPos(self):
        """
        Légère modification, exploration aléatoire non redondante du voisinnage de Moore,
        Si le Shark trouve un Fish à proximité, il fonce dessus.
        Sinon le Shark prend dans une direction aléatoire. 
        """
        listePas = self.genereListPasAlea()
        listePositions = self.pasToPosition(listePas)
        for (futurX,futurY) in listePositions :
            if self.env.grille[futurY][futurX] == None :
                continue
            elif self.env.grille[futurY][futurX].isFish() :
                return (futurX,futurY)
            else : # on rencontre un requin
                listePositions.remove((futurX,futurY))
        if listePositions == 0 :
            return None

        return listePositions[0] # qui est bien une position aléatoire

    def decide(self) :
        """
        on choisis un pas random et on observe si il y a un obstacle ou pas
        """

        #Mort du requin s'il n'a pas mangé à temps
        if self.dontStarveCPT == 0:
        	self.killMe = True
        	self.update()
        	return

        #Naissance ou pas
        if self.sharkBreedTimeCPT == 0 :
            self.naissance = True
            self.sharkBreedTimeCPT = self.sharkBreedTime
        else :
            self.sharkBreedTimeCPT = self.sharkBreedTimeCPT - 1


        #Pourra-t-il bouger ? 3 cas possibles
        (self.futurX,self.futurY) = self.randomNextPos()

        #1. Il peut manger un possion et donc aller vers lui
        if ((self.env.grille[self.futurY][self.futurX] != None) and self.env.grille[self.futurY][self.futurX].isFish()):
            self.bougera = True
            self.dontStarveCPT = self.dontStarve
            self.update()
            return

        #2 et 3. Qu'il bouge ou pas, s'il n'a pas vu de poisson, il a faim
        self.dontStarveCPT = self.dontStarveCPT - 1
        
        #2. Un requin le bloque
        if (isinstance(self.env.grille[self.futurY][self.futurX],Shark)) :
            self.bougera = False
        else :
            #3. Case vide
            self.bougera = True

        self.update()



    def update(self) :

        if self.killMe:
            self.env.kill(self)
            return

        if self.bougera :

            self.env.grille[self.y][self.x] = None

            #Manger le poisson
            if ((self.env.grille[self.futurY][self.futurX] != None) and self.env.grille[self.futurY][self.futurX].isFish()):
                self.env.kill(self.env.grille[self.futurY][self.futurX])

            if self.naissance :
                babyRage = Shark(self.x,self.y,self.env,self.trace,self.sharkBreedTime,self.dontStarve)
                self.env.ajouteAgent(babyRage)
                self.naissance = False

            self.env.grille[self.futurY][self.futurX] = self
            
            self.x = self.futurX
            self.y = self.futurY

        self.age += 1
        self.color = "red"



    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul=self.color)