from Global.Global import *
from Utilities.Utilities import printConsole,printError,get_sizeB,coding_str,printSuccess
from Objects.Superblock import *
from Load.Load import *

def login(args):
    print(" --- Ejecutando login --- ")
    print("args: ", args)

    if(userSesion is not None): return printError("Ya hay una sesion iniciada")

    mPartition = None
    for partition in mounted_partitions:
        if partition[0] == args.id:
            mPartition = partition
            break

    if mPartition is None: return printError("No se encontró la particion a iniciar sesion")

    TempSuperblock = Superblock()
    Crrfile = open(mPartition[2], "rb+")
    
    Fread_displacement(Crrfile, mPartition[1].start, TempSuperblock)
    TempSuperblock.get_infomation()
   
    # crear metodo para buscar inodos por nombre

    # buscar el inodo con nombre en este caso /users.txt
   


        