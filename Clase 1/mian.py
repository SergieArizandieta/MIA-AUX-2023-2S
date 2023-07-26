import sys
import pickle
from Persona import Persona


if __name__ == "__main__":
   print("---- Classe 1 ----")
   person_obj = Persona()
   person_obj.set_nombre("Sergie")
   person_obj.set_edad(20)
   person_obj.imprimir_info()

   print(f"El tamaño de la clase Persona en memoria de ejecución es: {sys.getsizeof(person_obj)} bytes")

   data_serializada = pickle.dumps(person_obj)
   print (f"El tamaño de la clase Persona serializada es: {len(data_serializada)} bytes")

   nombre_archivo = "./Clase 1/persona.pop"
   try:
      abrir_archivo = open(nombre_archivo, "wb") # escritura binaria
      abrir_archivo.close()
      print(f"Se creo el archivo {nombre_archivo}")
   except Exception as e:
      print(f"Error al abrir el archivo {nombre_archivo}: {e}")
      sys.exit(1)

   abrir_archivo = open(nombre_archivo, "rb+") # lectura y escritura binaria
   abrir_archivo.write(data_serializada)
   abrir_archivo.close()

   abrir_archivo = open(nombre_archivo, "rb+") 
   
   person_obj_recuperado = Persona()
   person_obj_recuperado.imprimir_info()

   data_serializada_recuperada = abrir_archivo.read()
   try:
      person_obj_recuperado = pickle.loads(data_serializada_recuperada)
   except Exception as e:
      print(f"Error deserealizar {nombre_archivo}: {e}")
      sys.exit(1)

      
   person_obj_recuperado.imprimir_info()

   
   


