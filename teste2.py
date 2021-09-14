from tkinter import *
from numpy.lib.function_base import select
from functions import *
import matplotlib.pyplot as plt
#Para criar a figura onde será plotado o gráfico:
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
root = Tk()

root.title("Dados")
root.configure(background='lightblue')
root.resizable(True, True) #Responsividade
root.geometry("900x700")

#criando uma figura:
figure1 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
g1 = figure1.add_subplot(111) #Coloca a figura dentro da variavel grafico
g1.set_title('Serial Data')
g1.set_xlabel('Sample')
g1.set_ylabel('Voltage')
g1.set_xlim(0,600)
g1.set_ylim(-1,4)
lines = g1.plot([],[])[0]

canva = FigureCanvasTkAgg(figure1, master = root) #Instancia a figura dentro da janela  
canva.get_tk_widget().place(relx=0.3, rely=0.3,
                                relwidth=0.5, relheight=0.5)# Tamnaho e posição na tela
canva.draw()

data = loadingDataTension()
time = range(1, len(data)+1)
i = 0
j = 0
cond = True
x = []
y = []


def update_data():
    global i, j, cond
    if(i<len(data)):
        x.append(time[i])
        y.append(data[j])
        i = i+1
        j = j+1
    else: 
        cond = False

def plot_data():
    global x, y, lines
    update_data()
    if(cond):
        lines.set_xdata(x)
        lines.set_ydata(y)
        canva.draw()
        root.after(1,plot_data)

root.after(1,plot_data)
root.mainloop()