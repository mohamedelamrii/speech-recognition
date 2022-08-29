import librosa
from django.http import HttpResponse
from django.shortcuts import render
import sounddevice as sd
import soundfile as sf
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
import numpy as np
import datetime

def home(request):

    def predict(audio):
        classes = ['bed', 'bird', 'cat', 'dog', 'down', 'five', 'four', 'go', 'happy', 'house', 'left', 'no', 'off',
                   'on', 'right', 'stop', 'yes', 'zero']
        model = load_model('C:\\Users\\hicha\\Desktop\\projects\\DeployModel\\DeployModel\\best_model1.hdf5')

        prob = model.predict(audio.reshape(1, 8000, 1))


        index = np.argmax(prob[0])
        return classes[index]
    def Record():


        samplerate = 16000
        duration = 1  # seconds
        filename = 'yes.wav'
        print("start")
        mydata = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, blocking=True)
        print("end")
        sd.wait()
        sf.write(filename, mydata, samplerate)

        samples, sample_rate = librosa.load(filename, sr=16000)
        samples = librosa.resample(samples, sample_rate, 8000)
        print(samples)
        global v
        v=""
        v = predict(samples)
        print("Text:", v)

    Record()
    return render(request, "home.html", context={"v" : v})


def result(request):
    return render(request, "result.html")

