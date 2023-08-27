import pickle
import ctypes


class Profesor(ctypes.Structure):

    # manejamos atributos a nivel de byte
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
      

    def set_type(self, type):
        self.type = type.encode('utf-8')[:1]

    def set_id_profesor(self, id_profesor):
        self.id_profesor = id_profesor

    def set_cui(self, cui):
        self.cui = cui
    
    def set_name(self, name):
        self.name = name.encode('utf-8')[:15].ljust(16, b'\0')

    def set_course(self, course):
        self.course = course.encode('utf-8')[:15].ljust(16, b'\0')


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

'''
print("0:",ctypes.sizeof(Profesor()))  # Imprimir el tamaño en bytes de la estructura

# Crear una instancia de Partition
partition = Profesor()
partition.set_infomation('1', 1, 3101523830201, 'Juan Perez', 'Matematica')
partition.display_info()


print("1:",len(pickle.dumps(Profesor)))

# Crear una instancia de Partition
partition = Profesor()
partition.display_info()

#print("2:",ctypes.sizeof(partition))  # Imprimir el tamaño en bytes de la estructura
print("2:",len(pickle.dumps(Profesor)))
'''