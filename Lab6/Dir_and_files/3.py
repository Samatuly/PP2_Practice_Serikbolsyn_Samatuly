import os
dir = r'C:\Users\Orynb\Desktop\Serikbolsyn\python\Lab6\Dir_and_files\4.txt'
if(os.path.exists(dir) == True):
    dirname = os.path.dirname(dir)
    print(dirname)
    filename = os.path.basename(dir)
    print(filename)
else:
    print("Maybe, you wrote wrong")