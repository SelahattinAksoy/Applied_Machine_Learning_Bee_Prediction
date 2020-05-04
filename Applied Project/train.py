import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report


def create_train_data(theFrame):

    msk = np.random.rand(len(theFrame)) < 0.8
    train = theFrame[msk]
    test = theFrame[~msk]
    return train, test


def classification_report_(test, predicted, name):
    print("**********Predicted Raport", name, "***********")
    print(classification_report(test["class"], predicted))


def prediction_by_NaiveBayes(trainNB,testNB):

    gnb = GaussianNB()
    y_pred_gnb = gnb.fit(trainNB[frame.columns[0:6]], trainNB["class"])
    predicted = y_pred_gnb.predict(testNB[frame.columns[0:6]])
    naivesAccuracy = metrics.accuracy_score(testNB["class"], predicted)
    classification_report_(testNB, predicted, "NaiveBayes")
    return naivesAccuracy


def predition_by_RandomForest(trainRF,testRF):
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    clean_class_0_1 = np.where(trainRF["class"] == "bee", 1, 0)
    regressor.fit(trainRF[frame.columns[0:6]], clean_class_0_1)
    predicted_y = regressor.predict(testRF[frame.columns[0:6]])
    predicted_y = np.where(predicted_y > 0.5, "bee", "nobee")
    randomfAccuracy = metrics.accuracy_score(testRF[frame.columns[6:7]], predicted_y)
    classification_report_(testRF, predicted_y, "RandomForest")

    return randomfAccuracy


def accurcy_table(nb, rf):
   frame = pd.DataFrame({
        "Algorithm": ["Naive", "Random"],
        "Accuracy": [nb, rf]
    })
   return frame


frame = pd.read_csv("Cleaned Data\\cleaned_csv_file.csv")
train, test = create_train_data(frame)

frames = ""

naives = prediction_by_NaiveBayes(train, test)
randomf = predition_by_RandomForest(train, test)
table = accurcy_table(naives, randomf)
print(table)