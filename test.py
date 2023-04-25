
import numpy as np
import pyedflib
import matplotlib.pyplot as plt

edf = pyedflib.EdfReader('binary.bdf')

labels = edf.getSignalLabels()

print(labels)

print("Duaration:"+str(edf.getFileDuration()))
print("Freq.:"+str(edf.getSampleFrequencies()))
print("N-Sample(=Freq x Duaration):"+str(edf.getNSamples()))
print("Date:"+str(edf.getStartdatetime()))


print("Anotation:"+str(edf.read_annotation()))
print("Technician:"+str(edf.getTechnician()))
print("Header:"+str(edf.getHeader()))


i = 0
signal0 = edf.readSignal(0).astype('str')
signal1 = edf.readSignal(1).astype('str')
signal2 = edf.readSignal(2).astype('str')
signal3 = edf.readSignal(3).astype('str')
signal4 = edf.readSignal(4).astype('str')
signal5 = edf.readSignal(5).astype('str')
signal6 = edf.readSignal(6).astype('str')
signal7 = edf.readSignal(7).astype('str')
signal8 = edf.readSignal(8).astype('str')

f = open('output.csv', 'w')

for i in range(signal0.size):
    f.write(signal0[i]+","+signal1[i]+","+signal2[i]+","+signal3[i]+","+signal4[i]+","+signal5[i]+","+signal6[i]+","+signal7[i]+","+signal8[i]+"\n")

f.close()