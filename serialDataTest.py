import serial as sr
# import matplotlib.pyplot as plt
# import numpy as np


serialPort = sr.Serial('COM5',9600) #Instância da porta que será lida

while(True):

    data = serialPort.readline()
    data.decode()
    print(int(data))

