import librosa
import librosa.display
from librosa import  feature
import numpy as np
import pandas as pd
from pathlib import Path  #Path lib for looking file in a path

def FindFileNamesByPath(path,typeofFile):

    File_List = [path.name for path in Path(path).rglob('*.'+typeofFile)]
    return [(result, (result.split("--")[1])) for result in File_List]


def Librosa(path):
    y, sr = librosa.load("Cleaned Data\Cleaned_Voice\\"+path, sr=None)
    return y, sr


def CreateLibrosa(allDataName):
    librosa_value = [(Librosa(path[0]), path[1]) for path in allDataName]
    return librosa_value


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


def get_Feature_extract(allData):
    out = [(get_feature_vector(librosaValue[0][0], librosaValue[0][1]), librosaValue[1])
           for librosaValue in CreateLibrosa(allData)]
    return out


result = FindFileNamesByPath("Cleaned Data\Cleaned_Voice","wav")
print(result)
print(len(result))
geto = get_Feature_extract(result)

classBeeNoBee = []
vectors = []
for i in geto:
    vectors.append(i[0])
    classBeeNoBee.append(i[1])

frame = pd.DataFrame(librosa.util.normalize(vectors), columns=["chroma_stft", "spectral_centroid",
                                                                "spectral_bandwidth", "spectral_rolloff", "rmse",
                                                                "zero_crossing_rate"])
print(frame)
frame["class"] = classBeeNoBee

frame.to_csv("Cleaned Data\\cleaned_csv_file.csv", index=False, header=True)

