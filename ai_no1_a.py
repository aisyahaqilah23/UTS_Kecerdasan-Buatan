# Aisyah Aqilah Rian Vania
# 21091397002
# 2021-B

import numpy as np

inputs = [1.0, 1.9, 2.0, 2.8, 3.0, 3.3, 4.0, 4.6, 5.0, 5.7]
weights = [0.1, 0.3, 0.7, 0.9, 1.0, 1.1, 1.3, 1.7, 1.9, 2.0]

bias = 4.0

outputs = np.dot(weights, inputs) + bias
print(outputs)