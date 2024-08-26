import os
import shutil


def copy_files_with_suffix(source_folder, target_folder, suffix='更新.xlsx'):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    for file_name in os.listdir(source_folder):
        if file_name.endswith(suffix):
            source_file_path = os.path.join(source_folder, file_name)
            target_file_path = os.path.join(target_folder, file_name)
            shutil.copy(source_file_path, target_file_path)
    print("文件复制完成！")
