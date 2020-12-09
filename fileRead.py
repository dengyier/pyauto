import os

# root_dir为要读取文件的根目录
root_dir = "/Users/yaoyao/Learn/dyData/UiFile"
# 读取批量文件后要写入的文件
with open("test.txt", "w") as test:

    # 依次读取根目录下的每一个文件
    for file in os.listdir(root_dir):
        file_name = root_dir + "/" + file
        filein = open(file_name, "r")
        # 按行读取每个文件中的内容
        for line in filein:
            test.write(line.rstrip("\n"))
        test.write("\n")
        filein.close()


