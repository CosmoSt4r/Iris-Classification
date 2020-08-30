import torch
import pandas as pd
from sklearn.model_selection import train_test_split


# Initializing neural network's class( 4 - x - x - 3 )
class IrisNet(torch.nn.Module):

    def __init__(self, n_hidden_neurons):
        super(IrisNet, self).__init__()
        self.fc1 = torch.nn.Linear(4, n_hidden_neurons)
        self.act1 = torch.nn.Sigmoid()
        self.fc2 = torch.nn.Linear(n_hidden_neurons, n_hidden_neurons)
        self.act2 = torch.nn.Sigmoid()
        self.fc3 = torch.nn.Linear(n_hidden_neurons, 3)
        self.sm = torch.nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.act1(x)
        x = self.fc2(x)
        x = self.act2(x)
        x = self.fc3(x)
        return self.sm(x)


# Initializing neural network with 16 hidden neurons
iris_net = IrisNet(16)
print('Neural network initialized.')

data = pd.read_csv('classifier/Iris.csv')
print('Dataset initialized.')
data = data.drop('Id', axis=1)
data['Species'] = data['Species'].replace({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})

X = data.drop('Species', axis=1)
y = data.Species

X = torch.FloatTensor(X.values)
y = torch.LongTensor(y.values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)

loss = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(iris_net.parameters(), lr=0.001)

top_result = 0

print('Neural network: training...')
for epoch in range(2000):
    optimizer.zero_grad()
    predictions = iris_net.forward(X_train)

    loss_val = loss(predictions, y_train)
    loss_val.backward()

    optimizer.step()

    if epoch % 100 == 0:
        test_predictions = iris_net.forward(X_test)
        test_predictions = test_predictions.argmax(dim=1)
        result = (test_predictions == y_test).float().mean()
        if result > top_result:
            top_result = result
print('Neural network: ready')
print(f'Accuracy: {round(float(top_result) * 100, 2)}%')


def predict_iris_type(s_len, s_wid, p_len, p_wid):

    # In prediction we have only 0, 1 and 2 so we have to decode it to Iris types
    iris_types = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

    # We gain 'str' type information from sliders so we have to make it 'float' type
    iris = [float(s_len), float(s_wid), float(p_len), float(p_wid)]
    iris = torch.FloatTensor([iris])

    # predicting type
    predicted_type = iris_net.forward(iris).argmax()

    # decoding predicted type
    predicted_type = iris_types[predicted_type]

    return predicted_type
