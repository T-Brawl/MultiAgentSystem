from core import Environnement as env
from core import Agent
from core import Window as w
from core import SMA
import random
import time
from tkinter import *





class SMAWator(SMA.SMA):

    def __init__(self,gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre):
        super(SMAWator, self).__init__(gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre)
        self.fauneMax = gridSizeX * gridSizeY

        self.FULL = """Tous les requins sont morts et les poissons ont rempli le golfe.\nFin de la simulation."""

        self.EMPTY = """Les requins ont mangé tous les poissons puis sont morts de faim.\nFin de la simulation."""

    def run(self):
        super(SMAWator, self).run()

    def updateDisplay(self):
        super(SMAWator, self).updateDisplay()

        fishes = sharks = 0
        oldFish = oldShark = 0
        bebeFish = bebeShark = 0

        for agent in self.env.lesAgents:
            if agent.isFish():
                fishes += 1

                if(agent.age == 0):
                    bebeFish += 1

                if(agent.age > oldFish):
                    oldFish = agent.age
            else:
                sharks += 1

                if(agent.age > oldShark):
                    oldShark = agent.age

                if(agent.age == 0):
                    bebeShark += 1


        self.fenetre.showTicks.delete('text')   
        self.fenetre.fishStats.delete('text')   
        self.fenetre.sharkStats.delete('text')      

        self.fenetre.showTicks.create_text(100,100,text='Tour n°'+str(self.nbActualTicks),tag='text') 
        self.fenetre.fishStats.create_text(100,100,text='Poissons : {}\nDont nouveaux nés : {}\nPlus vieux poisson : {}'.format(fishes,bebeFish,oldFish),tag='text')    
        self.fenetre.sharkStats.create_text(100,100,text='Requins : {}\nDont nouveaux nés : {}\nPlus vieux requin : {}'.format(sharks,bebeShark,oldShark),tag='text')

        if((fishes == self.fauneMax) or ((fishes == 0) and (sharks == 0))):
            toplevel = Toplevel()
            label1 = Label(toplevel, text=self.FULL if (fishes == self.fauneMax) else self.EMPTY, height=0, width=100)
            label1.pack()
            toplevel.focus_force()
            self.fenetre.can.destroy()
            #self.fenetre.showTicks.destroy()   
            #self.fenetre.fishStats.destroy()   
            #self.fenetre.sharkStats.destroy() 

        #For the wild and for gnuplot
        if(self.trace):
            print("{} {} {}".format(self.nbActualTicks,fishes,sharks))

    def theloop(self):
        super(SMAWator, self).theloop()
