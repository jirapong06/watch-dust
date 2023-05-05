import json
from statistics import mean

load_lut = []
lut = []

def sampleData():
    for i in range(16):
        data = open("esp32_calibrate_v2_"+str(i+1)+".txt", "r")
        buf = json.loads(data.read())

        load_lut.append(buf)
        print("Load File :",i+1)

    valueBuff = []
    for i in range(4096):
        valueBuff.clear()
        for j in range(16):
            valueBuff.append(load_lut[j][i])
        meanBuff = mean(valueBuff)
        lut.append(meanBuff)
        #print(meanBuff)

def writeFile():
    f = open("esp32_calibrate_v2_finish.txt", "w")
    f.write(str(lut))
    f.close()
    
sampleData()
writeFile()
