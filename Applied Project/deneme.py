from pydub import AudioSegment
t1 = 36.34 * 1000 #Works in milliseconds
t2 = 37.65 * 1000
newAudio = AudioSegment.from_wav("Data\CF003 - Active - Day - (214).wav")
newAudio = newAudio[t1:t2]
newAudio.export('SoundParts\\ali.wav', format="wav") #Exports to a wav file in the current path.