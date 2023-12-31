import ctypes
import struct
from Student import Student
from Utilities import coding_str

const = '1s I q 16s 16s'
#1s significa 1 caracter
#I significa 1 entero
#q significa 1 long long
#16s significa 16 caracteres
#16s significa 16 caracteres

#1s I q 16s 9s es debido a los atributos de la clase Student
class Profesor(ctypes.Structure):

    _fields_ = [
        ('type', ctypes.c_char),
        ('id_profesor', ctypes.c_int),
        ('cui', ctypes.c_longlong ),
        ('name', ctypes.c_char * 16),
        ('course', ctypes.c_char * 16)
    ]

    def __init__(self):
        self.type = b'0'
        self.id_profesor = 0
        self.cui = 0
        self.name = b'\0'*16
        self.course = b'\0'*16
        self.student1 = Student()
        self.student2 = Student()

      
    def set_type(self, type):
        self.type = coding_str(type,1)

    def set_id_profesor(self, id_profesor):
        self.id_profesor = id_profesor

    def set_cui(self, cui):
        self.cui = cui
    
    def set_name(self, name):
        self.name = coding_str(name,16)

    def set_course(self, course):
        self.course = coding_str(course,16)

    def set_infomation(self, type, id_profesor, cui, name, course):
        self.set_type(type)
        self.set_id_profesor(id_profesor)
        self.set_cui(cui)
        self.set_name(name)
        self.set_course(course)
    
    def display_info(self):
        print(f"Type: {self.type.decode()}")
        print(f"Id Profesor: {self.id_profesor}")
        print(f"Cui: {self.cui}")
        print(f"Name: {self.name.decode()}")
        print(f"Course: {self.course.decode()}")

    def getSerlized(self):
        return const
    
    def doSerialize(self):
        person_data = struct.pack(
            const,
            self.type,
            self.id_profesor,
            self.cui,
            self.name,
            self.course
        )        
        return person_data + self.student1.doSerialize() + self.student2.doSerialize()

    def doDeserialize(self, data):
        sizeProfesor = struct.calcsize(const)
        sizeStudent = struct.calcsize(self.student1.getConst())

        person_data = data[:sizeProfesor]
        self.type, self.id_profesor, self.cui, self.name, self.course = struct.unpack(const, person_data)
            
        student_data = data[sizeProfesor:sizeProfesor+sizeStudent]
        self.student1 = Student()
        self.student1.doDeserialize(student_data)

        student_data = data[sizeProfesor+sizeStudent:sizeProfesor+sizeStudent+sizeStudent]
        self.student2 = Student()
        self.student2.doDeserialize(student_data)
        
            
     
        



