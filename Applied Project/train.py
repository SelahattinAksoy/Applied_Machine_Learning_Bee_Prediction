import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report


def create_train_data(frame):

    msk = np.random.rand(len(frame)) < 0.8
    train = frame[msk]
    test = frame[~msk]
    return train,test


def prediction_by_NaiveBayes(train,test):

    gnb = GaussianNB()
    y_pred_gnb = gnb.fit(train[frame.columns[0:6]], train["class"])
    predicted = y_pred_gnb.predict(test[frame.columns[0:6]])
   # print("Tahmin edilen",predicted)
    naives=metrics.accuracy_score(test["class"], predicted)
   # print("Accuracy:", (metrics.accuracy_score(test["class"], predicted))*100)
    classification_report_(test,predicted,"NaiveBayes")
    return naives

def predition_by_RandomForest(train,test):

    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    clean_class_0_1=np.where(train["class"]=="bee", 1, 0)
    regressor.fit(train[frame.columns[0:6]], clean_class_0_1)
    predicted_y=regressor.predict(test[frame.columns[0:6]])
    predicted_y=np.where(predicted_y>0.5, "bee", "nobee")
    randomf=(metrics.accuracy_score(test[frame.columns[6:7]],predicted_y)),
    classification_report_(test,predicted_y,"RandomForest")

    return randomf

def accurcy_table(naives,randomf):
   frame= pd.DataFrame({
        "Algo":["Naive","Random"],
        "Accurcy":[naives,randomf]
    })
   print(frame)

def classification_report_(test,predicted,name):
    print("**********","Predicted Raport",name,"***********")
    print(classification_report(test["class"], predicted))

frame=pd.read_csv("Cleaned Data\\cleaned_csv_file.csv")
train,test=create_train_data(frame)


naives=prediction_by_NaiveBayes(train,test)
randomf=predition_by_RandomForest(train,test)
accurcy_table(naives,randomf)




