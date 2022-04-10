import serial as sr

serialPort = sr.Serial('COM5',9600)
serialPort.reset_input_buffer()

while(True):
    data = str(serialPort.readline().decode()).split(",")
    
    # print(f"Nivel:{data[0]}  Tempo{data[1]} ")
    print(data)
    




