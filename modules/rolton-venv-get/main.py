import os
import shutil
import sys
import zipfile

import requests


def download_and_extract_zip(url, temp_dir):
    os.makedirs(temp_dir, exist_ok=True)
    try:
        print("Скачивание ZIP-архива...")
        zip_filename = os.path.join(temp_dir, "archive.zip")
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Ошибка при скачивании: HTTP {response.status_code}")
        with open(zip_filename, "wb") as f:
            f.write(response.content)
        print("ZIP-архив успешно скачан.")
        print("Распаковка ZIP-архива...")
        with zipfile.ZipFile(zip_filename, "r") as zip_ref:
            zip_ref.extractall(temp_dir)
        print("ZIP-архив успешно распакован.")
        return temp_dir

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def find_module_folder(base_dir, module_name):
    for root, dirs, _ in os.walk(base_dir):
        for dir_name in dirs:
            if dir_name == module_name:
                return os.path.join(root, dir_name)
    return None


def copy_files_to_module_folder(module_folder, target_module_dir):
    print(f"Копирование файлов в '{target_module_dir}'...")
    for item in os.listdir(module_folder):
        source_path = os.path.join(module_folder, item)
        destination_path = os.path.join(target_module_dir, item)
        if os.path.isdir(source_path):
            shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        else:
            shutil.copy2(source_path, destination_path)
    print(f"Файлы успешно скопированы в '{target_module_dir}'.")


def main():
    url = "https://github.com/KirillMos1/RoltonVenv-packages/archive/refs/heads/master.zip"
    temp_dir = "temp_download"
    print(
        r"""
$$$$$$$\            $$\   $$\                        $$\    $$\                                      $$$$$$\             $$\     
$$  __$$\           $$ |  $$ |                       $$ |   $$ |                                    $$  __$$\            $$ |    
$$ |  $$ | $$$$$$\  $$ |$$$$$$\    $$$$$$\  $$$$$$$\ $$ |   $$ | $$$$$$\  $$$$$$$\ $$\    $$\       $$ /  \__| $$$$$$\ $$$$$$\   
$$$$$$$  |$$  __$$\ $$ |\_$$  _|  $$  __$$\ $$  __$$\\$$\  $$  |$$  __$$\ $$  __$$\\$$\  $$  |      $$ |$$$$\ $$  __$$\\_$$  _|  
$$  __$$< $$ /  $$ |$$ |  $$ |    $$ /  $$ |$$ |  $$ |\$$\$$  / $$$$$$$$ |$$ |  $$ |\$$\$$  /       $$ |\_$$ |$$$$$$$$ | $$ |    
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ | \$$$  /  $$   ____|$$ |  $$ | \$$$  /        $$ |  $$ |$$   ____| $$ |$$\ 
$$ |  $$ |\$$$$$$  |$$ |  \$$$$  |\$$$$$$  |$$ |  $$ |  \$  /   \$$$$$$$\ $$ |  $$ |  \$  /         \$$$$$$  |\$$$$$$$\  \$$$$  |
\__|  \__| \______/ \__|   \____/  \______/ \__|  \__|   \_/     \_______|\__|  \__|   \_/           \______/  \_______|  \____/ 
                                                                                                                                 
"""
    )
    module_name = input("Введите имя модуля: ").strip()
    extracted_dir = download_and_extract_zip(url, temp_dir)
    if not extracted_dir:
        return
    try:
        module_folder = find_module_folder(extracted_dir, module_name)
        if module_folder:
            script_location = os.path.dirname(os.path.abspath(sys.argv[0]))
            target_dir = os.path.join(script_location, module_name)
            os.makedirs(target_dir, exist_ok=True)
            print(f"Создана папка '{target_dir}'")
            copy_files_to_module_folder(module_folder, target_dir)
        else:
            print(f"Папка с модулем '{module_name}' не найдена.")
    finally:
        input("Нажмите любую клавишу клавиатуры для выхода...")


if __name__ == "__main__":
    main()
