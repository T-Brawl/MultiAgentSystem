import random
from tkinter import *
from core import Window


class WindowGame(Window.Window):

    def __init__(self, gridSizeX,gridSizeY,canvasSizeX,canvasSizeY):
        super(WindowGame, self).__init__(gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,boxSize=None,windowbg='black',title='Paques-Manne')

        self.debug = Canvas(self.tk, width =200, height =canvasSizeY /3, bg ='ivory')
        self.debug.pack(side=BOTTOM)

        self.score = Canvas(self.tk, width =200, height =canvasSizeY /3, bg ='ivory')
        self.score.pack(side=LEFT)