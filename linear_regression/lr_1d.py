import numpy as np
import matplotlib.pyplot as plt

# import data
X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

# convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# Plot initial data
plt.scatter(X, Y)
plt.show()

# Apply equations
denominator = X.dot(X) - (X.mean() * X.sum())
a = (X.dot(Y) - (Y.mean() * X.sum())) / denominator
b = ((Y.mean() * X.dot(X)) - (X.mean() * X.dot(Y))) / denominator
print("f(x) = {}x + {}".format(a, b))

# Calculate predicted Y
Y_hat = a * X + b

# Re-plot
plt.scatter(X, Y)
plt.plot(X, Y_hat, lw=1)
plt.show()

# Calculate R Sqaured
d1 = Y - Y_hat  # Sum of Squared Residual
d2 = Y - Y.mean()  # Sum of Squared Residual
r2 = 1 - (d1.dot(d1) / d2.dot(d2))
print("R squared is {}".format(r2))
