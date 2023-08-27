import re
import argparse
import shlex
from Utilities.Utilities import printConsole,printError
from DiskManagement.DiskManagement import *

#mkdisk -size=5 -unit=M -"path=/home/user/Dis co1.dsk" -fit=bf -name=Disco1
#mkdisk -size=5 -unit=M -path=home/serchiboi/aMIA/Disco4.dsk -fit=bf 
#mkdisk -size=5 -path="/home/user/Dis co1.dsk"

def Commands():
   printConsole(" ---- Bienvenido al Sistema de Archivos de  - 202000119 ---- ")
   while True:
      command = input('\033[36m<<System>> - Ingrese un comando -\n\033[00m').lower()
      command = re.sub(r"[#][^\n]*", "", command)
      command = 'mkdisk -size=5 -path=/home/serchiboi/aMIA/Disco4.dsk -fit=bf -unit=m'
      if command == "": continue
      elif re.search("[e|E][x|X][i|I][t|T]", command): break
      AnalyzeType(command)
   printConsole("... Saliendo del programa ...")
   

def AnalyzeType(entry):
   try:
      printConsole("Analizando comando: " + entry)
      split_args = shlex.split(entry)
      if(split_args.pop(0) == "mkdisk"):
         print(" ------ Se dectecto mkdisk ------ ")
         fn_mkdisk(split_args)
         print(" ------ Termino mkdisk ------ ")
   except Exception as e: pass
   
def fn_mkdisk(split_args):
   try:
      parser = argparse.ArgumentParser(description="Parámetros")
      parser.add_argument("-size", type=int, required=True)
      parser.add_argument("-path", required=True)
      parser.add_argument("-fit", default='f')
      parser.add_argument("-unit", default='m')
      args = parser.parse_args(split_args)

      args.fit = args.fit[:1]

      if args.fit not in ["b","f","w"]: raise Exception("El parametro fit solo puede ser b, f o w")
      if args.unit not in ["k","m"]: raise Exception("El parametro unit solo puede ser k o m")
      
      if re.search("[.][d|D][s|S][k|K]",args.path) is None: raise Exception("La extensión del archivo debe ser .dsk")

      mkdisk(args)

   except SystemExit: printError("Análisis de argumentos")
   except Exception as e: printError(str(e))

  

      
      

