class Human:
    def eat(self):
        print("I can eat.")

class male(Human):
    def work(self):
        print("I can work.")
class boy(male):
    pass

boy_1=boy()
boy_1.eat
boy_1.work
    