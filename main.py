class One:
    def __init__(self, name):
        self.name = name


class Two:
    def __init__(self, age):
        self.age = age


class Three:
    def aged(self):
        return f'мне {self.age}'


class Four:
    def names(self):
        return f'меня зовут {self.name}'


class Five(One, Two, Three, Four):
    def __init__(self, name, __age):
        One.__init__(self, name)
        Two.__init__(self, __age)

    @property
    def agee(self):
        return f'{self.age}'

    @agee.setter
    def ageee(self, b):
        self.age = b


c = Five('Ermek', 22)
print(c.names())
print(c.aged())
