import sys
sys.path.append('..')

import SMAWator as sma
import Ocean as o
import FishAndSharkCreator as wildLife



gridSizeX=50
gridSizeY=50
canvasSizeX=800
canvasSizeY=600
nbFish=200
nbShark=5
fishBreedTime=2
sharkBreedTime=10
sharkStarveTime=3

ocean = o.Ocean(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY)

sma.SMAWator(gridSizeX=gridSizeX
    ,gridSizeY=gridSizeY
    ,canvasSizeX=canvasSizeX
    ,canvasSizeY=canvasSizeY
    ,refresh=1
    ,scheduling="fair"
    ,nbTicks=0
    ,trace=False
    ,grid=False
    ,seed=None
    ,delay=1
    ,nbAgents=nbFish+nbShark
    ,fenetre=ocean
    ,torique=True
    ,agentCreator=wildLife.FishAndSharkCreator(nbFish,nbShark,fishBreedTime,sharkBreedTime,sharkStarveTime)
    ).run()
