from tkinter import *
import tkinter
# from numpy.lib.function_base import select
from functions import *
import matplotlib.pyplot as plt
#Para criar a figura onde será plotado o gráfico:
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial as sr

root = Tk()
serialPort = sr.Serial('COM5',9600) #Instância da porta que será lida
serialPort.reset_input_buffer()

root.title("Dados")
root.configure(background='#371E30')
root.resizable(True, True) #Responsividade
root.geometry("900x500")


#variáveis do intervalo dos graficos
a = 0
b = 100

#criando uma figura 1:
figure1 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
g1 = figure1.add_subplot(111) #Coloca a figura dentro da variavel grafico
g1.set_title('Serial Data')
g1.set_xlabel('Sample')
g1.set_ylabel('Tension')
g1.set_xlim(a, b)
g1.set_ylim(-1,1100)

lines1 = g1.plot([],[])[0] #(Explicar)

canva1 = FigureCanvasTkAgg(figure1, master = root) #Instancia a figura dentro da janela  
canva1.get_tk_widget().place(relx=0.2, rely=0.1,
                                relwidth=0.60, relheight=0.70)# Tamnaho e posição na tela
canva1.draw()


i = 1 #eixo x

on = False # mudar para graficOn

xData = []
yData = []


def update_data():
    global i, a, b

    data = serialPort.readline()
    print(data)
    data.decode()
    # print(int(data))
    
    xData.append(i)
    yData.append(int(data))

    i = i+1

    if(i>b):
        a = a + 1
        b = b + 1
        g1.set_xlim(a, b)

def plot_data():
    if(on == True):
        update_data()
        
        lines1.set_xdata(xData)
        lines1.set_ydata(yData)
            
        canva1.draw()
            
        root.after(1,plot_data)
    else:
        root.after(1,plot_data)

def onOf():
    global on
    on = not on

def reset():
    global xData, yData, i, a, b
    xData = []
    yData = []
    i = 1 #eixo x
    a = 0
    b = 100
    g1.set_xlim(a, b)


root.update() 
start = tkinter.Button(root, text = "Start/Stop", font = ('calbiri',15),command = lambda: onOf())
start.place(relx = 0.54, rely = 0.85, relwidth=0.15, relheight=0.10)

root.update()
start = tkinter.Button(root, text = "Reset", font = ('calbiri',15),command = lambda: reset())
start.place(relx = 0.34, rely = 0.85, relwidth=0.15, relheight=0.10)

root.after(1,plot_data)
root.mainloop()


