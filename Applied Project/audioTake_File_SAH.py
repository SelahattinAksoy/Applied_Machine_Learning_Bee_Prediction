import matplotlib.pyplot as plt
import numpy as np
import wave
from pydub import AudioSegment

soundFile = input("Please enter sound file name: ")
spf = wave.open("Data\\" + soundFile + ".wav", "r") #wave objesi

labFile = open("Data\\" + soundFile + ".lab", "r")
line = labFile.readline()
line = labFile.readline()
timeList = []
while line:
    line = line.split('	')
    if line[0] == '.\n':
        break
    eleman = float(line.pop(0))
    line.insert(0, eleman)
    eleman2 = float(line.pop(1))
    line.insert(1, eleman2)
    #line.pop(-1)#to get rid of bee nobee
    timeList.append(line)
    line = labFile.readline()
print(timeList)
newAudio = AudioSegment.from_wav("Data\\" + soundFile + ".wav")
partOfNewAudio = newAudio[timeList[0][0]*1000:timeList[0][1]*1000]
partOfNewAudio.export("SoundParts\\part1.wav", format="wav")
spf = wave.open("SoundParts\\part1.wav", "r")
# Extract Raw Audio from Wav File
signal = spf.readframes(-1)     #wave objesindeki frami oku
signal = np.frombuffer(signal, dtype="Int16")

frameRate = spf.getframerate()

Time = np.linspace(0, len(signal) / frameRate, num=len(signal))

print(spf.getnframes())  #frame aldık  par part
print(spf.getframerate())  #frekans aldık
print(spf.getsampwidth())
print(spf.getnchannels())
print(len(signal))
print(signal)

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(Time, signal)  #,color="yellow",linestyle="dashed"
plt.savefig("pic.png")
plt.show()

