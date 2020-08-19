import numpy as np

inputs = [1,2,3,4]

weights = [0.4,0.3,0.6,0.2]
bias = 2

output = np.dot(weights,inputs) + bias
print(output)
