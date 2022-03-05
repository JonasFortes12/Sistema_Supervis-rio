import serial as sr
import matplotlib.pyplot as plt
# import numpy as np

plt.ion()

fig = plt.figure()

i = 0
x = list()
y = list()


serialPort = sr.Serial('COM5',9600) #Instância da porta que será lida 
serialPort.close()
serialPort.open()


while(True):
    data = serialPort.readline()
    print(data.decode())

    x.append(i)
    y.append(data.decode())

    plt.scatter(i, float(data.decode()))
    i += 1
    plt.show()
    plt.pause(0.0001) 