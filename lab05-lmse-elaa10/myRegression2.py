import numpy as np

class MyLinearMultivariateRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x, y):
        X = np.array([[1] + row for row in x])
        Y = np.array(y).reshape(-1, 1)

        # w = (X^T * X)^-1 * X^T * Y
        Xt = X.T
        XtX = Xt.dot(X)
        XtY = Xt.dot(Y)
        w = np.linalg.inv(XtX).dot(XtY)

        self.intercept_ = w[0][0]
        self.coef_ = [w[1][0], w[2][0]]

    def predict(self, x):
        return [self.intercept_ + self.coef_[0] * row[0] + self.coef_[1] * row[1] for row in x]
