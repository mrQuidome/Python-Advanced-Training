class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"{self.name} says hello!")

class Student(Person):
    def __init__(self, name, age, topic):
        super().__init__(name, age)
        self.topic = topic

    def learn(self):
        print(f'{self.name} is learning {self.topic}')

    def say_hello(self):
        super().say_hello()
        print("Student - say hello")

s1 = Student('John', 42, 'Java')
s1.learn()
s1.say_hello()
