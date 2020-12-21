import pandas as pd
import os

def readAndPrintRow(path):
    df = pd.read_csv(path)
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
       readAndPrintRow(path)