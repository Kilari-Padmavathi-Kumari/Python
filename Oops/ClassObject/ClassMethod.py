class College:
    # Class variable
    college_name = "ABC College"

    # Class method
    @classmethod
    def show_college(cls):
        print("College Name:", cls.college_name)

# Calling class method using class name
College.show_college()




'''class Rectangle:
    count=0
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        Rectangle.count+=1

    @classmethod
    def get_Count(cls):
        return cls.count
r1=Rectangle(15,8)
r2=Rectangle(7,4)
print(Rectangle.get_Count())'''
        