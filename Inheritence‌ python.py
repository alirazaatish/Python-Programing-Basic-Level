class male:
    def __init__(self):
         self.no_of_nose=1
         self.no_of_ears=2
    def eat(self):
        print("I can eat.")
    def work(self):
        print("I can work")

class female(male):
      def __init__(self,name):
           super().__init__()
           self.name=name

      def work(self):
           super().work()
           print("I am doing cooking.")

female_1=female("Aimen")
female_1.eat()
female_1.work()
print(female_1.no_of_ears)
print(female_1.name)
