from tkinter import *
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
figure1 = plt.figure(figsize=(8, 4), dpi=70) #Define as dimensões da figura
g1 = figure1.add_subplot(111) #Coloca a figura dentro da variavel grafico

canva = FigureCanvasTkAgg(figure1, root) #Instancia a figura dentro da janela  
canva.get_tk_widget().place(relx=0.025, rely=0.05,
                                relwidth=0.30, relheight=0.30)# Tamnaho e posição na tela
        
data = loadingDataTension()
time = range(1, len(data)+1)

g1.set(xlabel='Tempo (s)', ylabel='Posição (m)',
    title='Dados')

x = []
y = []

plt.ion()
while(True):
    for i, j in zip(time, data):
        x.append(i)
        y.append(j)
        g1.plot(x, y)
        plt.pause(0.05)
    x.clear()
    y.clear()
plt.ioff()

root.mainloop()