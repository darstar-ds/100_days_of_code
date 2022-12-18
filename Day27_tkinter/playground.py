def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(2,2,2,2,2,2,2,2,2,2,4)

def calculate(n, **kwargs):
    print(kwargs)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Skodzina", model="Enyaq")
print(my_car.model)