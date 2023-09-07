import re
import argparse

import shlex
from Utilities.Utilities import printConsole,printError
from DiskManagement.DiskManagement import *
from FileSystem.FileSystem import *
from User.User import *


# [
#       "mkdisk -size=20 -unit=m -path=/home/serchiboi/aMIA/Disco1.dsk",
#       "fdisk -type=P -unit=K -name=part1 -size=7680 -path=/home/serchiboi/aMIA/Disco1.dsk"
#       ]

# [
#       "mount -path=/home/serchiboi/aMIA/Disco1.dsk -name=part1",
#       'mkfs -type=full -id=191Disco1'
#       ]

def Commands():
   printConsole(" ---- Bienvenido al Sistema de Archivos de  - 202000119 ---- ")
   arr = [
      "mount -path=/home/serchiboi/aMIA/Disco1.dsk -name=part1",
      'mkfs -type=full -id=191Disco1',
      'login -user=root -pass=123 -id=191Disco1'
      ]
   index = 0
   while True:
      command = input('\033[36m<<System>> - Ingrese un comando -\n\033[00m')
      command = re.sub(r"[#][^\n]*", "", command)

      command = arr[index]
      if command == "": continue
      elif re.search("[e|E][x|X][i|I][t|T]", command): break
      AnalyzeType(command)
      index += 1
   printConsole("... Saliendo del programa ...")
   

def AnalyzeType(entry):
   try:
      entry= entry.lower()
      printConsole("Analizando comando: " + entry)
      split_args = shlex.split(entry)
      command = split_args.pop(0)
      if(command == "mkdisk"):
         print(" ------ Se dectecto mkdisk ------ ")
         fn_mkdisk(split_args)
         print(" ------ Termino mkdisk ------ ")
      elif(command == "fdisk"):
         print(" ------ Se dectecto fdisk ------ ")
         fn_fdisk(split_args)
         print(" ------ Termino fdisk ------ ")
      elif(command == "mount"):
         print(" ------ Se dectecto mount ------ ")
         fn_mount(split_args)
         print(" ------ Termino mount ------ ")
      elif(command == "mkfs"):
         print(" ------ Se dectecto mkfs ------ ")
         fn_mkfs(split_args)
         print(" ------ Termino mkfs ------ ")
      elif(command == "login"):
         print(" ------ Se dectecto login ------ ")
         fn_login(split_args)
         print(" ------ Termino login ------ ")
   except Exception as e: pass

def fn_login(split_args):
   try:
      parser = argparse.ArgumentParser(description="Parámetros")
      parser.add_argument("-user", required=True)
      parser.add_argument("-pass", required=True)
      parser.add_argument("-id", required=True)
      args = parser.parse_args(split_args)

      login(args)

   except SystemExit: printError("Análisis de argumentos")
   except Exception as e: printError(str(e))

def fn_mkfs(split_args):
   try:
      parser = argparse.ArgumentParser(description="Parámetros")
      parser.add_argument("-id", required=True)
      parser.add_argument("-type")
      parser.add_argument("-fs", default='2')
      args = parser.parse_args(split_args)
      args.fs = args.fs[:1]

      mkfs(args)

   except SystemExit: printError("Análisis de argumentos")
   except Exception as e: printError(str(e))


def fn_mount(split_args):
   try:
      parser = argparse.ArgumentParser(description="Parámetros")
      parser.add_argument("-path", required=True)
      parser.add_argument("-name", required=True)
      args = parser.parse_args(split_args)

      mount(args)

   except SystemExit: printError("Análisis de argumentos")
   except Exception as e: printError(str(e))


def fn_fdisk(split_args):
   try:
      parser = argparse.ArgumentParser(description="Parámetros")
      parser.add_argument("-size", type=int)
      parser.add_argument("-path", required=True)
      parser.add_argument("-name", required=True)
      parser.add_argument("-unit", default='k')
      parser.add_argument("-type", default='p')
      parser.add_argument("-fit", default='w')
      parser.add_argument("-delete")
      parser.add_argument("-add")
      args = parser.parse_args(split_args)

      args.fit = args.fit[:1]

      if args.unit is not None:
         if args.unit not in ["k","m","b"]: raise Exception("El parametro unit solo puede ser k o m o b")


      fdisk(args)

   except SystemExit: printError("Análisis de argumentos")
   except Exception as e: printError(str(e))


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

  

      
      

