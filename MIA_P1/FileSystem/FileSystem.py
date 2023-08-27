import subprocess
import os
from Load.Load import *
from Objects.MBR import *
from Utilities.Utilities import printConsole,printError,get_sizeB
from Global.Global import mounted_partitions

def mkfs(args):
    print(" --- Ejecutando mkfs --- ")
    print("args: ", args)

    # bucar id de particion montada

    # numerador = (partition_montada.size - sizeof(Structs::Superblock)
    # denrominador base = (4 + sizeof(Structs::Inodes) + 3 * sizeof(Structs::Fileblock))
    # temp = "2" ? 0 : sizeof(Structs::Journaling)
    # denrominador = base + temp
    # n = floor(numerador / denrominador)

    if args.fs == 2:
        # caclulo sin journaling
        
        # crear super bloque
        # crear el archivo inicial
        pass
    elif args.fs == 3:
        # caclulo con journaling

        # crear super bloque
        # crear el journaling
        # crear el archivo inicial
        pass
     
