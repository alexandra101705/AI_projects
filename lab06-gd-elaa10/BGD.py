class MyBGDRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x, y, learningRate=0.01, noEpochs=1000):
        n = len(x)
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]

        for epoch in range(noEpochs):
            gradients = [0.0 for _ in range(len(self.coef_))]

            for i in range(n):
                xi = x[i]
                yi = y[i]
                y_pred = self.eval(xi)
                error = y_pred - yi

                for j in range(len(xi)):
                    gradients[j] += error * xi[j]
                gradients[-1] += error

            for j in range(len(self.coef_)):
                self.coef_[j] -= learningRate * gradients[j] / n

        self.intercept_ = self.coef_[-1]
        self.coef_ = self.coef_[:-1]

    def eval(self, xi):
        yi = self.coef_[-1]
        for j in range(len(xi)):
            yi += self.coef_[j] * xi[j]
        return yi

    def predict(self, x):
        return [self.eval(xi) for xi in x]

