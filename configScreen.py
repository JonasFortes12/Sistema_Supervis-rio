from tkinter import *
from tkinter import ttk
root = Tk()

class Aplication():
    def __init__(self):
        self.root = root

        self.screen()
        self.widgets_frame1()
        
        root.mainloop()
    
    def screen(self):
        self.root.title("Dados")
        self.root.configure(background='#371E30')
        self.root.resizable(True, True) #Responsividade
        self.root.geometry("700x500")

    def widgets_frame1(self):
        #Botão Confirmar
        self.bt1 = Button(self.root, text="Cancelar", font = ('calbiri',15))
        self.bt1.place(relx=0.15, rely=0.85, relwidth=0.15, relheight=0.08)

        #Botão Cancelar
        self.bt2 = Button(self.root, text="Confirmar", font = ('calbiri',15))
        self.bt2.place(relx=0.75, rely=0.85, relwidth=0.15, relheight=0.08)

        #criando labels e entradas
        valores = ["valor01", "valor02", "valor03", "valor04", "valor05"]
        
        self.lbPorta= Label(self.root, text="Porta", font=('calbiri',15))
        self.lbPorta.place(relx= 0.65, rely= 0.30, relwidth= 0.13)

        self.entryPorta = Entry(self.root, font=('calbiri',15))
        self.entryPorta.place(relx= 0.65, rely= 0.35, relwidth= 0.13)

        self.lbValores = Label(root, text= "Valores", font=('calbiri',15))
        self.lbValores.place(relx= 0.22, rely= 0.30, relwidth= 0.13)
        
        self.cbValores = ttk.Combobox(root, values=valores, font=('calbiri',15))
        self.cbValores.place(relx= 0.22, rely= 0.35, relwidth= 0.13)
        self.cbValores.set("valor01")
    


Aplication() 
