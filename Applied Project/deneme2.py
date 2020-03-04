import matplotlib.pyplot as plt

from scipy.io import wavfile
samplerate, data = wavfile.read('C:\\Users\\selah\\Desktop\\Applied Machine Learning\\mert.wav')


print (data.shape)
print (type(data))
print (samplerate)
print (data.size/samplerate) #ses kaydının uzunluğunu buluyor
print (min(data))
samples = data.shape[0]
plt.plot(data)
plt.show()