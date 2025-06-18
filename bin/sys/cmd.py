import os, subprocess, datetime, platform
from ..utils.calc import calculate
from ..utils.color_checker import checker_color
from .users_manager import registr, user_data_get

logger = open(os.path.join(os.getcwd(), "bin", "sys", "data", "log.txt"), "a+")

def runner(cmd, workdir, userdir, username, root = 0):
    global logger
    cmd = cmd.split()
    
    if cmd:
        logger.write(f"[{datetime.datetime.now()}] Execute '{cmd[0]}'\n")
        logger.flush()
        if cmd[0] == "help":
            if len(cmd) == 1:
                print("help - это сообщение\nmodule-run - запуск модуля\nutil-run - запуск утилиты\ndir - отображение текущей папки\nnew - создать файл/директорию\nsettings - изменить настройки\necho - отобразить текст\nversion - вывести версию\nrun - запустить скрипт\nview - просмотреть содержимое файла")
                logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                logger.flush()
                
            elif len(cmd) == 2:
                if cmd[1] == "errors":
                    print("=== ОШИБКИ ROLTONVENV ===\n")
                    print("Класс ошибок 0x0000001x - ошибки в системе пользователей / фатальные ошибки")
                    print(" - 0x00000011 - пользователь уже существует")
                    print(" - 0x00000012 - пользователь не существует")
                    print(" - 0x00000013 - файловая система повреждена (также является типом ошибки для всех встроеенных ошибок)")
                    print(" - 0x00000014 - неизвестная ошибка")
                    print("\nКласс ошибок 0x0000002x - ошибки в командах")
                    print(" - 0x00000021 - неизвестная команда")
                    print(" - 0x00000022 - неизвестный аргумент функции")
                    print(" - 0x00000023 - недостаточно аргументов")
                    print("\nКласс ошибок 0x0000003x - ошибки в утилитах")
                    print(" - 0x00000031 - неизвестная утилита")
                    print(" - 0x00000032 - неправильный аргумент утилиты")
                    print("\nКласс ошибок 0x0000004x - ошибки в модулях")
                    print(" - 0x00000041 - неизвестный модуль")
                    print(" - 0x00000042 - отсутсвует название модуля")
                    print(" - 0x00000043 - модуль поврежден (также является типом ошибки для всех встроеенных ошибок)")
                    print("\nКласс ошибок 0x0000005x - ошибки файловой системы")
                    print(" - 0x00000051 - файл не найден")
                    print("\nКласс ошибок 0x0000006x - ошибки прав доступа")
                    print(" - 0x00000061 - нету прав на выполнение команды")
                else:
                    print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                    logger.flush()
        elif cmd[0] == "exit":
            if len(cmd) == 1:
                logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                logger.flush()
                logger.close()
                return
                
            else:
                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                logger.flush()
                
        elif cmd[0] == "dir":
            try:
                print(f"| [{workdir}]")
                for filer in os.listdir(workdir):
                    print(f"|-- {filer}")
                    
            except Exception as e:
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' BUILTIN_ERROR '{e}'\n")
                logger.flush()
                print(f"BUILTIN_ERROR: {e}")
            else:
                logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                logger.flush()
                
        elif cmd[0] == "util-run":
            if len(cmd) > 2:
                if cmd[1] == "calc":
                    print(calculate(cmd[2]))
                    logger.write(f"[{datetime.datetime.now()}] Succesful execute utilite '{cmd[1]}'\n")
                    logger.flush()
                    
                elif cmd[1] == "color-checker":
                    checker_color()
                    logger.write(f"[{datetime.datetime.now()}] Succesful execute utilite '{cmd[1]}'\n")
                    logger.flush()
                    
                else:
                    print("UTIL_UWNKOWN_ERROR (0x00000031): неизвестная утилита")
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000031\n")
                    logger.flush()
                    
            else:
                print("COMMAND_NEED_ARGUMENT_ERROR (0x00000023): недостаточно аргументов")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000023\n")
                logger.flush()
                
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
                                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000043 (BUILTIN_ERROR: {e})\n")
                                logger.flush()
                            else:
                                os.system("cls")
                                logger.write(f"[{datetime.datetime.now()}] Succesful execute module '{cmd[1]}'\n")
                        else:
                            continue
                    if flag:
                        pass
                        
                    else:
                        print("MODULE_UWNKOWN_ERROR (0x00000041): неизвестный модуль. Скачайте его с помощью rolton-venv-get")
                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000041\n")
                        logger.flush()
                        
            else:
                print("MODULE_NEED_ARGUMENT_ERROR (0x00000042): ожидалось 2 аргумента")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000042\n")
                logger.flush()
                
        elif cmd[0] == "cd":
            # заглушка
            folders = cmd[1].split("/")
            print(folders)
            logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
            logger.flush()
            
        elif cmd[0] == "new":
            if len(cmd) in (1, 2,):
                print("COMMAND_NEED_ARGUMENT_ERROR (0x00000023): недостаточно аргументов")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000023\n")
                logger.flush()
            else:
                if cmd[1] == "file":
                    open(os.path.join(workdir, cmd[2]), "x").close()
                    logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                    logger.flush()
                elif cmd[1] == "dir":
                    try: os.mkdir(cmd[2])
                    except Exception as e:
                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' BUILTIN_ERROR '{e}'\n")
                        logger.flush()
                        print(f"BUILTIN_ERROR: {e}")
                    else:
                        logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                        logger.flush()
                else:
                    print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                    logger.flush()
                    
        elif cmd[0] == "version":
            if len(cmd) == 1:
                vers_file = open(os.path.join(os.getcwd(), "bin", "sys", "data", "version.txt"), "r")
                print(f"Версия RoltonVenv: {vers_file.read()}")
                vers_file.close()
                logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                logger.flush()
                
            else:
                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                logger.flush()
                
        elif cmd[0] == "settings":
            if len(cmd) >= 3:
                if cmd[1] == "log":
                    if cmd[2] == "get":
                        print(logger.read())
                        logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                        logger.flush()
                    elif cmd[2] == "clear":
                        if root:
                            logger.close()
                            logger = open(os.path.join(os.getcwd(), "bin", "sys", "data", "log.txt"), "w")
                            logger.write()
                            logger.flush()
                            logger.close()
                            logger = open(os.path.join(os.getcwd(), "bin", "sys", "data", "log.txt"), "a+")
                            logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                            logger.flush()
                        else:
                            print("ACCESS_NOT_GRANTED_ERROR (0x00000061): вы не администратор")
                            logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000061\n")
                            logger.flush()
                    else:
                        print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[2]}'")
                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                        logger.flush()
                elif cmd[1] == "system":
                    if len(cmd) >= 4:
                        if cmd[2] == "welcome-text":
                            if cmd[3] == "style":
                                if cmd[4] == "get":
                                    theme = open(os.path.join(os.getcwd(), "bin", "sys", "data", "selected-logo.txt"), "r")
                                    print(f"Выбранная тема: {theme.read()[:1]}")
                                    theme.close()
                                elif cmd[4] == "set":
                                    if root:
                                        try: test = cmd[5]
                                        except KeyError:
                                            print("COMMAND_NEED_ARGUMENT_ERROR (0x00000023): недостаточно аргументов")
                                            logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000023\n")
                                            logger.flush()
                                        else:
                                            if cmd[5] in ("standart", "doom", "money"):
                                                theme = open(os.path.join(os.getcwd(), "bin", "sys", "data", "selected-logo.txt"), "w")
                                                theme.write(cmd[5] + "\n")
                                                theme.flush()
                                                theme.close()
                                            else:
                                                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[5]}'")
                                                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                                                logger.flush()
                                    else:
                                        print("ACCESS_NOT_GRANTED_ERROR (0x00000061): вы не администратор")
                                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000061\n")
                                        logger.flush()
                                else:
                                    print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[4]}'")
                                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                                    logger.flush()
                            else:
                                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[3]}'")
                                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                                logger.flush()
                        elif cmd[2] == "users":
                            if cmd[3] == "add":
                                if root:
                                    if len(cmd) > 6:
                                        if cmd[6] in ("1", "0"):
                                            workdir = os.path.join(os.getcwd(), "users", cmd[4])
                                            try: os.mkdir(workdir)
                                            except FileExistsError:
                                                print(f"FILE_EXISTS_ERROR (0x00000011): пользователь '{cmd[4]}' уже существует")
                                                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000011\n")
                                                logger.flush()
                                            code, error, _ = registr(cmd[4], cmd[5], workdir, "40", "37", int(cmd[6]))
                                            if code:
                                                print(f"BUILTIN_ERROR: {error}")
                                                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' (BUILTIN_ERROR: '{error}')\n")
                                                logger.flush()
                                        else:
                                            print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[6]}'")
                                            logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                                            logger.flush()
                                    else:
                                        print("COMMAND_NEED_ARGUMENT_ERROR (0x00000023): недостаточно аргументов")
                                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000023\n")
                                        logger.flush()
                                else:
                                    print("ACCESS_NOT_GRANTED_ERROR (0x00000061): вы не администратор")
                                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000061\n")
                                    logger.flush()
                            elif cmd[3] == "view":
                                if len(cmd) > 4:
                                    if cmd[4] == "root":
                                        data = user_data_get()
                                        for name, values in data.items():
                                            if values[6] == 1:
                                                print(f"Пользователь {name}\n  - ID: {values[0]}\n  - Администратор: да\n  - Рабочая директория: {values[3]}\n")
                                        logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                                        logger.flush()
                                    elif cmd[4] == "all":
                                        data = user_data_get()
                                        for name, values in data.items():
                                            print(f"Пользователь {name}\n  - ID: {values[0]}\n  - Администратор: {"да" if values[6] == 1 else "нет"}\n  - Рабочая директория: {values[3]}\n")
                                        logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                                        logger.flush()
                                    else:
                                        print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[4]}'")
                                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                                        logger.flush()
                            else:   
                                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[3]}'")
                                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                                logger.flush()
                        else:   
                            print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[2]}'")
                            logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                            logger.flush()
                    else:
                        print("COMMAND_NEED_ARGUMENT_ERROR (0x00000023): недостаточно аргументов")
                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000023\n")
                        logger.flush()
                else:
                    print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                    logger.flush()
            else:
                print("COMMAND_NEED_ARGUMENT_ERROR (0x00000023): недостаточно аргументов")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000023\n")
                logger.flush()
        elif cmd[0] == "echo":
            for string in cmd[1:]: print(string, end = " ")
            logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
            logger.flush()
        elif cmd[0] == "run":
            if len(cmd) == 1:
                print("COMMAND_NEED_ARGUMENT_ERROR (0x00000023): недостаточно аргументов")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000023\n")
                logger.flush()
            else:
                try: script_user = open(os.path.join(os.getcwd(), "scripts", f"{cmd[1]}"))
                except FileNotFoundError:
                    print("FILE_NOT_FOUND_ERROR (0x00000051): файл не найден!")
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000051\n")
                    logger.flush()
                except Exception as e:
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' BUILTIN_ERROR '{e}'\n")
                    logger.flush()
                    print(f"BUILTIN_ERROR: {e}")
                else:
                    commands = script_user.read().split("\n")
                    commands = commands[:-1] if commands[-1] == "" else commands
                    for cmd in commands: runner(cmd, workdir, userdir, username)
                    print()
                    script_user.close()
                    logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                    logger.flush()
        elif cmd[0] == "view":
            if len(cmd) == 2:
                try: 
                    file_opened = open(os.path.join(workdir, cmd[1]), "r")
                except FileNotFoundError:
                    print("FILE_NOT_FOUND_ERROR (0x00000051): файл не найден!")
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000051\n")
                    logger.flush()
                except Exception as e:
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' BUILTIN_ERROR '{e}'\n")
                    logger.flush()
                    print(f"BUILTIN_ERROR: {e}")
                else:
                    print(file_opened.read())
                    logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                    logger.flush()
                    file_opened.close()
            else:
                print("COMMAND_NEED_ARGUMENT_ERROR (0x00000023): недостаточно аргументов")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000023\n")
                logger.flush()
        elif cmd[0] == "sponsors":
            if len(cmd) == 1:
                print("Спонсоры:\nPulsarVenv - похожий на наш проект (ТГ: @pulsarvenv)")
            else:
                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                logger.flush()
        elif cmd[0].startswith("#"):
            print("", end = "")
        elif cmd[0] == "fetch":
            if len(cmd) == 1:
                fetch_file = open(os.path.join(os.getcwd(), "bin", "sys", "data", "fetch.txt"), "r")
                lines = fetch_file.readlines()
                vers_file = open(os.path.join(os.getcwd(), "bin", "sys", "data", "version.txt"), "r")
                print(f"{lines[0]}\n{lines[1]} Имя: RoltonVenv {vers_file.readlines()[0]} для {platform.system()}\n{lines[2]}\n{lines[3]} ОС: {platform.system()} {platform.release()}\n{lines[4]}\n{lines[5]} Версия: {vers_file.readlines()[0]}\n{lines[6]}\n{lines[7]} CPU: {platform.processor()}\n{lines[8]}\n{lines[9]} Пользователь: {username}\n{lines[10]}\n")
                logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                logger.flush()
                fetch_file.close()
                vers_file.close()
            else:
                print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                logger.flush()
        else:
            print(f"COMMAND_UWNKOWN_ERROR (0x00000021): неизвестная команда '{cmd[0]}'. Для запуска модуля используйте 'module-run', для запуска утилиты 'util-run'")
            logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000021\n")
            logger.flush()
    else:
        return
