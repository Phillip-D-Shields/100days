def function_default_args(a=1, b=2, c=3): # default values
    print(a, b, c)

print(function_default_args(c=5))

def function_unlimited_args(*args): # unlimited args
    for n in args:
        print(n)

print(function_unlimited_args(1, 2, 3, 4, 5))

def add(*args):
    total = 0
    print(type(args))
    for n in args:
        total += n
    return total

print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3, 4, 5, 5, 4, 3, 2, 1))


def function_multiple_keyword_args(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

print(function_multiple_keyword_args(a=1, b=2, c=3))

# calculate function with n and kwargs
def calculate(n, **kwargs):
    print(n)
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs['add']
    n -= kwargs['sub']
    n *= kwargs['mul']
    n /= kwargs['div']
    return n

print(calculate(1, add=1000, sub=5, mul=10, div=2))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')
        self.color = kwargs.get('color')

car_test = Car(make='Ford', model='Fiesta', year=2015, color='Blue')
print(car_test.model)

second_car = Car(make='nissan')
print(second_car.model)