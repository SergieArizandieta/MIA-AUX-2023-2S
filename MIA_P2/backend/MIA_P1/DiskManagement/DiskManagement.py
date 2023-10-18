import subprocess
import os
from Load.Load import *
from Objects.MBR import *
from Utilities.Utilities import printConsole,printError,get_sizeB
from Global.Global import mounted_partitions

def mount(args):
   print(" --- Ejecutando mount --- ")
   print("args: ", args)
   crr_mbr = MBR()
   Crrfile = open(args.path, "rb+")
   Fread_displacement(Crrfile,0,crr_mbr)
   
   crr_partition = Partition()
   for partition in crr_mbr.partitions:
      if partition.size != -1:
         if partition.name.decode() == args.name:
            crr_partition = partition

   if crr_partition.size != -1:
      # F = XX +  NUM PARTITION + NOMBRE DISCO donde XX es el numero de carnet
      nombre_archivo = os.path.splitext(os.path.basename(args.path))[0]
      index = 1
      for data in mounted_partitions:
         if data[1] == args.path:
            index = int(data[0][2:3]) + 1

      id = "19" + str(index) + nombre_archivo
      print("id:",id)
      temp = [id,crr_partition ,args.path]
      mounted_partitions.append(temp)
   else:
      printError("La particion no existe")
      return "La particion no existe"
   Crrfile.close()
   return "Particion montada exitosamente" + " id: " + str(id)

def fdisk(args):
   print(" --- Ejecutando fdisk --- ")
   print("args: ", args)

   crr_mbr = MBR()
   Crrfile = open(args.path, "rb+")
   Fread_displacement(Crrfile,0,crr_mbr)

   if args.size is not None: # creting partition
      start = len(MBR().doSerialize())
      index = 0
      
      for partition in crr_mbr.partitions:
         if partition.size != -1:
            start = partition.start + partition.size
            index += 1
         else:
            break

      size_bytes = get_sizeB(args.size,args.unit)

      new_partition = Partition()
      new_partition.set_infomation('1',args.type,args.fit,start,size_bytes,args.name)
      crr_mbr.partitions[index] = new_partition
      Fwrite_displacement(Crrfile,0,crr_mbr)
      Crrfile.close()
      return "Particion creada exitosamente"
 
def mkdisk(args):
   print(" --- Ejecutando mkdisk --- ")
   print("args: ", args)
   print("args.size: ", args.size)
   print("args.path: ", args.path)
   print("args.fit: ", args.fit)
   print("args.unit: ", args.unit)

   size_bytes = get_sizeB(args.size,args.unit)

   #folder_path = os.path.dirname(args.path)
   #subprocess.run(f"mkdir -p {folder_path}", shell=True)

   if (Fcreate_file(args.path)): return

   Crrfile = open(args.path, "rb+")

   #Winit_size(Crrfile,size_bytes)

   NewMBR = MBR()
   NewMBR.set_infomation(size_bytes,args.fit)
   Fwrite_displacement(Crrfile,0,NewMBR)
   Crrfile.close()
   return "Disco creado exitosamente"
   

   


  
