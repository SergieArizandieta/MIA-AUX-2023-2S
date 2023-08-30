import struct
import math
import datetime
from Load.Load import *
from Utilities.Utilities import printConsole,printError,get_sizeB
from Global.Global import mounted_partitions
from Objects.Inode import *
from Objects.Fileblock import *
from Objects.Superblock import *

def mkfs(args):
    print(" --- Ejecutando mkfs --- ")
    print("args: ", args)

    mPartition = None
    for partition in mounted_partitions:
        if partition[0] == args.id:
            mPartition = partition
            break

    if mPartition is None: return printError("La particion no esta montada")

    # numerador = (partition_montada.size - sizeof(Structs::Superblock)
    # denrominador base = (4 + sizeof(Structs::Inodes) + 3 * sizeof(Structs::Fileblock))
    # temp = "2" ? 0 : sizeof(Structs::Journaling)
    # denrominador = base + temp
    # n = floor(numerador / denrominador)
    
    numerator = mPartition[1].size - struct.calcsize(Superblock().getConst())
    denominator = 4 + struct.calcsize(Inode().getConst()) + 3 * struct.calcsize(Fileblock().getConst())
    temp = 0 if args.fs == 2 else 0
    denominator += temp
    n = math.floor(numerator / denominator)
    
    # creating superblock
    new_superblock = Superblock()
    new_superblock.inodes_count = 0
    new_superblock.blocks_count = 0

    new_superblock.free_blocks_count = 3 * n
    new_superblock.free_inodes_count = n

    date = coding_str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),16)
    new_superblock.mtime = date
    new_superblock.umtime = date
    new_superblock.mcount = 1

    if args.fs == '2':
        create_ext2(n, mPartition, new_superblock, date)
    elif args.fs == '3':
       
        pass

def create_ext2(n, mPartition, new_superblock, fecha):
    print(" --- Creando ext2 --- ")

    new_superblock.filesystem_type = 2
    new_superblock.bm_inode_start = mPartition[1].start + struct.calcsize(Superblock().getConst())
    new_superblock.bm_block_start = new_superblock.bm_inode_start + n
    new_superblock.inode_start = new_superblock.bm_block_start + 3 * n
    new_superblock.block_start = new_superblock.inode_start + n * struct.calcsize(Inode().getConst())

    # se crea inodo 0
    # cree un bloque de carpetas
    # se crea indo 1 para el user txt este n=indoo crea un bloque de archivos
    new_superblock.free_inodes_count -= 1
    new_superblock.free_blocks_count -= 1
    new_superblock.free_inodes_count -= 1
    new_superblock.free_blocks_count -= 1

    Crrfile = open(mPartition[2], "rb+")

    Fwrite_displacement(Crrfile, mPartition[1].start, new_superblock)

    zero = '0'
    for i in range(n):
        Fwrite_displacement_normal(Crrfile, new_superblock.bm_inode_start + i, zero)

    for i in range(3 * n):
        Fwrite_displacement_normal(Crrfile, new_superblock.bm_block_start + i, zero)

    new_Inode = Inode()
    for i in range(n):
        Fwrite_displacement(Crrfile, new_superblock.inode_start + i * struct.calcsize(Inode().getConst()), new_Inode)
 
    new_Fileblock = Fileblock()
    for i in range(3 * n):
        Fwrite_displacement(Crrfile, new_superblock.block_start + i * struct.calcsize(Fileblock().getConst()), new_Fileblock)

    Crrfile.close()
    
    





    pass
     
