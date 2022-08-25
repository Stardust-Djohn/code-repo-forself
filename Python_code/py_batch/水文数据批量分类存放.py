"""
Time：20220523
Author:董坚
v1.1
    指定一级文件目录的路径（存放各站点数据的根目录）
    运行后遍历其一级目录结构（各类站点数据），检查并创建二级目录结构（各年月文件夹）
    查找二级目录中的数据文件，根据数据文件名正则表达结果，分类存放于二级目录结构中（即三级结构中）
"""
import os
import re
import shutil


def data_batch(pth):
    cur_path = pth
    # cur_path = os.getcwd()  # 一级目录， 可以修改成指定的路径
    # 当前目录迭代器
    with os.scandir(cur_path) as entries:
        # 遍历一级目录
        for entry in entries:
            # 如果是文件夹（路径），则进入，来到二级目录
            if entry.is_dir():
                log_1 = os.path.join(cur_path, entry.name)  # 二级目录绝对路径
                # 过滤，只取二级目录下的文件
                files_name = filter(lambda p: os.path.isfile(os.path.join(log_1, p)), os.listdir(log_1))
                for op_file in files_name:
                    # 提取文件的年月日信息
                    file_time_info = get_file_str(op_file)
                    # 如果file_time_info列表不为空，则执行移动文件操作
                    if file_time_info:
                        file_check_mv(log_1, file_time_info, op_file)
                print("目录执行完毕：", log_1)


# 匹配提取出文件的年、月、日
def get_file_str(file_name_str):
    # 正则匹配规则：YYYY-MM-DD,中间连接符号任意：_-
    search_obj = re.search(r"[0-9]{4}.[0-9]{2}.[0-9]{2}", file_name_str)
    time_list = []
    # 如果正则表达式匹配到字符串
    if search_obj:
        time_str = search_obj.group()
        time_list = re.split('-|_', time_str)  # 中间连接符号，可视情况再添加
    # 如果正则表达式匹配失败，则返回空列表
    return time_list


# 判断并移动文件至指定的文件夹
# 输入参数依次为待操作的根目录、文件日期信息列表、当前处理文件的文件名
def file_check_mv(cur_path, file_info, op_file):
    aim_dir = file_info[0] + "." + file_info[1]  # 目标文件夹名
    aim_path = os.path.join(cur_path, aim_dir)  # 目标文件夹绝对路径
    # 判断对应的文件夹是否被创建，如果没有则创建
    if not os.path.exists(aim_path):
        os.mkdir(aim_path)
    # 将文件移动到指定的文件夹中，如果同名文件存在则替换
    shutil.move(os.path.join(cur_path, op_file), os.path.join(aim_path, op_file))


if __name__ == "__main__":
    data_batch("E:\\河口海岸数据\\长江主要水文测站潮位数据")
