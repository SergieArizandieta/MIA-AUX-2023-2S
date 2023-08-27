import os
from load import * 
from Student import Student
from Profesor import Profesor
import ctypes

if __name__ == "__main__":
   print("=============NUEVA FORMA================")
   print("Current working directory:", os.getcwd())
   print("=====================================")

   # Creating three instances of the Profesor object
   Profesor1 = Profesor()
   Profesor1.set_infomation('0', 1, 1101523830201, 'Juan Perez', 'Matematica')
   Profesor1.display_info()
   print("=============PROFESOR1==============")   
   Profesor2 = Profesor()
   Profesor2.set_infomation('1', 2, 2101523830201, 'Sergie Arizandieta', 'Computacion')
   Profesor2.display_info()
   print("=============PROFESOR2==============")  

   Student1 = Student()
   Student1.set_infomation('0', 1, 3101523830201, 'Heather Gordillo', '202000999')
   Student1.display_info()
   print("=============STUDENT1==============")  
   Student2 = Student()
   Student2.set_infomation('1', 2, 4101523830201, 'Alisson Hernandez', '202000111')
   Student2.display_info()
   print("=============STUDENT2==============")

   file_name = "./Clase 3 Update/example_file.adsj" 
   if (Fcreate_file(file_name)): exit()
   
   Crrfile = open(file_name, "rb+") 

   print("=============WRITING==============")
   displacement = 0
   arr = [Profesor1, Profesor2, Student1, Student2]
   for i in arr:
      Fwrite_displacement(Crrfile, displacement, i)
      displacement += len(i.doSerialize())
      print("=")
   

   print("=============READING==============")
   displacement = 0

   Profesor1 = Profesor()
   Profesor2 = Profesor()
   Student1 = Student()
   Student2 = Student()
   arr = [Profesor1, Profesor2, Student1, Student2]

   print("===Profesor===")
   for i in arr:
      Fread_displacement(Crrfile,displacement,i)
      i.display_info()
      displacement += len(i.doSerialize())
      print("=")
   
   Crrfile.close()  
   print("=============FINISH==============")