#What is the expected outcome of the following code?

import random

random.seed(0)
x = random.choice([1, 2])
random.seed(0)
y = random.choice([1, 2])
print(x - y)
