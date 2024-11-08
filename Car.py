#AUTHOR: Trevor Conger UNWSP
#DATE: 11/8/24
#TITLE: OOP Car

#CAR CLASS
# INIT year, make, speed
# ACCELERATE: increases speed 5 mph
# BRAKE: decreases speed 5 mph
# GETTER: getSpeed , return self.__speed
class Car:
    def __init__(self, year, make, speed):
       self.__year = year
       self.__make = make
       self.__speed = speed

    def accelerate(self):
       self.__speed+=5
   
    def brake(self):
       self.__speed-=5
   
    def getSpeed(self):
       return self.__speed



