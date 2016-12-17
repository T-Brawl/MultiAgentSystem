import sys
sys.path.append('..')

import SMAGame as sma
from core import Window as w
import WindowGame
import GameAgentCreator as ga


gridSizeX=50
gridSizeY=50
canvasSizeX=800
canvasSizeY=600

nbWalls = 128
nbHunters = 10
hunterSpeed = 10
avatarSpeed = 1

enoughDefenders = 4
defenderLife = 100

initGame = ga.GameAgentCreator(gridSizeX,gridSizeY,nbWalls,nbHunters,hunterSpeed,avatarSpeed,enoughDefenders)
#fenetre = w.Window(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY,boxSize=None,windowbg='black',title="Simulation de particules")
fenetre = WindowGame.WindowGame(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY)

sma.SMAGame(gridSizeX=gridSizeX
    ,gridSizeY=gridSizeY
    ,canvasSizeX=canvasSizeX
    ,canvasSizeY=canvasSizeY
    ,refresh=1
    ,scheduling="fair"
    ,nbTicks=0
    ,trace=False
    ,grid=False
    ,seed=None
    ,delay=100
    ,nbAgents=nbHunters + nbWalls+ 1#initGame.nbAgents()
    ,fenetre=fenetre
    ,torique=True
    ,agentCreator=initGame
    ,defenderLife=defenderLife
    ).run()