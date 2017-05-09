# Linear Regression Notes


### Dot Operations
A "dot" operation takes two ordered arrays of numbers, multiplies each ordered pair, then sums all the ordered pairs.
This is used for operations such as <code>&Sigma;x<sub>i</sub>y<sub>i</sub></code>, where for each index <code>i</code>, the two items in the ordered pair (<code>x<sub>i</sub></code> and <code>y<sub>i</sub></code>) are multiplied and then sum of the results is returned.


### Chain Rule
Chain rule gets applied any time that you are taking the derivative of some function where there is another function being applied inside of it.
This is used, for example, when taking the derivative of the following: <code>(sin x)<sup>2</sup></code>. Because both the exponent <code><sup>2</sup></code> operation and the <code>sin</code> operation are both functions, we have to apply the chain rule.

In the above example, both of the functions have shortcuts, so we can use those. We know that the derivative of <code>x<sup>2</sup></code> is <code>2x</code> and that the derivative of <code>sin x</code> is <code>cos x</code>.
To apply the chain rule, we'll append the derivative of a function any time that function is present in the solution for the derivative of another function. So if when solving for the derivative of <code>(sin x)<sup>2</sup></code> we get to <code>((sin x)<sup>2</sup>)' = 2(sin x)</code>, we have to apply the chain rule because <code>sin x</code> is a function and has its own derivative. This makes the full answer: <code>((sin x)<sup>2</sup>)' = 2(sin x) • cos x</code>.


### Sum of Squared Residual
The sum of squared residual is the error function defined previously: <code>SS<sub>res</sub> = &Sigma;(y<sub>i</sub> - y&#770;<sub>i</sub>)<sup>2</sup>

### Sum of Squared Total
The sum of squared total is the sum of all the  squared differences between actual <code>y</code><small>s</small> and the mean <code>y&#772;</code>, which looks like: <code>SS<sub>total</sub> = &Sigma;(y<sub>i</sub> - y&#772;)<sup>2</sup></code>

### R Squared
R Squared defines how well a line of best fit describes the variation in Y. It is defined as <code>R<sup>2</sup> = 1 - (SS<sub>res</sub> / SS<sub>total</sub>)</code>. The range of results is from 0 to 1, with 1 being a line of perfect fit. If the result for <code>R<sup>2</sup></code> is negative, it means that the model for prediction is worse than just predicting the mean of Y.

### NumPy Arrays
When using NumPy arrays rather than primitive lists, many of the basic operators(<code>+ - \* /</code>) act differently. For example, if the both the items are vectors of the same length, then the operation is applied to each ordered pair in the two vectors, returning one vector with the results. If the variable on the left is a vector but the the variable on the right is simply a float or an integer, then the operation is performed for every item in the vector with the variable on the right being constant.
```python
v1 = numpy.array([1, 2, 3, 4])
v2 = numpy.array([2, 4, 3, 1])

print(v1 + v2)
# out: [3, 6, 6, 5]

print(v2 * 3)
# out: [6, 12, 9, 3]
```
