import matplotlib.pyplot as plt
import numpy as np
import wave
from pydub import AudioSegment


list_of_sound_file_name=[]
for i in range(214,227,1):
    sound=str(i)
    sound="("+sound+")"
    soundFile="CF003 - Active - Day - "+sound
    list_of_sound_file_name.append(soundFile)
print(list_of_sound_file_name)


for j in list_of_sound_file_name:

        spf = wave.open("Data\\" + j + ".wav", "r") #wave objesi

        labFile = open("Data\\" + j + ".lab", "r")


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

        counter=0;
        for i in timeList:
            newAudio = AudioSegment.from_wav("Data\\" + j + ".wav")
            partOfNewAudio = newAudio[i[0] * 1000:i[1] * 1000]
            partOfNewAudio.export("Cleaned Data\\Cleaned_Voice\\"+j+"--"+(i[2])[:-2]+"--"+str(counter)+".wav", format="wav")


            spf = wave.open("Cleaned Data\\Cleaned_Voice\\"+j+"--"+(i[2])[:-2]+"--"+str(counter)+".wav", "r")
            # Extract Raw Audio from Wav File
            signal = spf.readframes(-1)     #wave objesindeki frami oku
            signal = np.frombuffer(signal, dtype="Int16")
            frameRate = spf.getframerate()
            Time = np.linspace(0, len(signal) / frameRate, num=len(signal))
            plt.figure(1)
            plt.title(j+"--"+(i[2])[:-2]+"--"+str(counter))
            plt.plot(Time, signal)  # ,color="yellow",linestyle="dashed"
            plt.savefig("Cleaned Data\\Freq_of_Cleaned_Voice\\"+j+"--"+(i[2])[:-2]+"--"+str(counter)+".png")
            counter += 1


print(spf.getnframes())  #frame aldık  par part
print(spf.getframerate())  #frekans aldık
print(spf.getsampwidth())
print(spf.getnchannels())
print(len(signal))
print(signal)


#plt.show()

