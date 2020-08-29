import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

dataset = pd.read_csv("classifier/Iris.csv")

dataset.drop('Id', axis=1, inplace=True)

train, test = train_test_split(dataset, test_size=0.3)

train_X = train[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
train_y = train.Species

test_X = test[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
test_y = test.Species

prediction_accuracy = 0
print('Prediction model: training', end='\r')
while prediction_accuracy < 0.93:
    model = svm.SVC()
    model.fit(train_X, train_y)
    prediction = model.predict(test_X)
    prediction_accuracy = metrics.accuracy_score(prediction, test_y)
print('Prediction model: ready')


def predict_iris_type(s_len, s_wid, p_len, p_wid):
    iris = [pd.Series([s_len, s_wid, p_len, p_wid])]
    iris = pd.concat(iris, axis=1).transpose()

    predicted_type = model.predict(iris)[0]
    return predicted_type
