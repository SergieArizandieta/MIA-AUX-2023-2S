

import ctypes
import struct
from Utilities.Utilities import coding_str

const = 'i i i i i 17s 17s i H i i i i i i i i'
class Superblock(ctypes.Structure):

    _fields_ = [
        ('filesystem_type', ctypes.c_int), 
        ('inodes_count', ctypes.c_int),
        ('blocks_count', ctypes.c_int),
        ('free_blocks_count', ctypes.c_int),
        ('free_inodes_count', ctypes.c_int),
        ('mtime', ctypes.c_char*17),
        ('umtime', ctypes.c_char*17),
        ('mcount', ctypes.c_int),
        ('magic', ctypes.c_uint16),
        ('inode_size', ctypes.c_int),
        ('block_size', ctypes.c_int),
        ('first_ino', ctypes.c_int), 
        ('first_blo', ctypes.c_int),
        ('bm_inode_start', ctypes.c_int),
        ('bm_block_start', ctypes.c_int),
        ('inode_start', ctypes.c_int),
        ('block_start', ctypes.c_int),
    ]

    def __init__(self):
        self.magic = 0xEF53
 
    def get_infomation(self):
        print("==Superblock info")
        print(f"filesystem_type: {self.filesystem_type}")
        print(f"inodes_count: {self.inodes_count}")
        print(f"blocks_count: {self.blocks_count}")
        print(f"free_blocks_count: {self.free_blocks_count}")
        print(f"free_inodes_count: {self.free_inodes_count}")
        print(f"mtime: {self.mtime.decode()}")
        print(f"umtime: {self.umtime.decode()}")
        print(f"mcount: {self.mcount}")
        print(f"magic: {hex(self.magic)}")
        print(f"inode_size: {self.inode_size}")
        print(f"block_size: {self.block_size}")
        print(f"first_ino: {self.first_ino}")
        print(f"first_blo: {self.first_blo}")
        print(f"bm_inode_start: {self.bm_inode_start}")
        print(f"bm_block_start: {self.bm_block_start}")
        print(f"inode_start: {self.inode_start}")
        print(f"block_start: {self.block_start}")

    def getConst(self):
        return const

    def doSerialize(self):
        serialize =  struct.pack(
            const,
            self.filesystem_type,
            self.inodes_count,
            self.blocks_count,
            self.free_blocks_count,
            self.free_inodes_count,
            self.mtime,
            self.umtime,
            self.mcount,
            self.magic,
            self.inode_size,
            self.block_size,
            self.first_ino,
            self.first_blo,
            self.bm_inode_start,
            self.bm_block_start,
            self.inode_start,
            self.block_start,
        )
        return serialize
    
    def doDeserialize(self, data):
        (self.filesystem_type, 
        self.inodes_count,
        self.blocks_count,
        self.free_blocks_count,
        self.free_inodes_count,
        self.mtime,
        self.umtime,
        self.mcount,
        self.magic,
        self.inode_size,
        self.block_size,
        self.first_ino,
        self.first_blo,
        self.bm_inode_start,
        self.bm_block_start,
        self.inode_start,
        self.block_start) = struct.unpack(const, data) 

    