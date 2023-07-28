# password genartor

import random


number = '124567890'
string = 'amznxbcvkjhdgsfareqtyuiopl'
symbol = '!@#~$%^&*()_+><?"|":|{][}'

result = number + string + symbol
len = 16
password = ''.join(random.sample(result, len))
print('password is ' + password)
