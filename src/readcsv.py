import pandas as pd
import os

country = input("Enter country name or *: ") 
topic = input("Enter topic name or *: ")

def readAndPrintRow(path):
    df = pd.read_csv(path, low_memory=False)
    row_count, column_count = df.shape
    print("File name: ",path)
    print("Number of rows ", row_count)
    print("")
    #print("Number of columns ", column_count)


def getAllDir(root):
    list=[]
    try:
        for name in os.listdir(root):
            list.append(root+"/"+name)
    except:
        pass
    for item in list:
        list.extend(getAllDir(item))
    return list

allPath = getAllDir(".")
allPath = list(set(allPath))

for path in allPath:
    if path.endswith(".csv"):
        if country != "*" and topic != "*":
            if country in path and topic in path:
                readAndPrintRow(path)
        elif country != "*" and topic == "*":
            if country in path:
                readAndPrintRow(path)
        elif country == "*" and topic != "*":
            if topic in path:
                readAndPrintRow(path)
        else:
            readAndPrintRow(path)