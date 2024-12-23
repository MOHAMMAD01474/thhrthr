class Student:

    def __init__(self, first_name, last_name, national_number, student_number, GPA , age ):
        
        self.first_name = first_name 

        self.last_name = last_name

        self.age = age 

        self.national_number = national_number

        self.student_number =  student_number

        self.GPA = GPA
    
      
    def get_age(self):
        return ("The "+self.first_name + 's age is ' + str(self.age))
    
    def get_firsr_name(self):
        return ("The first name: "+ self.first_name)


student_1 = Student('Mahdi', 'Zamani' ,  '00218140162025' , 2124303553 , 19 , 22)

student_2 = Student('Amirali', 'Baghery' ,  '00232240082013' , 4022128458 ,18.88 , 21)

student_3 = Student('Rasool', 'Rezaee' ,  '00141730133052' ,'0025074111' , 19.90 , 22)


print(student_3.get_firsr_name())
print(student_3.get_age())

