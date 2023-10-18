from Global.Global import *
from Utilities.Utilities import printConsole,printError,get_sizeB,coding_str,printSuccess
from Objects.Superblock import *
from Load.Load import *
from Utilities.InodesUtilities import *

def login(args):
    print(" --- Ejecutando login --- ")
    print("args: ", args)

    if(len(userSesion)!=0): return "Ya hay una sesion iniciada"

    mPartition = None
    for partition in mounted_partitions:
        if partition[0] == args.id:
            mPartition = partition
            break

    if mPartition is None: return "No se encontró la particion a iniciar sesion"

    TempSuperblock = Superblock()
    Crrfile = open(mPartition[2], "rb+")
    
    Fread_displacement(Crrfile, mPartition[1].start, TempSuperblock)

    IndexInode = initSearch("/user.txt",Crrfile,TempSuperblock)

    InodeFIle = Inode()
    Fread_displacement(Crrfile, TempSuperblock.inode_start + IndexInode * TempSuperblock.inode_size, InodeFIle)

    data = getInodeFileData(InodeFIle,Crrfile,TempSuperblock)
    splitData = data.split("\n")
    splitData.pop()

    for line in splitData:
        info = line.split(",")
        if info[1] == "U":
            if info[2] == args.user:
                print(userSesion)
                userSesion.append(info)
                pass
   
    print("=============",userSesion)
    userSesion.pop(0)
    print("=============",userSesion)
    Crrfile.close()
    return "Sesion iniciada exitosamente"
   


        