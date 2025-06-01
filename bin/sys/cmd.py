import os, subprocess
from ..utils.calc import calculate
from ..utils.color_checker import checker_color

def runner(cmd, workdir, userdir, username):
    cmd = cmd.split()
    if cmd:
        if cmd[0] == "help":
            if len(cmd) == 1:
                print("help - это сообщение\nmodule-run <модуль> - запуск модуля\nutil-run <утилита> <параметр> - запуск утилиты\ndir - отображение текущей папки")
            else:
                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
        elif cmd[0] == "exit":
            if len(cmd) == 1:
                return
            else:
                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
        elif cmd[0] == "dir":
            try:
                print(f"| [{workdir}]")
                for filer in os.listdir(workdir):
                    print(f"|-- {filer}")
            except Exception as e:
                print(f"BUILTIN_ERROR: {e}")
        elif cmd[0] == "util-run":
            if len(cmd) > 2:
                if cmd[1] == "calc":
                    print(calculate(cmd[2]))
                elif cmd[1] == "color-checker":
                    checker_color()
                else:
                    print("UTIL_UWNKOWN_ERROR (0x00000031): неизвестная утилита")
            else:
                print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
        elif cmd[0] == "module-run":
            if len(cmd) == 2:
                modules_dir = os.path.join(os.getcwd(), "modules")
                with os.scandir(modules_dir) as data_fld:
                    flag = False
                    for entry in data_fld:
                        if entry.is_dir() and entry.name == cmd[1]:
                            module = os.path.join(modules_dir, entry.name) + "main.exe"
                            flag = True
                            os.system("cls")
                            try: subprocess.call([f"{module}", username])
                            except Exception as e:
                                print("MODULE_CORRUPTED_ERROR (0x00000043): модуль поврежден. Переустановите его!")
                                print(f"BUILTIN_ERROR: {e}")
                            else: os.system("cls")
                        else:
                            continue
                    if flag:
                        pass
                    else:
                        print("MODULE_UWNKOWN_ERROR (0x00000041): неизвестная модуль. Скачайте его с помощью rolton-venv-get")
            else:
                print("MODULE_NEED_ARGUMENT_ERROR (0x00000033): ожидалось 2 аргумента")
        elif cmd[0] == "cd":
            # заглушка
            folders = cmd[1].split("/")
            print(folders)
        elif cmd[0] == "new":
            if len(cmd) in (1, 2,):
                print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
            else:
                if cmd[1] == "file":
                    open(os.path.join(workdir, cmd[2]), "x").close()
                else:
                    print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
        elif cmd[0] == "version":
            if len(cmd) == 1:
                vers_file = open(os.path.join(os.getcwd(), "bin", "sys", "data", "version.txt"), "r")
                print(f"Версия RoltonVenv: {vers_file.read()}")
                vers_file.close()
            else:
                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
        else:
            print(f"COMMAND_UWNKOWN_ERROR (0x00000021): неизвестная команда '{cmd[0]}'. Для запуска модуля используйте 'module-run', для запуска утилиты 'util-run'")
    else:
        return
