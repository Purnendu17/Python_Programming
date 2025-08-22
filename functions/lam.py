from functools import partial
double=partial(lambda x: x*2)
print(double(5))