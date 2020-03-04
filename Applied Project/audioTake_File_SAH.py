import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open("C:\\Users\\selah\\Desktop\\Applied Machine Learning\\mert.wav", "r") #wave objesi

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)     #wave objesinşdeki frami oku
signal = np.fromstring(signal, "Int16")

fs = spf.getframerate()

Time = np.linspace(0, len(signal) / fs, num=len(signal))

print(spf.getnframes())  #frame aldık  par part
print(spf.getframerate())  #frekans aldık
print(spf.getsampwidth())
print(spf.getnchannels())
print (len(signal))
print (signal)
a=signal[1:100][1:100]

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(Time,signal)  #,color="yellow",linestyle="dashed"
plt.savefig("C:\\Users\\selah\\Desktop\\Applied Machine Learning\\Applied_Machine_Learning_Bee_Prediction\\aliemre2.png")
plt.show()

