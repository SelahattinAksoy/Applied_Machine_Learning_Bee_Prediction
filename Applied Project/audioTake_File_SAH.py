import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open("C:\\Users\\selah\\Desktop\\Applied Machine Learning\\Data\\CF003 - Active - Day - (215).wav", "r") #wave objesi

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)     #wave objesinşdeki frami oku
signal = np.fromstring(signal, "Int16")

fs = spf.getframerate()

Time = np.linspace(0, len(signal) / fs, num=len(signal))

print(spf.getnframes())  #frame aldık  par part
print(spf.getframerate())  #frekans aldık
print(spf.getsampwidth())
print(spf.getnchannels())
plt.figure(1)
plt.title("Signal Wave...")
plt.plot(Time,signal)
plt.show()

