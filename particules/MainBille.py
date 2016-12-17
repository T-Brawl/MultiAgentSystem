import sys
sys.path.append('..')
from core import SMA
from core import Window as w
import BilleCreator as bc

gridSizeX=50
gridSizeY=50
canvasSizeX=1200
canvasSizeY=800


fenetre = w.Window(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY,boxSize=None,windowbg='ivory',title="Simulation de particules")

SMA.SMA(gridSizeX=gridSizeX
    ,gridSizeY=gridSizeY
    ,canvasSizeX=canvasSizeX
    ,canvasSizeY=canvasSizeY
    ,refresh=1
    ,scheduling="fair"
    ,nbTicks=0
    ,trace=True
    ,grid=True
    ,seed=None
    ,delay=1
    ,nbAgents=100
    ,fenetre=fenetre
    ,torique=False
    ,agentCreator=bc.BilleCreator()
    ).run()
