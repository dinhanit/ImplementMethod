import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.001, epoch = 50):
        self.learning_rate = learning_rate
        self.weights = None
        self.bias = None
        self.loss_history = []
        self.epoch = epoch
        
    def fit(self, X, y):
        
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for i in range(self.epoch):
            y_predicted = np.dot(X,self.weights) + self.bias
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            mse = np.mean((y_predicted - y)**2)
            self.loss_history.append(mse)

    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted
    
    def Val(self,x,y):
        return np.mean((self.predict(x)-y)**2)