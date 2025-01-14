"""class Transport:
    def __init__(self, count_of_wheels, fuel, name,color,speed,can_be_used):
        self.count_of_wheels=count_of_wheels
        self.fuel=fuel
        self.name=name
        self.color=color
        self.speed=speed
        self.can_be_used=can_be_used

    def show(self):
        print(f"Name {self.name} Color {self.color} Speed {self.speed} fuel {self.fuel} count_of_wheels {self.count_of_wheels} can_be_used {self.can_be_used}")

class Car(Transport):
    def __init__(self, count_of_wheels, fuel, name,color,speed,can_be_used, count_of_seats):
        super().__init__(count_of_wheels, fuel, name, color, speed, can_be_used)
        self.count_of_seats= count_of_seats


    def show(self):
        print(f"Name {self.name} Color {self.color} Speed {self.speed} fuel {self.fuel} count_of_wheels {self.count_of_wheels} can_be_used {self.can_be_used} count_of_seats {self.count_of_seats}")

class Moto(Transport):
    def __init__(self, count_of_wheels, fuel, name,color,speed,can_be_used, type):
        self.type = type
        super().__init__(count_of_wheels, fuel, name,color,speed,can_be_used)

    def show(self):
        print(f"Name {self.name} Color {self.color} Speed {self.speed} fuel {self.fuel} count_of_wheels {self.count_of_wheels} can_be_used {self.can_be_used} type {self.type}")


obj = Transport(0,"Default","Default","Default",0,False)
obj.show()

obj1= Car(4,"gas","Audi A4", "Green", 320, True,5)
obj1.show()

obj2 =Moto(2,"gas","Yamaha R1","red", 400, True, "sport")
obj2.show()
"""

"""class Book:
    def __init__(self, title, author, count_of_pages):
        self.title = title
        self.author = author
        self.count_of_pages = count_of_pages

    def info(self):
        print(f"Title = {self.title} \nAuthor = {self.author} \nCount of pages = {self.count_of_pages}\n\n")

class Magazine(Book):
    def __init__(self, title, author, count_of_pages, sponsored, pictures):
        super().__init__(title, author, count_of_pages)
        self.sponsored = sponsored
        self.pictures = pictures

    def info(self):
        print(f"Title = {self.title} \nAuthor = {self.author} \nCount of pages = {self.count_of_pages} \nSponsored = {self.sponsored} Pictures = {self.pictures}\n\n")

class EBook(Book):
    def __init__(self, title, author, count_of_pages, can_be_download, price):
        super().__init__(title, author, count_of_pages)
        self.can_be_download = can_be_download
        self.price = price

    def info(self):
        print(f"Title = {self.title} \nAuthor = {self.author} \nCount of pages = {self.count_of_pages} \nCan be download = {self.can_be_download} \nprice = {self.price}\n\n")

class Emagazine(Book):
    def __init__(self, title, author, count_of_pages, can_be_download, price, count):
        super().__init__(title, author, count_of_pages)
        self.can_be_download = can_be_download
        self.price = price
        self.count = count

    def info(self):
        print(
            f"Title = {self.title} \nAuthor = {self.author} \nCount of pages = {self.count_of_pages} \nCan be download = {self.can_be_download} \nprice = {self.price} Count = {self.count}\n\n")

book = Book("How to destroy your pc", "Oleg Molotok", 50)
book.info()
magazine = Magazine("How to destroy your pc but magazine", "Oleg NeMolotok", 60, True, 20)
magazine.info()
ebook = EBook("How to destroy your pc but ebook", "Oleg Molotok", 40, True, "2$")
ebook.info()
emagazine = Emagazine("How to destroy your pc but emagazine", "Oleg NeMolotok", 60, False, "3$", 10)
emagazine.info()
"""


import random

class Person:
    def __init__(self, name, last_name, id):
        self.name = name
        self.last_name = last_name
        self.id = id

    def show(self):
        print(f"Name = {self.name} \nLast Name = {self.last_name} \nId = {self.id}")

class Student(Person):
    def __init__(self, name, last_name):
        id = random.randint(1, 100)
        super().__init__(name, last_name, id)

class Worker(Student):
    def __init__(self, name, last_name, id, age, hours_of_work, salary):
        super().__init__(name, last_name)
        self.age = age
        self.hours_of_work = hours_of_work
        self.salary = salary

    def change_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
            print(f"Salary updated to {self.salary}\n")
        else:
            print("Invalid salary amount")

class Teacher(Worker):
    def __init__(self, name, last_name, id, age, hours_of_work, salary, count_of_groups, size_of_group):
        super().__init__(name, last_name, id, age, hours_of_work, salary)
        self.count_of_groups = count_of_groups
        self.size_of_group = size_of_group
        self.group_sizes = [0] * count_of_groups

    def add_student_to_group(self, group_index):
        if 0 <= group_index < self.count_of_groups:
            if self.group_sizes[group_index] < self.size_of_group:
                self.group_sizes[group_index] += 1
                print(f"Student added to group {group_index + 1}. Current size: {self.group_sizes[group_index]}")
            else:
                print(f"Group {group_index + 1} is already full.")
        else:
            print("Invalid group index.")



obj = Worker("Oleg", "Tyty", "1235678", 25, 40, 50000)
obj.show()
print(f"Salary: {obj.salary}")
obj.change_salary(60000)

teacher = Teacher("Matviy", "SigmaBoy", "44543445", 30, 20, 70000, 2, 3)
teacher.add_student_to_group(0)
teacher.add_student_to_group(1)
teacher.add_student_to_group(0)
teacher.add_student_to_group(0)


students = [Student("Student1", "LastName1"),
            Student("Student2", "LastName2"),
            Student("Student3", "LastName3"),
            Student("Student4", "LastName4"),
            Student("Student5", "LastName5"),
            Student("Student6", "LastName6"),
            Student("Student7", "LastName7")]


print("\nStudents with ID less than 50:")
for student in students:
    if student.id < 50:
        student.show()


workers = [
    Worker("Nikitka", "Dobro", 101, 40, 60, 50000),
    Worker("Vlad", "Baruga", 102, 42, 102, 60000),
    Worker("Stepan", "Stepanuch", 103, 52, 34, 30000)]
for worker in workers:
    if worker.salary > 40000:
        worker.show()
