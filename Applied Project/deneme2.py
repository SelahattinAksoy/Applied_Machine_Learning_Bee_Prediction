import matplotlib.pyplot as plt
import librosa
import librosa.display
from librosa import  feature
import  wave
import numpy as np
import pandas as pd
from pathlib import Path  #Path lib for looking file in a path
from sklearn.naive_bayes import GaussianNB



fn_list_i = [
    feature.chroma_stft,
    feature.spectral_centroid,
    feature.spectral_bandwidth,
    feature.spectral_rolloff
]

fn_list_ii = [
    feature.rms,
    feature.zero_crossing_rate,
]


def get_feature_vector(y, sr):
    feat_vect_i = [np.mean(funct(y, sr)) for funct in fn_list_i]
    feat_vect_ii = [np.mean(funct(y)) for funct in fn_list_ii]
    feature_vector = feat_vect_i + feat_vect_ii

    return feature_vector


y, sr = librosa.load("Cleaned Data\Cleaned_Voice\CF003 - Active - Day - (214).wav--be--0.wav" , sr=None)

#print(get_feature_vector(y,sr))
print(librosa.util.normalize(get_feature_vector(y,sr)))
