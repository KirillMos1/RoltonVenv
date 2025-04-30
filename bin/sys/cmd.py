import os
from ..utils.calc import calculate

def runner(cmd, workdir, userdir, username):
    cmd = cmd.split()
    if cmd:
        if cmd[0] == "help":
            if len(cmd) == 1:
                print("help - это сообщение")
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
                print(e)
        elif cmd[0] == "util-run":
            if len(cmd) > 2:
                if cmd[1] == "calc":
                    print(calculate(cmd[2]))
                else:
                    print("UTIL_UWNKOWN_ERROR (0x00000031): неизвестная утилита")
            else:
                print("UTIL_NEED_ARGUMENT_ERROR (0x00000033): недостаточно аргументов")
        else:
            print(f"COMMAND_UWNKOWN_ERROR (0x00000021): неизвестная команда '{cmd[0]}'. Для запуска модуля используйте 'module-run', для запуска утилиты 'util-run'")
    else:
        return