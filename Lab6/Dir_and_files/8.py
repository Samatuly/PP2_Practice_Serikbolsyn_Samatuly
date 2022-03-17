import os
file = "file_to_delete.txt"
location = r"C:\Users\Orynb\Desktop\Serikbolsyn\python\Lab6\Dir_and_files"
path = os.path.join(location, file) 
os.remove(path)