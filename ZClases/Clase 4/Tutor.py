import ctypes
import struct
from Utilities import coding_str
from Student import Student

const = '16s I q 16s'
#16 bytes
#4 bytes
#8 bytes
#16 bytes
class Tutor(ctypes.Structure):
   
   _fields_ = [
         ("name", ctypes.c_char * 16), # 16 bytes
         ("edad", ctypes.c_int), # 4 bytes 
         ("cui",  ctypes.c_longlong), # 8 bytes 
         ("course", ctypes.c_char * 16) # 16 bytes
         # Total: 44 bytes
   ]

   def __init__(self):
      self.name = b'\0'*16
      self.age = -1
      self.cui = -1
      self.course = b'\0'*16
      self.student1 = Student()
      self.student2 = Student()

   def set_name(self, name):
        self.name = coding_str(name, 16)

   def set_cui(self, cui):
        self.cui = cui
   
   def set_age(self, age):
        self.age = age

   def set_course(self, course):
         self.course = coding_str(course, 16)

   def set_infomation(self,name, cui, age, course):
      self.set_name(name)
      self.set_cui(cui)
      self.set_age(age)
      self.set_course(course)
       
   def display_info(self):
      print(f"Name: {self.name.decode()}")
      print(f"Cui: {self.cui}")
      print(f"Age: {self.age}")
      print(f"Course: {self.course.decode()}")

   def doSerialize(self):
      tutor_data = struct.pack(const, self.name, self.age, self.cui, self.course)
   
      return tutor_data + self.student1.doSerialize() + self.student2.doSerialize()
   
   def doDeserialize(self, data):
      sizeProfesor = struct.calcsize(const)
      sizeStundent = struct.calcsize(self.student1.getConst())

      tutor_data = data[:sizeProfesor]
      self.name, self.age, self.cui, self.course = struct.unpack(const, tutor_data)

      student1_data = data[sizeProfesor:sizeProfesor+sizeStundent]
      self.student1.doDeserialize(student1_data)

      student2_data = data[sizeProfesor+sizeStundent:]
      self.student2.doDeserialize(student2_data)

   
         