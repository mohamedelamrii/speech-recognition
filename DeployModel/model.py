


import warnings

import librosa as librosa
import numpy as np

warnings.filterwarnings("ignore")
train_audio_path = './train/audio/'

classes = ['bed', 'bird', 'cat', 'dog', 'down', 'five', 'four', 'go', 'happy', 'house', 'left', 'no', 'off', 'on', 'right', 'stop', 'yes', 'zero']

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

from keras.models import load_model

model = load_model('best_model1.hdf5')


def predict(audio):
    prob = model.predict(audio.reshape(1, 8000, 1))
    index = np.argmax(prob[0])
    return classes[index]





# samples, sample_rate = librosa.load('C:/Users/hicha/Desktop/modelDL/test/audio/clip_00d109e04.wav', sr=16000)
# samples = librosa.resample(samples, sample_rate, 8000)
# #ipd.Audio(samples, rate=8000)
# print("Text:",predict(samples))
import sounddevice as sd
import soundfile as sf

samplerate = 16000
duration = 1 # seconds
filename = '../yes.wav'
print("start")
mydata = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, blocking=True)
print("end")
sd.wait()
sf.write(filename, mydata, samplerate)


samples, sample_rate = librosa.load(filename, sr=16000)
samples = librosa.resample(samples, sample_rate, 8000)

print("Text:", predict(samples))