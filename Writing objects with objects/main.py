import os
from load import * 
from Student import Student
from Profesor import Profesor

if __name__ == "__main__":
   print("=============NUEVA FORMA================")
   print("Current working directory:", os.getcwd())
   print("=====================================")
   print("=============PROFESOR 1==============") 

   # Creating three instances of the Profesor object
   Profesor1 = Profesor()
   Profesor1.set_infomation('0', 1, 1101523830201, 'Juan Perez', 'Matematica')
   Profesor1.display_info()

   print("=============STUDENT1 1==============")  
   Student1 = Student()
   Student1.set_infomation('0', 0, 3101523830201, 'Heather Gordillo', '202000999')
   
   Profesor1.student1 = Student1
   Profesor1.student1.display_info()

   print("=============STUDENT2 2==============")  
   Student2 = Student()
   Student2.set_infomation('0', 1, 3101523830201, 'Sergie Arizandieta', '202000111')

   Profesor1.student2 = Student2
   Profesor1.student2.display_info()

   # --------------------------- Reading and writing ---------------------------

   file_name = "./Writing objects with objects/example_file.adsj" 
   if (Fcreate_file(file_name)): exit()
   
   Crrfile = open(file_name, "rb+") 

   print("=============WRITING==============")
   displacement = 0
   arr = [Profesor1]
   for i in arr:
      Fwrite_displacement(Crrfile, displacement, i)
      displacement += len(i.doSerialize())
      print("=")
   
   print("=============READING==============")
   displacement = 0

   Profesor1 = Profesor()
   arr = [Profesor1]

   for i in arr:
      Fread_displacement(Crrfile,displacement,i)
      print("---profesor 1")
      i.display_info()
      print("---student 1")
      i.student1.display_info()
      print("---student 2")
      i.student2.display_info()
      displacement += len(i.doSerialize())
      print("------------------")
   
   Crrfile.close()  
   print("=============FINISH==============")