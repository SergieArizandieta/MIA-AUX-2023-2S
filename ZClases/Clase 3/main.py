import os
from Profesor import Profesor
from Student import Student
from load import *

if __name__ == "__main__":
    print("=============Una solucion HT1================")
    print("Current working directory:", os.getcwd())
    print("=====================================")

    # Creating three instances of the Profesor object
    Profesor1 = Profesor()
    Profesor1.set_infomation('0', 1, 1101523830201, 'Juan Perez', 'Matematica')
    Profesor1.display_info()
    print("=============PROFESOR1==============")   
    Profesor2 = Profesor()
    Profesor2.set_infomation('0', 2, 2101523830201, 'Sergie Arizandieta', 'Computacion')
    Profesor2.display_info()
    print("=============PROFESOR2==============")  
   
    Student1 = Student()
    Student1.set_infomation('1', 1, 3101523830201, 'Heather Gordillo', '202000999')
    Student1.display_info()
    print("=============STUDENT1==============")  
    Student2 = Student()
    Student2.set_infomation('1', 2, 4101523830201, 'Alisson Hernandez', '202000111')
    Student2.display_info()
    print("=============STUDENT1==============")


    file_name = "./Clase 3/example_file.adsj"  # Name of the file to be created

    fileCreate = Fcreate_file(file_name)
    if (fileCreate == None): exit()
    fileCreate.close()

    Crrfile = open(file_name, "rb+")  # Open the file in read and write mode
    Winit_size(Crrfile,5)
    #exit()

    print("=============WRITING==============")

    displacement = 0
    

    '''
        #NORMAL WRITING
        Fwrite_displacement(Crrfile, displacement, Profesor1)
        displacement += len(pickle.dumps(Profesor()))
        Fwrite_displacement(Crrfile, displacement, Profesor2)
        displacement += len(pickle.dumps(Profesor()))
        Fwrite_displacement(Crrfile, displacement, Student1)
        displacement += len(pickle.dumps(Student()))
        Fwrite_displacement(Crrfile, displacement, Student2)
    '''

    arr = [Profesor1, Profesor2, Student1, Student2]
    for i in arr:
        Fwrite_displacement(Crrfile, displacement, i)
        displacement += len(pickle.dumps(i))
        
    print("=============READING==============")
    displacement = 0
   
    '''
        #NORMAL READING
        ReadObject = Fread_displacement(Crrfile, displacement,ReadObject)
        ReadObject.display_info()
        displacement += len(pickle.dumps(ReadObject))
        ReadObject = Fread_displacement(Crrfile, displacement,ReadObject)
        ReadObject.display_info()
        displacement += len(pickle.dumps(ReadObject))
        ReadObject = Fread_displacement(Crrfile, displacement,ReadObject)
        ReadObject.display_info()
        displacement += len(pickle.dumps(ReadObject))
        ReadObject = Fread_displacement(Crrfile, displacement,ReadObject)
        ReadObject.display_info()
    '''

    for i in range(len(arr)):
        ReadObject = None
        ReadObject = Fread_displacement(Crrfile, displacement,ReadObject)
        if (ReadObject == None): break
        ReadObject.display_info()
        displacement += len(pickle.dumps(ReadObject))
        print("=")
   
    Crrfile.close()  
    print("=============FINISH==============")
        



   


    
   