class Human:
      def eat(self):
           print("I can eat.")
      def work(self):
            print("I can work.")
class Male(Human): 
      def sleep(self):
            print("i can sleep.")
class boy(Male):
      def work(self):
            #super().work()
            print("I can code.")
Boy_1=boy()
Boy_1.eat()
Boy_1.sleep()
Boy_1.work()