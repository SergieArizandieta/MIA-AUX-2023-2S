class Persona:
   def __init__(self):
      self.nombre = "~" * 15 # 15 caracteres -> 15 bytes
      self.edad = -1 # numero 4 bytes total = 19 bytes

   def set_nombre(self, nombre):
      self.nombre = nombre[:15].ljust(16, ' ')

   def set_edad(self, edad):
      if edad > 0:
         self.edad = edad

   def imprimir_info(self):
      print("Nombre: ", self.nombre)
      print("Edad: ", self.edad)