# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# point = Point(10, 20)
# print(point.x)

# exercise
# define a new time person
# should have name and talk() attribute.


class Person:
    def __init__(self, name):
        self.name = name  # self represents the current object. we are setting the name attribute of the current object with the name passed in the argument.

    def talk(self):
        print(f"Hi. I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()