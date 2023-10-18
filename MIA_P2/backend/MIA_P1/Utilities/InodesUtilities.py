from Load.Load import *
from Objects.Inode import *
from Objects.Folderblock import *
from Objects.Fileblock import *

def initSearch(path,Crrfile,TempSuperblock):
    print("path",path)
    StepsPath = path.split("/")
    StepsPath.pop(0)
    
    if(len(StepsPath)==0):
        return 0
    
    print("StepsPath",StepsPath)
    Inode0 = Inode()
    Fread_displacement(Crrfile, TempSuperblock.inode_start, Inode0)
    return SarchInodeByPath(StepsPath,Inode0,Crrfile,TempSuperblock)

def SarchInodeByPath(StepsPath,Inode,Crrfile,TempSuperblock):
    index = 0 
    SearchedName = StepsPath.pop(0)
       
    for i in Inode.i_block:
        if(i != -1):
            if(index < 13):
                #CASO DIRECTOS
                crr_Folderblock = Folderblock()
                Fread_displacement(Crrfile, TempSuperblock.block_start + i * TempSuperblock.block_size, crr_Folderblock)

                for content in crr_Folderblock.Content:
                    if(content.b_inodo != -1):
                        if(content.b_name.decode() == SearchedName):
                            if(len(StepsPath)==0):
                                return content.b_inodo
                            else:
                                NextInode = Inode()
                                Fread_displacement(Crrfile, TempSuperblock.inode_start + content.b_inodo * TempSuperblock.inode_size, NextInode)
                                return SarchInodeByPath(StepsPath,NextInode,Crrfile)
    
            else:
                #CASO INDIRECTOS 
                pass  
        index+=1


    
def getInodeFileData(Inode,Crrfile,TempSuperblock):
    index = 0
    content = ""
    for i in Inode.i_block:
        if(i != -1):
            if(index < 13):
                #CASO DIRECTOS
                crr_Fileblock = Fileblock()
                Fread_displacement(Crrfile, TempSuperblock.block_start + i * TempSuperblock.block_size, crr_Fileblock)

                content += crr_Fileblock.b_content.decode()
    
            else:
                #CASO INDIRECTOS 
                pass  
        index+=1

    return content


        