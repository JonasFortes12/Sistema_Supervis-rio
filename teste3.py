from tkinter import *
from numpy.lib.function_base import select
from functions import *
import matplotlib.pyplot as plt
#Para criar a figura onde será plotado o gráfico:
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
root = Tk()

root.title("Dados")
root.configure(background='#371E30')
root.resizable(True, True) #Responsividade
root.geometry("1200x700")

#criando uma figura 1:
figure1 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
g1 = figure1.add_subplot(111) #Coloca a figura dentro da variavel grafico
g1.set_title('Serial Data')
g1.set_xlabel('Sample')
g1.set_ylabel('Tension')
g1.set_xlim(0,500)
g1.set_ylim(-1,4)
lines1 = g1.plot([],[])[0]

canva1 = FigureCanvasTkAgg(figure1, master = root) #Instancia a figura dentro da janela  
canva1.get_tk_widget().place(relx=0.025, rely=0.05,
                                relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
canva1.draw()

#criando a figura 2:
figure2 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
g2 = figure2.add_subplot(111) #Coloca a figura dentro da variavel grafico
g2.set_title('Serial Data')
g2.set_xlabel('Sample')
g2.set_ylabel('Current')
g2.set_xlim(0,500)
g2.set_ylim(-0.01,0.015)
lines2 = g2.plot([],[])[0]

canva2 = FigureCanvasTkAgg(figure2, master = root) #Instancia a figura dentro da janela  
canva2.get_tk_widget().place(relx=0.350, rely=0.05,
                                relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
canva2.draw()

#criando a figura 3:
figure3 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
g3 = figure3.add_subplot(111) #Coloca a figura dentro da variavel grafico
g3.set_title('Serial Data')
g3.set_xlabel('Sample')
g3.set_ylabel('Input')
g3.set_xlim(0,500)
g3.set_ylim(-1,3)
lines3 = g3.plot([],[])[0]

canva3 = FigureCanvasTkAgg(figure3, master = root) #Instancia a figura dentro da janela  
canva3.get_tk_widget().place(relx=0.675, rely=0.05,
                                relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
canva3.draw()


dataTension = loadingDataTension()
dataCurrent = loadingDataCurrent()
dataInput = loadingDataInput()
timeTension = range(1, len(dataTension)+1)
timeCurrent = range(1, len(dataCurrent)+1)
timeInput = range(1, len(dataInput)+1)
i = 0
j = 0
cond = True
xTension = []
xCurrent = []
xInput = []
yTension = []
yCurrent = []
yInput = []


def update_data():
    global i, j, cond
    if(i<len(dataTension)):
        xTension.append(timeTension[i])
        yTension.append(dataTension[j])
        xCurrent.append(timeCurrent[i])
        yCurrent.append(dataCurrent[j])
        xInput.append(timeInput[i])
        yInput.append(dataInput[j])
        i = i+1
        j = j+1
    else: 
        cond = False

def plot_data():
    global xTension, yTension, xCurrent, yCurrent, xInput, yInput
    update_data()
    if(cond):
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

root.after(1,plot_data)
root.mainloop()