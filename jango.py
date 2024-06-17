
import time
class demo:
    def PrintNames(self):
        Names=['Rama','seetha','ravana']
        for i in Names:
            print(i)
            time.sleep(2)
    def Printnum(self):
         for i in range(10):
            print(i)
            time.sleep(2)
    def add(self):
        a=10
        b=20
        c=a+b 
        print('sum is ', c) 
d=demo()
d.PrintNames()
d.Printnum()
d.add()


        
# import time
# class demo:
#     def PrintNames(self):
#         for i in range(1,100,2):
#             print(i)
#             # time.sleep(2)
#     def Printnum(self):
#          for i in range(0,100,2):
#             print(i)
#             # time.sleep(2)
 
# d=demo()
# d.PrintNames()
# d.Printnum()
# d.add()

