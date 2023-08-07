from Persona import Persona
from load import Aescritura_desplazado,Alectura_desplazado

if __name__ == "__main__":
   print("---- Classe 2 ----")
   person_obj = Persona()
   person_obj.set_nombre("Sergie")
   person_obj.set_edad(20)
   person_obj.imprimir_info()

   nombre_archivo = "./Clase 2/example_file2.sdk"

   try:
      abrirArvhivo = open(nombre_archivo,"wb") # escritura binaria
      abrirArvhivo.close()
      print(f"=== Se creo el archivo {nombre_archivo} ===")
   except Exception as e:
      print(f"Error al abrir el archivo {nombre_archivo}: {e}")

   desplazamiento = 0
   archivo = open(nombre_archivo,"rb+") # escritura y lectura binaria (no se puede leer un archivo que no existe)

   Aescritura_desplazado(archivo,desplazamiento,person_obj)

   person_obj2 = Persona()
   person_obj2 = Alectura_desplazado(archivo,desplazamiento,person_obj2)
   person_obj2.imprimir_info()
   
   archivo.close()
   
