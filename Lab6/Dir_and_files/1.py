import os
path = r"C:\Users\Orynb\Desktop\Serikbolsyn\python\Lab6\Dir_and_files\Folder1"
dir_file_list = os.listdir(path)
print("All files and directories: ")
print(dir_file_list)
print("All directories: ")
for x in os.listdir(path):
    if os.path.isfile(os.path.join(path, x)):
        print(x)
print("All files: ")
for y in os.listdir(path):
    if not os.path.isfile(os.path.join(path, y)):
        print(y)