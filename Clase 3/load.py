import pickle
import ctypes

def Fwrite_displacement(file, displacement, data):
    file.seek(displacement)
    serialized_data = pickle.dumps(data)
    file.write(serialized_data)
    #Getting the size of the object in bytes of serialized data that contain the all data necesari to unserialized
    print(f"Size of serialized data: {len(serialized_data)} bytes")
    #print(f"data: {serialized_data}")

def Fread_displacement(file, displacement,data):
    file.seek(displacement)
    serialized_data = file.read()
    #print(f"data: {serialized_data}")
    try:
        return pickle.loads(serialized_data) 
    except Exception as e:
        print(f"Error reading object: {e}")
        return data
    
def Fcreate_file(file_name):
    try:
        fileOpen = open(file_name, "wb")  # Open the file in write mode
        print("=====File created successfully!======")
        return fileOpen
    except Exception as e:
        print(f"Error creating the file: {e}")

def Winit_size(file,size_mb):
    #mb to bytes -> mb * 1024kb/1mb * 1024b/1kb -> mb * 1024 * 1024
    buffer = b'\0'*1024
    times_to_write =  size_mb  * 1024 
    print(f"Expected File Size: {len(buffer)*times_to_write} bytes")

    for i in range(times_to_write):
        file.write(buffer)

    print("=====Size apply successfully!======")


  