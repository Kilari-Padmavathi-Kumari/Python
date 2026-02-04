class Student:
    def __init__(self,name,rollno,age):
        self.name = name
        #protect variable
        self._rollno = rollno
        #private variable
        self.__age = age
    # private method
    def __display(self):   
        print(f"hi myself {self.name} {self.__age} years old with roll no {self._rollno}")
    def displayPrivateData(self):
        self.__display()
#child class
class Branch(Student): 
    def show(self):
        print(f"my rollno is{self._rollno}")

B=Branch("kavya",2,34)
B.show() 
s1=Student("padma",1,23)
s1.displayPrivateData()
print(B._Student__age)
