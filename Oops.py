# 1.Square Numbers and Return Their Sum

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqsum(self):
        print('Sum of squared numbers:',self.x**2 + self.y**2 + self.z**2)
x = int(input())
y = int(input())
z = int(input())
object1 = point(x,y,z)
print(object1.sqsum()) 




# 2 Implement a Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 / self.num1


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

obj = Calculator(num1, num2)
print(obj.add())      
print(obj.subtract()) 
print(obj.multiply()) 
print(obj.divide())


# 3. Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
name = input()
rollnumber = int(input())
student = Student()
student.setName(name)
student.setRollNumber(rollnumber)
name = student.getName()
rollNumber = student.getRollNumber()
print("Name:", name)
print("Roll Number:", rollNumber)
