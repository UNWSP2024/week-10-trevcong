#AUTHOR: Trevor Conger UNWSP
#DATE: 11/8/24
#TITLE: OOP Car

from Car import Car

#Module for Car class
# INIT a car object with instance variables as YEAR, MAKE, SPEED
#       ITERATE 5 times
#            calling accelerate method
#            calling getSpeed method
#            Print to user speed and iteration
#       ITERATE 5 times
#            calling brake method
#            calling getSpeed method
#            Print to user speed and iteration
def main():
    myCar = Car("1992", "Audi", 0)

    print("Accelerating...")
    for i in range(5):
        myCar.accelerate()
        speed = myCar.getSpeed()
        print(f"Current speed after acceleration {i+1}: {speed} mph")
    
    print("\nBraking...")
    for i in range(5):
        myCar.brake()
        speed = myCar.getSpeed()
        print(f"Current speed after brake {i+1}: {speed} mph")

if __name__ == "__main__":
    main()