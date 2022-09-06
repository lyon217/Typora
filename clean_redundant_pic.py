from urllib import parse as urlparse
import pandas as pd
from datetime import datetime
from dateutil.parser import parse as timestamp_parse
import time
import re
import os
import shutil


# strs = '34_%E6%A0%B7%E5%BC%8F%E8%BF%81%E7%A7%BB'
# print(urlparse.unquote(strs))
#
# # 0. 读取整个文件夹中的所有文件，并将新增文件更新更新到update_time_list中(开始对新文件进行管理)，
# #    并将它们的文件最后更新时间(final_update_time,fut)调整为当前时间，
# #    将脚本执行最终时间(final_script_time,fst)调整为NULL
# # 1. 首先读取update_time_list文件查看有哪些fut和fst不一致，说明需要对该文件所对应的图片库进行更新
# # 2. 然后逐一的对这些文件的图片库进行更新
#
# # 1.读取时间str，然后转换为time对象
# timestr = '2022-09-04 16:53:10'
# print(datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S'))
#
# # 2.时间格式化，datatime格式化
# nianyuer = datetime.now()
# timet = nianyuer.strftime('%Y-%m-%d %H:%M:%S')
# print(timet)
#
# # 3.time对象转换为str
# print(str(timet))
#
# # 检查是否文件新增或者删除
# # 检查新增就是目前读到的所有md文件-txt文件中读到的
# # 检查删除就是txt文件中读到的-目前所有md文件
# # 先考虑新增：将新增文件路径加入到txt文件中并且将fst设为NULL
# # ----------------------------------------------------------------------
# pwd = os.getcwd()
# md_files = []
# for dirname, _, filenames in os.walk(pwd):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
#         if filename.endswith('.md'):
#             md_files.append(os.path.join(dirname, filename))
# # md_files_pd就是所有md文件的路径
# md_files_pd = pd.DataFrame(md_files, columns=['filename']).reset_index(drop=True)
# # 然后删除：将删除的文件从txt文件中删除，然后将其md文件转移到指定目录中
#
#
# # 读取正在管理的md文件
# inmanage_list = pd.read_csv('update_time_list.txt')
# inmanage_total_length = inmanage_list.shape[0]
# inmanage_filenames = pd.DataFrame(every_time['filename'], columns=['filename']).reset_index(drop=True)
# # print(every_time, every_time['filename'])
#
# # 得到新增：
# md_files_pd_temp = pd.concat([md_files_pd, inmanage_filenames, inmanage_filenames])
# md_files_pd_temp.drop_duplicates(subset='filename', keep=False)
# md_files_pd_added = pd.concat([md_files_pd, md_files_pd_temp])
#
# # 得到删除
#
#
# need_script_lists = inmanagee_list[inmanage_list['fut'] != inmanage_list['fst']]
# # for i in every_time['filename']:
# #     print(i)
#
# # def yield_list(ev_t, ev_t_len):
# #     for i in range(ev_t_len):
# #         # 如果1 2列的时间（戳）差距过大，则认为是文件更新了，需要同步文件库
# #         if ev_t[2] != 'NULL' and ev_t[0] != ev_t[1]:
# #             yield ev_t[0]
# #
# #
# # for i in yield_list(every_time, len(every_time)):
# #     print(i)
#
# row = """
# # test1
#
# ## test2
#
# ### test3
#
# #### test4
#
# ##### test5
#
# asdfad
#
# ![image-20220904171751023](Test01.assets/image-20220904171751023.png)
#
# ### sed
#
# - sdfdf
#
# ![image-20220904171853506](Test01.assets/image-20220904171853506.png)"""
#
# text1 = '![image-20220904171751023](Test01.assets/image-20220904171751023.png)'
# reg = r"!\[image-\d+\]\(.*\/image-(\d+\.\w+)\)"
# reintr = re.finditer(reg, row)
# for i in reintr:
#     print(i.group(1))
#
# print(md_files_pd)
#
# everry_time_resetidx = pd.concat([everry_time_resetidx, md_files_pd, md_files_pd])
# print(everry_time_resetidx.drop_duplicates(subset=['filename'], keep=False))


def get_md_filepath():
    pwd = os.getcwd()
    md_file_path = []
    for dirname, _, filenames in os.walk(pwd):
        for filename in filenames:
            # print(os.path.join(dirname, filename))
            if filename.endswith('.md'):
                md_file_path.append(os.path.join(dirname, filename))
    return md_file_path


def get_imagespath_from_filepath(assets_filepath):
    file_names = []
    for files in os.listdir(assets_filepath):
        if os.path.splitext(files)[1] in ['.jpg', '.png', '.jpeg', '.gif']:
            file_names.append(files)
    return file_names


def update_images_from_md_filepath(md_files):
    for i in range(len(md_files)):
        current_mdfile_name = md_files[i]
        current_mdfile_path = current_mdfile_name.replace('.md', '.assets', 1) + '/'
        images = []
        # print(current_mdfile_name)
        with open(current_mdfile_name, 'r') as f:
            contents = f.read()
        reg = r"!\[image-\d+\]\(.*\/(image-\d+\.\w+)\)"
        md_image_names = re.findall(reg, contents)
        print(md_image_names)
        assets_image_names = get_imagespath_from_filepath(current_mdfile_name.replace('.md', '.assets', 1))
        print(assets_image_names)
        diff = list(set(assets_image_names).difference(set(md_image_names)))
        print(diff)
        for name in diff:
            # print(current_mdfile_path + '/' + name)
            shutil.move(current_mdfile_path + name, './duoyu')


update_images_from_md_filepath(get_md_filepath())
