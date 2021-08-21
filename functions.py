import csv

def loadingDataCurrent():
    data = []

    with open('corrente.csv', encoding='utf-8') as values:
        
        read = csv.reader(values, delimiter=';')
        for row in read:
            for v in row:
                data.append(float(v))
    
    return data

def loadingDataTension():
    data = []

    with open('tensao.csv', encoding='utf-8') as values:
        
        read = csv.reader(values, delimiter=';')
        for row in read:
            for v in row:
                data.append(float(v))
    
    return data

def loadingDataInput():
    data = []

    with open('entrada.csv', encoding='utf-8') as values:
        
        read = csv.reader(values, delimiter=';')
        for row in read:
            for v in row:
                data.append(float(v))
    
    return data

