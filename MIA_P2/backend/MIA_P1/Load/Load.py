from Utilities.Utilities import printConsole,printError

def Fwrite_displacement(file, displacement, obj):
    #print("Writing in: ", displacement)
    #print("Size data: ",  len(data))
    data = obj.doSerialize()
    
    file.seek(displacement)
    file.write(data)

def Fwrite_displacement_normal(file, displacement, text):
    data = text
    file.seek(displacement)
    file.write(data)

def Fread_displacement(file, displacement,obj):
    try:
        #print("Reading in: ", displacement)
        file.seek(displacement)
        data = file.read(len(obj.doSerialize()))
        #print("Size data: ",  len(data))
        obj.doDeserialize(data)
    except Exception as e:
        printError(f"Error reading object err: {e}")

def Fcreate_file(file_name):
    try:
        fileOpen = open(file_name, "wb") 
        fileOpen.close()  
        #print("=====File created successfully!======")
        return False
    except Exception as e:
        printError(f"Creacion de archivo {e}")
        return True

def Winit_size(file,size_mb):
    for i in range(size_mb):
        file.write(b'\0')



  