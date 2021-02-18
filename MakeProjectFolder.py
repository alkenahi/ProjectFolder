#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import os.path


# In[6]:


def main():
    project_name = input("Type name of the projects: ")
    
    currentDir = os.getcwd()
    rootFolder = os.path.join(currentDir, project_name)
    try:
        futureDir = os.path.join(currentDir, project_name)
        if os.path.exists(futureDir) == False:
            makeFolder = os.mkdir(rootFolder)
            makeSubFold1 = os.mkdir(os.path.join(rootFolder,"data"))
            makeSubFold2 = os.mkdir(os.path.join(rootFolder,"notebooks"))
            makeSubFold3 = os.mkdir(os.path.join(rootFolder,"src"))
            print("Project Folder {0} Has Been Create For You".format(project_name))
        elif os.path.exists(futureDir) == True:
            print("Project Folder Already Exists")
            alternative_name = input("Type name of the projects: ")
            alterrootFolder = os.path.join(currentDir, alternative_name)
            makeFolder = os.mkdir(alterrootFolder)
            makeSubFold1 = os.mkdir(os.path.join(alterrootFolder,"data"))
            makeSubFold2 = os.mkdir(os.path.join(alterrootFolder,"notebooks"))
            makeSubFold3 = os.mkdir(os.path.join(alterrootFolder,"src"))
            print("Project Folder {0} Has Been Create For You".format(alternative_name))
        else:
            print("Please Rerun this function")
    except OSError:
        print("Failed")
    
if __name__ == '__main__':
    main()


# In[ ]:




