import ctypes
import struct
from typing import Any
from Utilities.Utilities import coding_str

const = 'i i i 17s 17s 17s 15i 1s 3s'

class Inode(ctypes.Structure):
    _fields_ = [
        ("i_uid", ctypes.c_int),
        ("i_gid", ctypes.c_int),
        ("i_size", ctypes.c_int),
        ("i_atime", ctypes.c_char * 17),
        ("i_ctime", ctypes.c_char * 17),
        ("i_mtime", ctypes.c_char * 17),
        ("i_block", ctypes.c_int * 15),
        ("i_type", ctypes.c_char), # 0 = folder, 1 = file
        ("i_perm", ctypes.c_char * 3)
    ]

    def __init__(self):
        self.i_uid = -1
        self.i_gid = -1
        self.i_size = -1
        self.i_atime = b'\0'*17
        self.i_ctime = b'\0'*17
        self.i_mtime = b'\0'*17
        self.i_block = (ctypes.c_int * 15)(*[-1] * 15)
        self.i_type = b'\0' # 0 = carpeta, 1 = archivo
        self.i_perm = b'\0'*3 #UGO 

    def get_infomation(self):
        print("==Inode info")
        print(f"i_uid: {self.i_uid}")
        print(f"i_gid: {self.i_gid}")
        print(f"i_size: {self.i_size}")
        print(f"i_atime: {self.i_atime.decode()}")
        print(f"i_ctime: {self.i_ctime.decode()}")
        print(f"i_mtime: {self.i_mtime.decode()}")
        print(f"i_block: {list(self.i_block)}")
        print(f"i_type: {self.i_type.decode()}")
        print(f"i_perm: {self.i_perm.decode()}")
        
 
    def getConst(self):
        return const

    def doSerialize(self):
        serialize =  struct.pack(
            const,
            self.i_uid,
            self.i_gid,
            self.i_size,
            self.i_atime,
            self.i_ctime,
            self.i_mtime,
            *self.i_block,
            self.i_type,
            self.i_perm
        )
        return serialize
    
    def doDeserialize(self, data):
        unpacked_data = struct.unpack(const, data)
        (
        self.i_uid,
        self.i_gid,
        self.i_size,
        self.i_atime,
        self.i_ctime,
        self.i_mtime
        ) = unpacked_data[:6]

        self.i_block = (ctypes.c_int * 15)(*unpacked_data[6:21])

        (
        self.i_type,
        self.i_perm
        )  = unpacked_data[21:]

