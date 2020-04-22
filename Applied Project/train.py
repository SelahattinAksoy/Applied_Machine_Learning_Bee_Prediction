import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor


frame=pd.read_csv("Cleaned Data\\cleaned_csv_file.csv")

def create_train_data():

    msk = np.random.rand(len(frame)) < 0.8
    train = frame[msk]
    test = frame[~msk]
    return train,test


train,test=create_train_data()

frames=""

def prediction_by_NaiveBayes():

    gnb = GaussianNB()
    y_pred_gnb = gnb.fit(train[frame.columns[0:6]], train["class"])
    predicted = y_pred_gnb.predict(test[frame.columns[0:6]])
    print("Tahmin edilen",predicted)
    naives=metrics.accuracy_score(test["class"], predicted)
    print("Accuracy:", (metrics.accuracy_score(test["class"], predicted))*100)
    return naives

def predition_by_RandomForest():

    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    clean_class_0_1=np.where(train["class"]=="bee", 1, 0)
    regressor.fit(train[frame.columns[0:6]], clean_class_0_1)
    predicted_y=regressor.predict(test[frame.columns[0:6]])
    predicted_y=np.where(predicted_y>0.5, "bee", "nobee")
    print("Tahmin edilen Deger  ",predicted_y)
    randomf=(metrics.accuracy_score(test[frame.columns[6:7]],predicted_y))
    print("Accuracy:",(metrics.accuracy_score(test[frame.columns[6:7]],predicted_y))*100)
    return randomf
def accurcy_table():
   frame= pd.DataFrame({
        "Algo":["Naive","Random"],
        "Accurcy":[naives,randomf]
    })
   print(frame)


naives=prediction_by_NaiveBayes()
randomf=predition_by_RandomForest()
accurcy_table()