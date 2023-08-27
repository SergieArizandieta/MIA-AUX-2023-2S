import pickle
import ctypes


class Student(ctypes.Structure):

    # manejamos atributos a nivel de byte
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
        self.carne = b'\0'*16

    def set_type(self, type):
        self.type = type.encode('utf-8')[:1]

    def set_id_student(self, id_student):
        self.id_student = id_student

    def set_cui(self, cui):
        self.cui = cui
    
    def set_name(self, name):
        self.name = name.encode('utf-8')[:15].ljust(16, b'\0')

    def set_carne(self, carne):
        self.carne = carne.encode('utf-8')[:9].ljust(10, b'\0')

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

'''
print("0:",ctypes.sizeof(Student()))  # Imprimir el tamaño en bytes de la estructura

# Crear una instancia de Partition
partition = Student()
partition.set_infomation('1', 1, 3101523830201, 'Juan Perez', '201612345')
partition.display_info()


print("1:",len(pickle.dumps(Student)))

# Crear una instancia de Partition
partition = Student()
partition.display_info()

#print("2:",ctypes.sizeof(partition))  # Imprimir el tamaño en bytes de la estructura
print("2:",len(pickle.dumps(Student)))
'''