import random
import ctypes
import struct
import datetime
from Utilities.Utilities import coding_str
from Objects.Partition import *
from Objects.Content import *

const = 'i 10s i 1s'
class Folderblock(ctypes.Structure):

    def __init__(self):
        self.Content = [Content(),Content(),Content(),Content()]

    def get_infomation(self):
        print("==Folderblock info")
        print(f"Content: {self.Content}")

    def getConst(self):
        return const
    
    def doSerialize(self): 
        return  self.Content[0].doSerialize() + self.Content[1].doSerialize() + self.Content[2].doSerialize() + self.Content[3].doSerialize()

    def doDeserialize(self, data):
        sizeContent = struct.calcsize(Content().getConst())

        for i in range(4):
            dataContent = data[(i*sizeContent): ((i+1)*sizeContent)]
            self.Content[i] = Content()
            self.Content[i].doDeserialize(dataContent)
            


        
        
            
     
        



