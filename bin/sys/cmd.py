import os, subprocess, datetime
from ..utils.calc import calculate
from ..utils.color_checker import checker_color

logger = open(os.path.join(os.getcwd(), "bin", "sys", "data", "log.txt"), "a+")

def runner(cmd, workdir, userdir, username):
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
                print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000033\n")
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
                        print("MODULE_UWNKOWN_ERROR (0x00000041): неизвестная модуль. Скачайте его с помощью rolton-venv-get")
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
                print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000033\n")
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
                        logger.close()
                        logger = open(os.path.join(os.getcwd(), "bin", "sys", "data", "log.txt"), "w")
                        logger.write()
                        logger.flush()
                        logger.close()
                        logger = open(os.path.join(os.getcwd(), "bin", "sys", "data", "log.txt"), "a+")
                        logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
                    else:
                        print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[2]}'")
                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                        logger.flush()
                elif cmd[1] == "system":
                    if len(cmd) > 5:
                        if cmd[2] == "welcome-text":
                            if cmd[3] == "style":
                                if cmd[4] == "get":
                                    theme = open(os.path.join(os.getcwd(), "bin", "sys", "data", "selected-logo.txt"), "r")
                                    print(f"Выбранная тема: {theme.read()[:1]}")
                                    theme.close()
                                elif cmd[4] == "set":
                                    if cmd[5] in ("standart", "doom", "money"):
                                        theme = open(os.path.join(os.getcwd(), "bin", "sys", "data", "selected-logo.txt"), "w")
                                        theme.write(cmd[5])
                                        theme.flush()
                                        theme.close()
                                    else:
                                        print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[5]}'")
                                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
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
                        print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
                        logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000033\n")
                        logger.flush()
                else:
                    print(f"COMMAND_ARGUMENT_ERROR (0x00000022): неизвестный аргумент функции '{cmd[1]}'")
                    logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000022\n")
                    logger.flush()
            else:
                print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000033\n")
                logger.flush()
        else:
            print(f"COMMAND_UWNKOWN_ERROR (0x00000021): неизвестная команда '{cmd[0]}'. Для запуска модуля используйте 'module-run', для запуска утилиты 'util-run'")
            logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000021\n")
            logger.flush()
    elif cmd[0] == "echo":
        for string in cmd[1:]: print(string, end = " ")
        logger.write(f"[{datetime.datetime.now()}] Succesful execute '{cmd[0]}'\n")
        logger.flush()
    elif cmd[0] == "run":
        if len(cmd) == 1:
            print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
            logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000033\n")
            logger.flush()
        else:
            try: script_user = open(os.path.join(os.getcwd(), "scripts", f"{cmd[1]}.rvs"))
            except FileNotExistsError:
                print("FILE_NOT_FOUND_ERROR (0x00000051): файл не найден!")
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000051\n")
                logger.flush()
            except Exception as e:
                logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' BUILTIN_ERROR '{e}'\n")
                logger.flush()
                print(f"BUILTIN_ERROR: {e}")
            else:
                commands = script_user.read().split("\n")
                commands = commads[:-1] if commands[-1] == "" else commands
                for cmd in commands: runner(cmd, workdir, userdir, username)
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
            print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
            logger.write(f"[{datetime.datetime.now()}] Failed execute '{cmd[0]}' code 0x00000033\n")
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
    else:
        return
