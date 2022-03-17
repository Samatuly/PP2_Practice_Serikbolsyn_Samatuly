import os
path = r"C:\Users\Orynb\Desktop\Serikbolsyn\python\Lab6\Dir_and_files\Folder1"
dir = os.listdir(path)
for x in dir:
    print(x)
    print('Exist:', os.access(x, os.F_OK))
    print('Readable:', os.access(x, os.R_OK))
    print('Writable:', os.access(x, os.W_OK))
    print('Executable:', os.access(x, os.X_OK))
    print()