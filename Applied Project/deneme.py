import librosa
audio_data = "C:\\Users\\selah\\Desktop\\Applied Machine Learning\\Data\\CF003 - Active - Day - (214).wav"
x , sr = librosa.load(audio_data)
print(type(x), type(sr))#<class 'numpy.ndarray'> <class 'int'>print(x.shape, sr)#(94316,) 22050