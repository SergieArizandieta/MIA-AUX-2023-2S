import ctypes
import struct
from Utilities.Utilities import coding_str

const = '64s'
class Fileblock(ctypes.Structure):

    _fields_ = [
        ('b_content', ctypes.c_char*64),
    ]

    def __init__(self):
        self.b_content = b'\0'*64
 
    def set_infomation(self,b_content):
        self.b_content = coding_str(b_content,64)
 
    def get_infomation(self):
        print("==Fileblock info")
        print(f"b_content: {self.b_content.decode()}")

    def getConst(self):
        return const

    def doSerialize(self):
        serialize =  struct.pack(
            const,
            self.b_content,
        )
        return serialize
    
    def doDeserialize(self, data):
        data = struct.unpack(const, data)
        self.b_content = data[0]

