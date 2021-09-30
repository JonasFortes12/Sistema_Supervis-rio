from tkinter import *
import tkinter
# from numpy.lib.function_base import select
from functions import *
import matplotlib.pyplot as plt
#Para criar a figura onde será plotado o gráfico:
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

root = Tk()

root.title("Dados")
root.configure(background='#371E30')
root.resizable(True, True) #Responsividade
root.geometry("1200x700")


dataTension = loadingDataTension()
dataCurrent = loadingDataCurrent()
dataInput = loadingDataInput()
#variáveis do intervalo dos graficos
a = 0
b = len(dataTension)

#criando uma figura 1:
figure1 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
g1 = figure1.add_subplot(111) #Coloca a figura dentro da variavel grafico
g1.set_title('Serial Data')
g1.set_xlabel('Sample')
g1.set_ylabel('Tension')
g1.set_xlim(a, b)
g1.set_ylim(-1,4)

lines1 = g1.plot([],[])[0]

canva1 = FigureCanvasTkAgg(figure1, master = root) #Instancia a figura dentro da janela  
canva1.get_tk_widget().place(relx=0.025, rely=0.2,
                                relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
canva1.draw()

#criando a figura 2:
figure2 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
g2 = figure2.add_subplot(111) #Coloca a figura dentro da variavel grafico
g2.set_title('Serial Data')
g2.set_xlabel('Sample')
g2.set_ylabel('Current')
g2.set_xlim(a, b)
g2.set_ylim(-0.01,0.015)
lines2 = g2.plot([],[])[0]

canva2 = FigureCanvasTkAgg(figure2, master = root) #Instancia a figura dentro da janela  
canva2.get_tk_widget().place(relx=0.350, rely=0.2,
                                relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
canva2.draw()

#criando a figura 3:
figure3 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
g3 = figure3.add_subplot(111) #Coloca a figura dentro da variavel grafico
g3.set_title('Serial Data')
g3.set_xlabel('Sample')
g3.set_ylabel('Input')
g3.set_xlim(a, b)
g3.set_ylim(-1,3)
lines3 = g3.plot([],[])[0]

canva3 = FigureCanvasTkAgg(figure3, master = root) #Instancia a figura dentro da janela  
canva3.get_tk_widget().place(relx=0.675, rely=0.2,
                                relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
canva3.draw()


i = 1 #eixo x
j = 0 #eixo y
on = False


xTension = []
xCurrent = []
xInput = []
yTension = []
yCurrent = []
yInput = []


def update_data():
    global i, j, a, b
    if(j<len(dataTension)):
        xTension.append(i)
        yTension.append(dataTension[j])
        
        xCurrent.append(i)
        yCurrent.append(dataCurrent[j])
        
        xInput.append(i)
        yInput.append(dataInput[j])
        i = i+1
        j = j+1
        if(i>b):
            a = a + 1
            b = b + 1
            g1.set_xlim(a, b)
            g2.set_xlim(a, b)
            g3.set_xlim(a, b)

    else:
        j = 0

def plot_data():
    if(on == True):
        update_data()
        
        lines1.set_xdata(xTension)
        lines1.set_ydata(yTension)
            
        lines2.set_xdata(xCurrent)
        lines2.set_ydata(yCurrent)
            
        lines3.set_xdata(xInput)
        lines3.set_ydata(yInput)
            
        canva1.draw()
        canva2.draw()
        canva3.draw()
            
        root.after(1,plot_data)
    else:
        root.after(1,plot_data)

def onOf():
    global on
    on = not on

def restart():
    global xTension, xCurrent, xInput, yCurrent, yTension, yInput, i, j, a, b, on
    xTension = []
    xCurrent = []
    xInput = []
    yTension = []
    yCurrent = []
    yInput = []
    i = 1 #eixo x
    j = 0 #eixo y
    a = 0
    b = len(dataTension)
    g1.set_xlim(a, b)
    g2.set_xlim(a, b)
    g3.set_xlim(a, b)

root.update()
start = tkinter.Button(root, text = "Start/Stop", font = ('calbiri',15),command = lambda: onOf())
start.place(relx = 0.44, rely = 0.7, relwidth=0.1, relheight=0.05)

root.update()
start = tkinter.Button(root, text = "Reiniciar", font = ('calbiri',15),command = lambda: restart())
start.place(relx = 0.44, rely = 0.8, relwidth=0.1, relheight=0.05)


root.after(1,plot_data)
root.mainloop()