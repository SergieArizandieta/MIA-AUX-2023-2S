import ctypes
import struct
from Utilities import coding_str

const = '1s I q 16s 9s'
#1s s un string de 1 caracter
#I es un entero
#q es un long long
#16s es un string de 16 caracteres
#9s es un string de 9 caracteres

#1s I q 16s 9s es debido a los atributos de la clase Student
class Student(ctypes.Structure):

    _fields_ = [
        ('type', ctypes.c_char),
        ('id_student', ctypes.c_int),
        ('cui', ctypes.c_longlong),
        ('name', ctypes.c_char * 16),
        ('carne', ctypes.c_char * 9) 
    ]

    def __init__(self):
        self.type = b'1'
        self.id_student = 0
        self.cui = 0
        self.name = b'\0'*16
        self.carne = b'\0'*9

    def set_type(self, type):
        self.type = coding_str(type,1)
   
    def set_id_student(self, id_student):
        self.id_student = id_student

    def set_cui(self, cui):
        self.cui = cui
    
    def set_name(self, name):
        self.name = coding_str(name,16)

    def set_carne(self, carne):
        self.carne = coding_str(carne,9)
 
    def set_infomation(self, type, id_student, cui, name, carne):
        self.set_type(type)
        self.set_id_student(id_student)
        self.set_cui(cui)
        self.set_name(name)
        self.set_carne(carne)
    
    def display_info(self):
        print(f"Type: {self.type.decode()}")
        print(f"Id Student: {self.id_student}")
        print(f"Cui: {self.cui}")
        print(f"Name: {self.name.decode()}")
        print(f"Carnet: {self.carne.decode()}")

    def getConst(self):
        return const

    def doSerialize(self):
        serialize =  struct.pack(
            const,
            self.type,
            self.id_student,
            self.cui,
            self.name,
            self.carne
        )
        return serialize
    
    def doDeserialize(self, data):
        self.type, self.id_student, self.cui, self.name, self.carne = struct.unpack(const, data)

