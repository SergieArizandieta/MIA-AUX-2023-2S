import random
import ctypes
import struct
import datetime
from Utilities.Utilities import coding_str
from Objects.Partition import *

const = 'i 10s i 1s'
class MBR(ctypes.Structure):

    _fields_ = [
        ('size', ctypes.c_int),
        ('date_creation', ctypes.c_char * 16),
        ('asignature', ctypes.c_int ),
        ('fit', ctypes.c_char)
    ]

    def __init__(self):
        self.size = -1
        self.date_creation = b'\0'*16
        self.asignature = -1
        self.fit = b'0'
        self.partitions = [Partition(),Partition(),Partition(),Partition()]

    def set_infomation(self,size,fit):
        self.size = size
        self.date_creation = coding_str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),16)
        self.asignature = random.randint(0, 2**31 - 1)
        self.fit = coding_str(fit,1)

    def get_infomation(self):
        print("==MBR info")
        print(f"Size: {self.size}")
        print(f"Date Creation: {self.date_creation.decode()}")
        print(f"Asignature: {self.asignature}")
        print(f"Fit: {self.fit.decode()}")
        print(f"Partitions: {self.partitions}")

    def getConst(self):
        return const
    
    def doSerialize(self):
        serialize = struct.pack(
            const,
            self.size,
            self.date_creation,
            self.asignature,
            self.fit,
        )        
        return serialize + self.partitions[0].doSerialize() + self.partitions[1].doSerialize() + self.partitions[2].doSerialize() + self.partitions[3].doSerialize()

    def doDeserialize(self, data):
        sizeMBR = struct.calcsize(const)
        sizePartition = struct.calcsize(Partition().getConst())

        dataMBR = data[:sizeMBR]
        self.size, self.date_creation, self.asignature, self.fit = struct.unpack(const, dataMBR)

        for i in range(4):
            dataPartition = data[sizeMBR + (i*sizePartition):sizeMBR + ((i+1)*sizePartition)]
            self.partitions[i] = Partition()
            self.partitions[i].doDeserialize(dataPartition)
            


        
        
            
     
        



