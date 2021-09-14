from tkinter import *
from numpy.random.mtrand import randint
from functions import *
import matplotlib.pyplot as plt
import numpy as np
#Para criar a figura onde será plotado o gráfico:
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
root = Tk()

graficOn = False


def On():
    global graficOn 
    graficOn = True





# ------------------------------------------------------------------------------------------

class Aplication():
    def __init__(self):
        self.root = root

        self.screen()
        self.grafic1()
        self.grafic2()
        self.grafic3()
        self.frameScreen()
        self.buttonsFrame()
        
        self.root.mainloop()
    
    def screen(self):
        self.root.title("Dados")
        self.root.configure(background='lightblue')
        self.root.resizable(True, True) #Responsividade
        self.root.geometry("900x700")

    def grafic1(self):
        
        #criando uma figura:
        figure1 = plt.Figure()
        ax = figure1.add_subplot(111)
        ax.set_title('Serial Data')
        ax.set_xlim(0,100)
        ax.set_ylim(-0.5,6)
        lines1 = ax.plot([],[])[0]

        canva = FigureCanvasTkAgg(figure1, master = root) #Instancia a figura dentro da janela  
        canva.get_tk_widget().place(relx=0.025, rely=0.05,
                                    relwidth=0.30, relheight=0.30)# Tamnaho e posição na tela
        canva.draw()

    def grafic2(self):
        
        #criando uma figura:
        figure2 = plt.Figure()
        ax = figure2.add_subplot(111)
        ax.set_title('Serial Data')
        ax.set_xlim(0,100)
        ax.set_ylim(-0.5,6)
        lines2 = ax.plot([],[])[0]

        canva = FigureCanvasTkAgg(figure2, master = root) #Instancia a figura dentro da janela  
        canva.get_tk_widget().place(relx=0.350, rely=0.05,
                                    relwidth=0.30, relheight=0.30)# Tamnaho e posição na tela
        canva.draw()

    def grafic3(self):
        
        #criando uma figura:
        figure3 = plt.Figure()
        ax = figure3.add_subplot(111)
        ax.set_title('Serial Data')
        ax.set_xlim(0,100)
        ax.set_ylim(-0.5,6)
        lines3 = ax.plot([],[])[0]

        canva = FigureCanvasTkAgg(figure3, master = root) #Instancia a figura dentro da janela  
        canva.get_tk_widget().place(relx=0.675, rely=0.05,
                                    relwidth=0.30, relheight=0.30)# Tamnaho e posição na tela
        canva.draw()

    def frameScreen(self):
        self.frame1 = Frame(self.root, bd= 4, bg = "blue")
        self.frame1.place(relx=0.05, rely=0.6, relwidth=0.90, relheight=0.20)

    def buttonsFrame(self):
        #Start
        self.bt1 = Button(self.frame1, text="Start", font = ('calbiri',12),
                command = lambda: On())
        self.bt1.place(relx=0.2, rely=0.5, relwidth=0.1, relheight=0.15, width=20, height=20)

        #Stop
        self.bt2 = Button(self.frame1, text="Stop", font = ('calbiri',12))
        self.bt2.place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.15, width=20, height=20)
        
        #botão Novo
        self.bt3 = Button(self.frame1, text="Botão 3", font = ('calbiri',12))
        self.bt3.place(relx=0.6, rely=0.5, relwidth=0.1, relheight=0.15, width=20, height=20)


Aplication() 


