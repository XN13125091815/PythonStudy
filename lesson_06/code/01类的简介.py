class Person:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def say_hello(self):
        print('Hello', self._name)

    def introduce(self):
        print(f"I am a {self._age} years old engineer!")


if __name__ == "__main__":
    p = Person('XiNing', 26, 176)
    p.say_hello()
    p.introduce()
