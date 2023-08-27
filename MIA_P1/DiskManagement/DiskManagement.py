import subprocess
import os
from Load.Load import *
from Objects.MBR import *
from Utilities.Utilities import printConsole,printError,get_sizeB


def mkdisk(args):
   print(" --- Ejecutando mkdisk --- ")
   print("args: ", args)
   print("args.size: ", args.size)
   print("args.path: ", args.path)
   print("args.fit: ", args.fit)
   print("args.unit: ", args.unit)

   size_bytes = get_sizeB(args.size,args.unit)

   folder_path = os.path.dirname(args.path)
   subprocess.run(f"mkdir -p {folder_path}", shell=True)

   if (Fcreate_file(args.path)): return

   Crrfile = open(args.path, "rb+")

   Winit_size(Crrfile,size_bytes)

   NewMBR = MBR()
   NewMBR.set_infomation(size_bytes,args.fit)
   Fwrite_displacement(Crrfile,0,NewMBR)

   


  
