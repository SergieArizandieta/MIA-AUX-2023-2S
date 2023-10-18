import ctypes
import struct
from Utilities.Utilities import coding_str

const = '1s 1s 1s i i 16s'
class Partition(ctypes.Structure):

    _fields_ = [
        ('status', ctypes.c_char),
        ('type', ctypes.c_char),
        ('fit', ctypes.c_char),
        ('start', ctypes.c_int),
        ('size', ctypes.c_int),
        ('name', ctypes.c_char * 16)
    ]

    def __init__(self):
        self.status = b'0'
        self.type = b'p'
        self.fit = b'w'
        self.start = -1
        self.size = -1
        self.name = b'\0'*16
 
    def set_infomation(self, status,type, fit, start, size, name):
        self.status = coding_str(status,1)
        self.type = coding_str(type,1)
        self.fit = coding_str(fit,1)
        self.start = start
        self.size = size
        self.name = coding_str(name,16)

    def get_infomation(self):
        print("==Partition info")
        print(f"Status: {self.status.decode()}")
        print(f"Type: {self.type.decode()}")
        print(f"Fit: {self.fit.decode()}")
        print(f"Start: {self.start}")
        print(f"Size: {self.size}")
        print(f"Name: {self.name.decode()}")

    def getConst(self):
        return const

    def doSerialize(self):
        serialize =  struct.pack(
            const,
            self.status,
            self.type,
            self.fit,
            self.start,
            self.size,
            self.name
        )
        return serialize
    
    def doDeserialize(self, data):
        self.status,self.type,self.fit,self.start,self.size,self.name = struct.unpack(const, data)

