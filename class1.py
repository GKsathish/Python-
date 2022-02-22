# In python method-overloading,constructor-overloading is not available.
# In python we can take many constructor but python will consider last constructor only from them.
class Student:
    clgname="GKF FAMILY"
    def __init__(s,roll_no,name):# self we can also write s or g or f .....
        s.roll_no=roll_no
        s.name=name 
    def talk(se):
        print("Hello Good Morning",se.name)
        print("Roll No is :",se.roll_no)
        print("-" * 20)
    @classmethod
    def getclgname(cl):
        print("College Name is:",cl.clgname)
    @staticmethod 
    def avg(x,y):
        print((x+y)/2)    
        
s1=Student(100, "gk")
print(s1.clgname)
s1.talk()
Student.getclgname()
Student.avg(10,20)
s1.avg(10,20)