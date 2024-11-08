#AUTHOR: Trevor Conger
#DATE: 11/8/24
#TITLE: OOP Employee

#Employee Class: 
#EMPLOYEE CLASS has 4 instance variables
#   Init: NAME, ID_NUMBER, Department, JobTitle
#   GETTERS
#       getName, getID, getDepartment, getJobTitle
#   SETTERS
#       setName, setID, setDepartment, setJobTitle
class Employee:
    def __init__(self, name, idNumber, department, jobTitle):
        self.__name = name
        self.__idNumber = idNumber
        self.__department = department
        self.__jobTitle = jobTitle
    
    #Getter to get Name
    #return name
    def getName(self):
        return self.__name
    #Getter to get ID number
    #return ID Number
    def getID(self):
        return self.__idNumber
    #Getter to get Department
    #return Department
    def getDepartment(self):
        return self.__department
    #Getter to get Job Title
    #return Job Title
    def getJobTitle(self):
        return self.__jobTitle
    
    #Setter to set Name
    #set name to self.__name
    def setName(self, name):
        self.__name = name
    #Setter to set ID Number
    #set ID number to self.__idNumber
    def setID(self, idNumber):
        self.__idNumber = idNumber
    #Setter to set the Department
    #set Department to self.__department
    def setDepartment(self, department):
        self.__department = department
    #Setter to set Job Title
    #set Job Title to self.__jobTitle
    def setJobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

#EmployeeRecords class
#     Init: EMPLOYEE NAME, EMPLOYEE ID, DEPARTMENT, JOB TITLE
#displayRecords
#     Display to user in format that is easily understandable
#     Display empyloyee details from employees array of objects
class EmployeeRecords:
    def __init__(self):
        self.employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
        self.employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
        self.employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
        self.employees = [self.employee1, self.employee2, self.employee3]
    
    def displayRecords(self):
        print(f"{'Name':<15} {'ID Number':<10} {'Department':<15} {'Job Title':<15}")
        print("-" * 55)
        for employee in self.employees:
            print(f"{employee.getName():<15} {employee.getID():<10} {employee.getDepartment():<15} {employee.getJobTitle():<15}")

def main():
    records = EmployeeRecords()
    records.displayRecords()

if __name__ == "__main__":
    main()