class student:
    
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa


stu1=student("Nishka",9.1)
stu2=student("Ravi",7.5)

print(f"{stu1.name} has more marks than {stu2.name} and {stu2.name} loves {stu1.name}")



