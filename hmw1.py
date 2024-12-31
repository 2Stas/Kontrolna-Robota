from random import randint
from uuid import uuid4
import random

class User:
    def init(self, balance, id, passw, name, address, credit):
        self.name = name
        self.balance = balance
        self.id = id
        self.passw = passw
        self.address = address
        self.credit = credit

    def login(self):
        global login

        namee = input("Введіть ім'я:  ")
        if namee == self.name.lower():
            login = True
            passsw = input("Введіть пароль:  ")
            if passsw == self.passw:
                login = True
                print("correct")
            else:
                print("Incorrect password")
                login = False
        else:
            print("Incorrect name")
            login = False

    def change_pass(self):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            new_passw = input("Введіть новий пароль:  ")

            user1.passw = new_passw

    def withdraw(self, amount):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            withdraw = self.balance - amount
            if self.balance < amount:
             print("У вас недостатньо коштів на рахунку для виконання дії")
            print("Залишок: ", withdraw)

    def work(self, hours):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            salary = hours * 12
            working = self.balance + salary
            print("Ви заробили: ", salary)
            print("Тепер у вас:", working)

    def credits(self, amount):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            self.credit = amount
            self.balance += amount
            print(f"credit = {self.credit}\n balance = {self.balance}")

    def pay_c(self, amount):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            if amount > self.credit:
                self.credit -= amount
                self.balance -= amount
                lyola = abs(self.credit)
                self.credit = 0
                self.balance += lyola

                print(f"credit = {self.credit}\n balance = {self.balance}")
            else:
                self.credit -= amount
                self.balance -= amount
                print(f"credit = {self.credit}\n balance = {self.balance}")

    def robbery(self):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            print("ти нечемний хлопчик якщо тобі настільки ліньки іти працювати.😒🤟")
            randint(1, 40)
            if randint == 5:
                self.balance += 200000
                global lacalut
                print("тобі вдалося пограбувати банк!🤑🤑🤑 Але тепер тебе шукає поліція, тоиу ти не зможеш брати кредит до кінця гри😥")
                lacalut = True
            else:
                print(f"О ні! Тебе впіймала поліція😥. Все ж таки ці прибомбаси з відео-ігор не працюють в реальному житті\n Тепер твоя гра закінчена, або ти можеш дати викуп який коштує 50000 гривень")
                final = input(f"Заплатити викуп? \n Так / Ні\n")
                global game
                if final == "Так".lower():
                    if self. balance < 50000:
                        print("От халепа. У тебе недостатньо коштів щоб це зробити😥☠💸💸💸")
                        game = False
                    else:
                        print("Після того як ти дав викуп тебе відпустили🥳")
                else:
                    print("Ну тоді ти будеш сидіти у тюрмі 20 років⏱")
                    game = False

    def translate(self, guy, amount):

        if amount > self.balance:
            print("У вас недостатньо коштів дял здійсення переказу")
        elif  amount == 0 or amount < 0:
            print("Неможливо переказати менше 0")
        else:
            self.balance -= amount
            print(f"Успішно передано {amount} користувачу {guy}")

    def logout(self):
        global login
        logout = input("Ви дійсно хочете вийти із акаунту? \n Так/Ні")
        if logout == "Так":
            print("Ви успішно вийшли із акаунту!")
            login = False
        else:
            print("Ви відхилили вихід із акаунту")

game = True
lacalut = False
login = False
user1 = User
user1.name = "Oleg"
user1.passw = "oleg-molotok"
user1.id = str(uuid4())
user1.balance = 1000
user1.address = "gigga nigga 24"
user1.credit = 0
print("Вас вітає наша підрбка Монобанку!")
print("щоб дізнатися команди напишіть 'help'")
while game:

    if login == False:
        anw = input("Введіть команду (спочатку зареєструйтеся будь ласка😭):  ")
    elif login == True:
        anw = input("Введіть команду:")

    if anw.startswith("hel"):
        print("\n Ввійти в акаунт = log in \n Змінити пароль = change password \n Зняти гроші = Withdraw \n Робота = work \n Пограбувати банк = robbery \n Вийти з акаунту = log out \n Переказувати гроші = translate \n Взяти кредит = credit \n Виплатити кредит = pay credit")

    elif anw.startswith("log i"):
        user1.login(user1)

    elif anw.startswith("chan"):
        old_passw = input("Введіть старий пароль:  ")
        if old_passw == user1.passw:
            user1.change_pass(user1)
        else:
            print("incorrect try to change password")

    elif anw.startswith("withd"):
        amount = int(input("Введіть сумму яку хочете зняти:  "))
        user1.withdraw(user1, amount)

    elif anw.startswith("wo"):
        hours = int(input("Введіть скільки годин ви будете пахати:  "))
        user1.work(user1, hours)

    elif anw.startswith("cred"):
        if login == False:
            print("Зареєстуйтесь щоб скористатися дією🙏")
        elif login == True:
            if lacalut == False:
                amount = int(input("Введіть сумму яку хочете зняти:  "))
                user1.credits(user1, amount)
            else:
                print("Ти не можеш брати кредит, бо інакше тебе зловить поліція")

    elif anw.startswith("pay cred"):
        amount= int(input("Введіть скільки гривень ви хочете заплатити за кредит:  "))
        user1.pay_c(user1, amount)

    elif anw.startswith("inf"):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            print(f"name = {user1.name}\n password = {user1.passw}\n id = {user1.id}\n balance = {user1.balance}\n credit = {user1.credit}\n address = {user1.address}")

    elif anw.startswith("rob"):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            user1.robbery(user1)

    elif anw.startswith("tran"):
        if login == False:
            print("Спочатку увійдіть у аккаунт😡")
        elif login == True:
            guy = input("Введіть ім'я користувача якому хочете переказати гроші:  ")
            amount = int(input(f"Введіть скільки гривень ви хочете переказати {guy}:  "))
            user1.translate(user1, guy, amount)

        elif anw.startswith("log o"):
            if login == False:
                print("Спочатку увійдіть у аккаунт😡")
            elif login == True:
                user1.logout(user1)

        else:
            print("Недійсна команда, спробуйте ще раз")