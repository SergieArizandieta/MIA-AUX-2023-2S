def readData(data):
   data = data.replace('\r', '')
   array = data.split('\n')
   array = [elemento for elemento in array if elemento != '']
   respose = TempAnalizer(array) 
   return respose

def TempAnalizer(data): # en su analizador recorrer 
   response = ""
   contador = 1 #esto solo es para diferenciar la salida, no es necesarioa
   for command in data:
      response += AnalizerP1( command) + " : " + str(contador) + "\n" # llamar aqui al analizador de su proyecto 1 y concatenar las salidas de cada comando 
      contador += 1
   return response

def AnalizerP1(command):
   return "Resultado de ejecutar el X comando"