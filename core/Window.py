from tkinter import *


class Window(object):
    """docstring for Window"""
    def __init__(self, gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,boxSize=None,windowbg='ivory',title='Simulation'):
        super(Window, self).__init__()
        self.gridSizeX = gridSizeX
        self.gridSizeY = gridSizeY
        self.canvasSizeX = canvasSizeX
        self.canvasSizeY = canvasSizeY
        self.boxSize = boxSize
        if boxSize == None :

            self.caseX = self.canvasSizeX / self.gridSizeX
            self.caseY = self.canvasSizeY / self.gridSizeY

        else :
            self.caseX,self.caseY = boxSize

        self.tk = Tk()
        self.tk.title(title)

        self.can = Canvas(self.tk, width =self.canvasSizeX, height =self.canvasSizeY, bg = windowbg)
        self.can.pack(side=LEFT)



    
    def grille(self) :
        '''
        dessine notre magnifique grille
        '''
        for ligne in range(self.gridSizeY):
            self.can.create_line(0, ligne * self.caseY, self.canvasSizeX, ligne * self.caseY, fill ='black')  

        for colonne in range(self.gridSizeX):
            self.can.create_line(colonne * self.caseX, 0, colonne * self.caseX, self.canvasSizeY, fill ='black')  