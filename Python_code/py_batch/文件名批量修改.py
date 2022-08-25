import os
import re


def re_fileName(path):
    fileList = os.listdir(path)
    num = 1
    for file in fileList:
        used_fileName, extension = os.path.splitext(file)
        # 202201枯季出海文件命名规则修改
        new_fileName = used_fileName.replace('n', 'N').replace('s', 'S').replace('-', '_')\
            .replace('TSP_4', 'TSP-4').replace('TSP_0', 'TSP-0')\
            .replace('TSP4', 'TSP-4').replace('TSP0', 'TSP-0')
        new_file = new_fileName + extension
        os.chdir(path)
        os.rename(file, new_file)
        print("文件%s重命名成功，新的文件名为：%s" % (file, new_file))
        num += 1


if __name__ == '__main__':
    main_path = 'E:\\河口海岸数据\\2022.01出海（南槽）\\202201南槽粒度数据\\粒度数据\\修正整合后原始数据\\'
    path_list = ['A2101\\A2101-N\\', 'A2101\\A2101-S\\',
                 'B2101\\B2101-N\\', 'B2101\\B2101-S\\',
                 'TSP0\\TSP0-N\\', 'TSP0\\TSP0-S\\',
                 'TSP4\\TSP4-N\\', 'TSP4\\TSP4-S\\']  # 目标路径
    # path = os.getcwd()  # 获取当前目录
    for path in path_list:
        re_fileName(main_path + path)



