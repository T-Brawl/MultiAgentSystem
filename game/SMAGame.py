from core import Environnement as env
from core import Agent
from core import Window as w
from core import SMA
import Wall 
import Winner
import Defender
import Avatar
import Hunter
import random
import time
from tkinter import *


class SMAGame(SMA.SMA):

    def __init__(self,gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre,defenderLife=None):
        super(SMAGame, self).__init__(gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,grid,nbTicks,trace,seed,refresh,nbAgents,torique,agentCreator,fenetre)

        self.nbAgentsMax = gridSizeX * gridSizeY
        self.gridSizeX = gridSizeX
        self.gridSizeY = gridSizeY

        self.winnerSpawn = False

        self.NOAVATAR = """Un chasseur a mangé votre avatar, fin de la partie.\nNombre de tours : """

        self.NOHUNTERS = """Vous avez mangé tous les chasseurs, fin de la partie.\nNombre de tours : """

        self.WINNER = """YOU WIN !\nNombre de tours : """

        self.defenderLife = defenderLife

        self.fenetre.can.focus_set()
        self.fenetre.can.bind("<Left>",self.avatarLeft)
        self.fenetre.can.bind("<Right>",self.avatarRight)
        self.fenetre.can.bind("<Up>",self.avatarUp)
        self.fenetre.can.bind("<Down>",self.avatarDown)
        self.fenetre.can.bind("a",self.speedUpHunter)
        self.fenetre.can.bind("z",self.speedDownHunter)
        self.fenetre.can.bind("o",self.speedUpAvatar)
        self.fenetre.can.bind("p",self.speedDownAvatar)
        self.fenetre.can.pack()


    def theloop(self):

        self.nbActualTicks = self.nbActualTicks + 1

        if( ((self.nbAgentsMax - len(self.env.lesAgents)) > (0.01 * self.nbAgentsMax)) and (random.random() < 0.1)):
            self.popDefender()

        # Chaque agent décide de sa nouvelle position.
        if self.scheduling in ("chaos","unfair","rand","aleatoire","alea","aléatoire"):
            for i in range(len(self.env.lesAgents)):
                agent = random.choice(self.env.lesAgents)
                agent.decide()
                if((not self.winnerSpawn) and (self.nbAgentsMax > len(self.env.lesAgents)) and isinstance(agent,Avatar.Avatar) and (agent.defendersEaten >= agent.enoughDefenders)):
                    self.popWinner()
                    self.winnerSpawn = True
        elif self.scheduling in ("fair"):
            random.shuffle(self.env.lesAgents)
            for agent in self.env.lesAgents:
                agent.decide()
                if((not self.winnerSpawn) and (self.nbAgentsMax > len(self.env.lesAgents)) and isinstance(agent,Avatar.Avatar) and (agent.defendersEaten >= agent.enoughDefenders)):
                    self.popWinner()
                    self.winnerSpawn = True
        else:
            for agent in self.lesAgents:
                agent.decide()
                if((not self.winnerSpawn) and (self.nbAgentsMax > len(self.env.lesAgents)) and isinstance(agent,Avatar.Avatar) and (agent.defendersEaten >= agent.enoughDefenders)):
                    self.popWinner()
                    self.winnerSpawn = True

        self.updateDisplay()

        # Terminaison
        # 0 = infini
        # Sinon voir si on a atteint le nombre de ticks demandés par l'utilisateur
        
        if((self.nbTicks==0) or (self.nbActualTicks < self.nbTicks)):
            self.fenetre.can.after(self.delay,self.theloop)
        else :
            self.fenetre.tk.destroy()

    def updateDisplay(self):
        super(SMAGame, self).updateDisplay()

        avatar = 0
        hunters = 0
        avatarSpeed = 0
        hunterSpeed = 0
        defendersEaten = 0 
        enoughDefenders = 0
        invincibility = 0
        winner = False

        for agent in self.env.lesAgents:
            if isinstance(agent,Avatar.Avatar):
                avatar += 1                
                defendersEaten = agent.defendersEaten                
                enoughDefenders = agent.enoughDefenders
                avatarSpeed = 1 / agent.pace
                invincibility = agent.invincibilityCPT
                winner = agent.hasWon
                continue
            if isinstance(agent,Hunter.Hunter):
                hunters += 1
                hunterSpeed = 1 / agent.pace
                continue

        if((avatar == 0) or (hunters == 0) or winner):
            if (avatar == 0):
                popup = self.NOAVATAR
            elif (hunters == 0):
                popup = self.NOHUNTERS
            else:
                popup = self.WINNER
            toplevel = Toplevel()
            label1 = Label(toplevel, text=popup+str(self.nbActualTicks), height=0, width=100)
            label1.pack()
            toplevel.focus_force()
            self.fenetre.can.destroy()

        self.fenetre.score.delete('text')
        self.fenetre.debug.delete('text')      

        self.fenetre.score.create_text(100,100,text="Score : {} / {} Defender".format(defendersEaten,enoughDefenders),tag='text')
        self.fenetre.debug.create_text(100,100,text="Vitesse de l'avatar : {}%\nVitesse des chasseurs : {}%\nInvincibility : {}".format(round(avatarSpeed * 100,2),round(hunterSpeed * 100,2),invincibility),tag='text') 

    def avatarLeft(self,event):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar.Avatar)):
                agent.noticeAvatar(-1,0)

    def avatarRight(self,event):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar.Avatar)): 
                agent.noticeAvatar(1,0)

    def avatarUp(self,event):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar.Avatar)): 
                agent.noticeAvatar(0,-1)

    def avatarDown(self,event):
        for agent in self.env.lesAgents:
            if (isinstance(agent,Avatar.Avatar)): 
                agent.noticeAvatar(0,1)

    def popDefender(self):
        a = random.randint(0, len(self.env.grille) - 1)
        b = random.randint(0, len(self.env.grille[0]) - 1)
        while( not (self.env.grille[a][b] == None) ):
            a = random.randint(0, len(self.env.grille) - 1)
            b = random.randint(0, len(self.env.grille[0]) - 1)

        power = Defender.Defender(b,a,self.gridSizeX,self.gridSizeY,self.env,self.defenderLife)
        self.env.ajouteAgent(power)

    def popWinner(self):
        a = random.randint(0, len(self.env.grille) - 1)
        b = random.randint(0, len(self.env.grille[0]) - 1)
        while( not (self.env.grille[a][b] == None) ):
            a = random.randint(0, len(self.env.grille) - 1)
            b = random.randint(0, len(self.env.grille[0]) - 1)

        power = Winner.Winner(b,a)
        self.env.ajouteAgent(power)

    def speedUpHunter(self,event):
        for agent in self.env.lesAgents:
            if isinstance(agent,Hunter.Hunter):
                if(agent.pace <= 1):
                    agent.pace = 1
                else:
                    agent.pace -= 1

    def speedDownHunter(self,event):
        for agent in self.env.lesAgents:
            if isinstance(agent,Hunter.Hunter):
                agent.pace += 1

    def speedUpAvatar(self,event):
        for agent in self.env.lesAgents:
            if isinstance(agent,Avatar.Avatar):
                if(agent.pace <= 1):
                    agent.pace = 1
                else:
                    agent.pace -= 1
                break

    def speedDownAvatar(self,event):
        for agent in self.env.lesAgents:
            if isinstance(agent,Avatar.Avatar):
                agent.pace += 1
                break