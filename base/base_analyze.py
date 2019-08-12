# import yaml
# 原始没有优化的方法
# def analyze_data(file_name, key_name):
#     # contact_data
#     file_path = "./data/" + file_name + ".yaml"
#     with open(file_path, "r", encoding='utf-8') as f:
#
#         data = yaml.load(f)
#         data_list = list()
#         for i in data[key_name].values():
#             data_list.append(list(i.values()))
#         return data_list

# 解决字典无序列表问题--优先使用
# def analyze_data(file_name, key_name):
#     # contact_data
#     file_path = "./data/" + file_name + ".yaml"
#     with open(file_path, "r", encoding='utf-8') as f:
#
#         data = yaml.load(f)
#         data_list = list()
#         for i in data[key_name].values():
#             data_list.append(i)
#         return data_list

import os
import yaml
def analyze_data(file_name, key):
    """
    根据文件解析数据
    :param file_name: 数据文件名
    :param key: 数据的key
    :return:
    """
    with open(r".%sdata%s%s.yaml" % (os.sep, os.sep, file_name), "r", encoding='utf-8') as f:
        data_list = list()
        data_list.extend(yaml.load(f)[key].values())
        return data_list

# 字典 -
# [[],[],[]]