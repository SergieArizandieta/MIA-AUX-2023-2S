import struct
import math
import datetime
from Load.Load import *
from Utilities.Utilities import printConsole,printError,get_sizeB,coding_str,printSuccess
from Global.Global import *
from Objects.Inode import *
from Objects.Fileblock import *
from Objects.Superblock import *
from Objects.Content import *
from Objects.Folderblock import *

def mkfs(args):
    print(" --- Ejecutando mkfs --- ")
    print("args: ", args)

    mPartition = None
    for partition in mounted_partitions:
        if partition[0] == args.id:
            mPartition = partition
            break

    if mPartition is None: return "La particion no esta montada"

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
        return create_ext2(n, mPartition, new_superblock, date)
    elif args.fs == '3':
        pass

def create_ext2(n, mPartition, new_superblock, date):
    print(" --- Creando ext2 --- ")
    #crear la carpeta raiz "/" -> cree inodo 0
    #crear el archivo "user.txt" en "/" -> cree inodo 1

    #cree carpeta de bloque (bloque0) -> inodo 1
    #crear archivo de bloque (bloque1) "1,G,root\n1,U,root,root,123\n"

    # inodo 0 -> bloque0 -> bloque1 -> bloque1

    new_superblock.filesystem_type = 2
    new_superblock.bm_inode_start = mPartition[1].start + struct.calcsize(Superblock().getConst())
    new_superblock.bm_block_start = new_superblock.bm_inode_start + n
    new_superblock.inode_start = new_superblock.bm_block_start + 3 * n
    new_superblock.block_start = new_superblock.inode_start + n * struct.calcsize(Inode().getConst())

    new_superblock.inode_size = struct.calcsize(Inode().getConst())
    new_superblock.block_size = struct.calcsize(Fileblock().getConst())

    # se crea inodo 0
    # cree un bloque de carpetas
    # se crea indo 1 para el user txt este n=indoo crea un bloque de archivos
    new_superblock.free_inodes_count -= 1
    new_superblock.free_blocks_count -= 1
    new_superblock.free_inodes_count -= 1
    new_superblock.free_blocks_count -= 1

    Crrfile = open(mPartition[2], "rb+")

    zero = b'\0'
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


    Inode0 = Inode()
    Inode0.i_uid = 1
    Inode0.i_gid = 1
    Inode0.i_size = 0
    Inode0.i_atime = date
    Inode0.i_ctime = date
    Inode0.i_mtime = date
    Inode0.i_type = b'\0'
    Inode0.i_perm = b'664'
    Inode0.i_block[0] = 0

    # . | 0
    # .. | 0
    # user.txt | 1
    #

    # contenido = Content()
    # contenido.get_infomation()

    Folderblock0 = Folderblock()
    Folderblock0.Content[0].b_inodo = 0
    Folderblock0.Content[0].b_name = b'.'
    Folderblock0.Content[1].b_inodo = 0
    Folderblock0.Content[1].b_name = b'..'
    Folderblock0.Content[2].b_inodo = 1
    Folderblock0.Content[2].b_name = b'user.txt'

    
    Inode1 = Inode()
    Inode1.i_uid = 1
    Inode1.i_gid = 1
    Inode1.i_size = struct.calcsize(Fileblock().getConst())
    Inode1.i_atime = date
    Inode1.i_ctime = date
    Inode1.i_mtime = date
    Inode1.i_type = b'1'
    Inode1.i_perm = b'664'
    Inode1.i_block[0] = 1


    data_usertxt = '1,G,root\n1,U,root,root,123\n'
    Fileblock1 = Fileblock()
    Fileblock1.b_content = coding_str(data_usertxt,64)


    Fwrite_displacement(Crrfile, mPartition[1].start, new_superblock)
    
    # fill bitmap  inodes
    Fwrite_displacement_normal(Crrfile, new_superblock.bm_inode_start, b'\1')
    Fwrite_displacement_normal(Crrfile, new_superblock.bm_inode_start+1, b'\1')
    
    # fill bm blocks
    Fwrite_displacement_normal(Crrfile, new_superblock.bm_block_start, b'\1')
    Fwrite_displacement_normal(Crrfile, new_superblock.bm_block_start+1, b'\1')

    # fill inodes  
    Fwrite_displacement(Crrfile, new_superblock.inode_start, Inode0)
    Fwrite_displacement(Crrfile, new_superblock.inode_start+1*struct.calcsize(Inode().getConst()), Inode1)

    # fill blocks
    Fwrite_displacement(Crrfile, new_superblock.block_start, Folderblock0)
    Fwrite_displacement(Crrfile, new_superblock.block_start+1*struct.calcsize(Fileblock().getConst()), Fileblock1)

    Crrfile.close()

    printSuccess("Se creo el sistema de archivos ext2")
    return "Se creo el sistema de archivos ext2"
    
