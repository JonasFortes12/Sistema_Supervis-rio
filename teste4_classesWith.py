from tkinter import *
import tkinter
from tkinter import ttk
# from numpy.lib.function_base import select
from functions import *
import matplotlib.pyplot as plt
#Para criar a figura onde será plotado o gráfico:
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root2 = Tk()

dataTension = loadingDataTension()
dataCurrent = loadingDataCurrent()
dataInput = loadingDataInput()
#variáveis do intervalo dos graficos
a = 0
b = len(dataTension)
i = 1 #eixo x
j = 0 #eixo y
on = False # mudar para graficOn
xTension = []
xCurrent = []
xInput = []
yTension = []
yCurrent = []
yInput = []

class Grafics():
    
    def grafic1(self):
        #criando uma figura 1:
        figure1 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
        g1 = figure1.add_subplot(111) #Coloca a figura dentro da variavel grafico
        g1.set_title('Serial Data')
        g1.set_xlabel('Sample')
        g1.set_ylabel('Tension')
        g1.set_xlim(a, b)
        g1.set_ylim(-1,4)
        lines1 = g1.plot([],[])[0] #(Explicar)
        canva1 = FigureCanvasTkAgg(figure1, master = root2) #Instancia a figura dentro da janela  
        canva1.get_tk_widget().place(relx=0.025, rely=0.2,
                                        relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
        canva1.draw()

    def grafic2(self):
        #criando a figura 2:
        figure2 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
        g2 = figure2.add_subplot(111) #Coloca a figura dentro da variavel grafico
        g2.set_title('Serial Data')
        g2.set_xlabel('Sample')
        g2.set_ylabel('Current')
        g2.set_xlim(a, b)
        g2.set_ylim(-0.01,0.015)
        lines2 = g2.plot([],[])[0]

        canva2 = FigureCanvasTkAgg(figure2, master = root2) #Instancia a figura dentro da janela  
        canva2.get_tk_widget().place(relx=0.350, rely=0.2,
                                        relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
        canva2.draw()

    def grafic3(self):
        #criando a figura 3:
        figure3 = plt.figure(figsize=(10, 6), dpi=70) #Define as dimensões da figura
        g3 = figure3.add_subplot(111) #Coloca a figura dentro da variavel grafico
        g3.set_title('Serial Data')
        g3.set_xlabel('Sample')
        g3.set_ylabel('Input')
        g3.set_xlim(a, b)
        g3.set_ylim(-1,3)
        lines3 = g3.plot([],[])[0]

        canva3 = FigureCanvasTkAgg(figure3, master = root2) #Instancia a figura dentro da janela  
        canva3.get_tk_widget().place(relx=0.675, rely=0.2,
                                        relwidth=0.30, relheight=0.40)# Tamnaho e posição na tela
        canva3.draw()

class Funcs(Grafics):  #Inerte
    
    def update_data(self):
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

    def plot_data(self):
        if(on == True):
            self.update_data()
            
            lines1.set_xdata(xTension)
            lines1.set_ydata(yTension)
                
            lines2.set_xdata(xCurrent)
            lines2.set_ydata(yCurrent)
                
            lines3.set_xdata(xInput)
            lines3.set_ydata(yInput)
                
            canva1.draw()
            canva2.draw()
            canva3.draw()
                
            root.after(1,Funcs.plot_data)
        else:
            root.after(1,Funcs.plot_data)

    def onOf():
        global on
        on = not on

    def reset():
        global xTension, xCurrent, xInput, yCurrent, yTension, yInput, i, j, a, b
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

class Aplication(Funcs, Grafics):  
    def __init__(self):
        self.root1 = root
        self.root2 = root2
        self.screen1()
        self.widgetsScreen1()
        root.mainloop()

    def screen1(self):
        self.root1.title("Configurações")
        self.root1.configure(background='#371E30')
        self.root1.geometry("900x500")
        self.root1.resizable(False, False)
        self.root1.focus_force()#força o foco na janela 2
        self.root1.grab_set()#impede que haja alterações na root2 enquanto root1
    
    def screen2(self):
        self.root2.title("Dados")
        self.root2.configure(background='#371E30')
        self.root2.resizable(True, True) #Responsividade
        self.root2.geometry("1200x700")
        
    def widgetsScreen2(self):
        startButton = tkinter.Button(self.root2, text = "Start/Stop", font = ('calbiri',15))
        startButton.place(relx = 0.44, rely = 0.7, relwidth=0.1, relheight=0.05)

        resetButton = tkinter.Button(self.root2, text = "Reset", font = ('calbiri',15))
        resetButton.place(relx = 0.44, rely = 0.8, relwidth=0.1, relheight=0.05)

        self.lbValor = Label(self.root2, text= 'valor', font=('calbiri',15))
        self.lbValor.place(relx= 0.44, rely= 0.30, relwidth= 0.13)
        
        self.lbPorta = Label(self.root2, text= 'porta', font=('calbiri',15))
        self.lbPorta.place(relx= 0.44, rely= 0.30, relwidth= 0.13)

        self.grafic1()
        self.grafic2()
        self.grafic3()

    def widgetsScreen1(self):
        
        def cancelButtonAction(): 
            self.root1.destroy()
        def confirmButtonAction(): 
            self.root1.destroy()
            self.screen2()
            self.widgetsScreen2()
            
            self.porta = self.entryPorta.get()
            print(self.porta)
            
            self.valor = self.cbValores.get()
            print(self.valor)

        #Botão Cancelar
        self.cancelButton = Button(self.root1, text="Cancelar", font = ('calbiri',15),
        command=cancelButtonAction)
        self.cancelButton.place(relx=0.15, rely=0.85, relwidth=0.15, relheight=0.08)

        #Botão Confirmar
        self.confirmButton = Button(self.root1, text="Confirmar", font = ('calbiri',15), 
        command=confirmButtonAction)
        self.confirmButton.place(relx=0.73, rely=0.85, relwidth=0.15, relheight=0.08)

        #criando labels e entradas
        bitSecValues = ["9600", "700", "580"]
        bitDataValues = ["10", "9", "8", "7", "6", "5", "4"]
        paridadeValues = ["Nenhum", "12", "Padrão"]
        bitsParadaValues = ["1", "2", "4"]
        contFluxValues = ["Nenhum", "Padrão", "Automático"]
        
       


        self.lbBitSec = Label(self.root1, text= "Bits por segundo", font=('calbiri',15))
        self.lbBitSec.place(relx= 0.20, rely= 0.30, relwidth= 0.18)
        self.cbBitSec = ttk.Combobox(self.root1, values=bitSecValues, font=('calbiri',15))
        self.cbBitSec.place(relx= 0.20, rely= 0.35, relwidth= 0.18)
        self.cbBitSec.set("9600")

        self.lbBitData = Label(self.root1, text= "Bits de dados", font=('calbiri',15))
        self.lbBitData.place(relx= 0.20, rely= 0.42, relwidth= 0.18)
        self.cbBitData = ttk.Combobox(self.root1, values=bitDataValues, font=('calbiri',15))
        self.cbBitData.place(relx= 0.20, rely= 0.47, relwidth= 0.18)
        self.cbBitData.set("8")

        self.lbBitsParada = Label(self.root1, text= "Bits de Parada", font=('calbiri',15))
        self.lbBitsParada.place(relx= 0.20, rely= 0.54, relwidth= 0.18)
        self.cbBitsParada = ttk.Combobox(self.root1, values=bitsParadaValues, font=('calbiri',15))
        self.cbBitsParada.place(relx= 0.20, rely= 0.59, relwidth= 0.18)
        self.cbBitsParada.set("1")
        
        self.lbPorta= Label(self.root1, text="Porta", font=('calbiri',15))
        self.lbPorta.place(relx= 0.65, rely= 0.30, relwidth= 0.18)
        self.entryPorta = Entry(self.root1, font=('calbiri',15))
        self.entryPorta.place(relx= 0.65, rely= 0.35, relwidth= 0.18)
        
        
        self.lbParidade = Label(self.root1, text= "Paridade", font=('calbiri',15))
        self.lbParidade.place(relx= 0.65, rely= 0.42, relwidth= 0.18)
        self.cbParidade = ttk.Combobox(self.root1, values=paridadeValues, font=('calbiri',15))
        self.cbParidade.place(relx= 0.65, rely= 0.47, relwidth= 0.18)
        self.cbParidade.set("Nenhum")


        self.lbContFlux = Label(self.root1, text= "Controle de fluxo", font=('calbiri',15))
        self.lbContFlux.place(relx= 0.65, rely= 0.54, relwidth= 0.18)
        self.cbContFlux = ttk.Combobox(self.root1, values=contFluxValues, font=('calbiri',15))
        self.cbContFlux.place(relx= 0.65, rely= 0.59, relwidth= 0.18)
        self.cbContFlux.set("Nenhum")

        
Aplication()