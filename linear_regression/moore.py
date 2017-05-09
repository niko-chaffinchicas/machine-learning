import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

non_decimal = re.compile(r'[^\d]+')

for line in open('moore.csv'):
    r = line.split('\t')
    # If there is a square bracket, just take everything to left of it
    x = int(non_decimal.sub('', r[2].split('[')[0]))
    y = int(non_decimal.sub('', r[1].split('[')[0]))
    X.append(x)
    Y.append(y)

# Convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# Take the base 10 log of Y
Y = np.log(Y)
plt.scatter(X, Y)
plt.show()

# Apply linear regression solution model
denominator = X.dot(X) - (X.mean() * X.sum())
a = (X.dot(Y) - (Y.mean() * X.sum())) / denominator
b = ((Y.mean() * X.dot(X)) - (X.mean() * X.dot(Y))) / denominator
print("f(x) = {}x + {}".format(a, b))

# Calculate predicted Y
Y_hat = a * X + b
plt.scatter(X, Y)
plt.plot(X, Y_hat, lw=1)
plt.show()

# Calculate R Sqaured
d1 = Y - Y_hat  # Sum of Squared Residual
d2 = Y - Y.mean()  # Sum of Squared Residual
r2 = 1 - (d1.dot(d1) / d2.dot(d2))
print("R squared is {}".format(r2))

# Reasoning out how long it will take the transitor count to double
# log(tc) = a * year + b
# tc = exp(b) * exp(a * year)
# 2 * tc = 2 * exp(b) * exp(a * year)
#        = exp(ln(2)) * exp(b) * exp(a * year)
print("time to double:", np.log(2) / a, "years")
