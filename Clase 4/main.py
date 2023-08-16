import os
from Tutor import Tutor
from Student import Student

if __name__ == "__main__":
   print("=============CLASE 4================")
   print("Current working directory:", os.getcwd())
   print("=====================================")

   
   print("=============PROFESOR 1==============") 
   tutor1 = Tutor()
   tutor1.set_infomation("Juan Perez", 123456789, 30, "MIA")
   tutor1.display_info()

   print("=============STUDENT1 1==============")  
   Student1 = Student()
   Student1.set_infomation('0', 0, 3101523830201, 'Heather Gordillo', '202000999')
   
   tutor1.student1 = Student1
   tutor1.student1.display_info()

   print("=============STUDENT2 2==============")  
   Student2 = Student()
   Student2.set_infomation('0', 1, 3101523830201, 'Sergie Arizandieta', '202000111')

   tutor1.student2 = Student2
   tutor1.student2.display_info()

   serializeData = tutor1.doSerialize()
   #print("data:",serializeData)

   print("=============PROFESOR 2==============") 
   tutor2 = Tutor()
   tutor2.doDeserialize(serializeData)
   tutor2.display_info()
   tutor2.student1.display_info()
   tutor2.student2.display_info()