"""from abc import abstractmethod

class ITSTEP:
    @abstractmethod
    def show_info(self):
        pass

    def simple_method(self):
        print("...")

class IFITSTE(ITSTEP):

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_info(self):
        return f"Name: {self.name} id: {self.id}"



class KalushITSTEL(ITSTEP):
    def __init__(self, name, id, count):
        self.name = name
        self.id = id
        self.count = count

    def show_info(self):
        return f"Name: {self.name} id: {self.id} count : {self.count}"


obj = IFITSTE("IF","001")

obj1= KalushITSTEL("Kalush", "002", 500)

print(obj.show_info())

print(obj1.show_info())

class Transport:
    @abstractmethod
    def show_transport(self):
        pass

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Car(Transport):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def show_transport(self):
        return f"name = {self.name} \nspeed = {self.speed}"

class Moto(Transport):
    def __init__(self, name , speed, type):
        super().__init__(name, speed)
        self.type = type

    def show_transport(self):
        return f"name = {self.name} \nspeed = {self.speed} \ntype = {self.type}"


carchik = Car("Buggati", 70)
motorcycle = Moto("Tekken 250", 120, "enduro")
print(carchik.show_transport())
print(motorcycle.show_transport())"""


import os

"""file = open("IT STEP.txt", "w")
ask = "none"
while ask != "STOP":
    ask = input("Напишіть щось...")
    file.write(ask)

    file.write(" ")

file.close()"""

"""file = "NEWFile.txt"

with open("IT STEPsec.txt", "w") as itfile:
    itfile.write("NEW IFORMATION")

with open(file, "r") as myFile:
    print(myFile.readlines())"""

myBio = "MyBio.txt"

with open("MyBio.txt", "w") as bio:
    name = input("Enter your name: ")
    bio.write(name)
    bio.write(" ")
    age = input("Enter your age: ")
    bio.write(age)
    bio.write(" ")
    date = input("Enter your birthday date: ")
    bio.write(date)
    bio.write(" ")
    id = input("Enter your id: ")
    bio.write(id)
    bio.write(" ")