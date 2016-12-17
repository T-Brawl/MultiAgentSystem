import random
from tkinter import *
from core import Window


class Ocean(Window.Window):

    def __init__(self, gridSizeX,gridSizeY,canvasSizeX,canvasSizeY):
        super(Ocean, self).__init__(gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,boxSize=None,windowbg='#0077BE',title='Golfe du Bénin')
        self.sharkStats = Canvas(self.tk, width =200, height =canvasSizeY /3, bg ='#E4229C')
        self.sharkStats.pack(side=BOTTOM)

        self.fishStats = Canvas(self.tk, width =200, height =canvasSizeY / 3, bg ='#5F9800')
        self.fishStats.pack(side=BOTTOM)

        self.showTicks = Canvas(self.tk, width =200, height =canvasSizeY / 3, bg ='#FFFFFF')
        self.showTicks.pack(side=TOP)
