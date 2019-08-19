import os
import multiprocessing

def copy_file(folder_name,old_folder,new_folder):
    old_file = open(old_folder + "/" + folder_name,"rb")
    content = old_file.read()
    old_file.close()
    new_file = open(new_folder + "/" + folder_name,"wb")
    new_file.write(content)
    new_file.close()


def main():
    """
    多进程文件拷贝
    1. 用户输入拷贝的文件夹名称
    2. 获取文件夹中的文件名
    3. 创建新的文件夹
    4. 创建进程池
    5. 拷贝文件
    """

    old_folder = input("请输入需要拷贝的文件夹：")
    folder_names =  os.listdir(old_folder)
    new_folder = "new"+ old_folder
    os.mkdir(new_folder)
    po = multiprocessing.Pool(4)
    for folder_name in folder_names:
        po.apply_async(copy_file,args=(folder_name,old_folder,new_folder,))
    po.close()
    po.join()
if __name__ == '__main__':
    main()