import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, epoch=1000):
        self.learning_rate = learning_rate
        self.epoch = epoch
        self.weights = None
        self.bias = None
        self.loss_history = []
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def initialize_parameters(self, n_features):
        self.weights = np.zeros(n_features)
        self.bias = 0
        
    def fit(self, X, y):
        self.initialize_parameters(X.shape[1])
        
        for _ in range(self.epoch):
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(linear_model)
            
            dw = (1 / X.shape[0]) * np.dot(X.T, (y_pred - y))
            db = (1 / X.shape[0]) * np.sum(y_pred - y)
            
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            mse = np.mean((y_pred - y)**2)
            self.loss_history.append(mse)

            
    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_pred = self.sigmoid(linear_model)
        y_pred_cls = [1 if pred > 0.5 else 0 for pred in y_pred]
        return y_pred_cls
