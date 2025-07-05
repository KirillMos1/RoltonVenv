import datetime
import getpass
import os

import bin.sys.cmd
import bin.sys.users_manager

logger = open(os.path.join(os.getcwd(), "bin", "sys", "data", "log.txt"), "a")
work_directory = ""
user_home = ""
user_name = ""
user_passwd = ""
user_id = 0
user_color_bg = ""
user_color_fg = ""
user_root = 0

logger.write(f"[{datetime.datetime.now()}] Init functions\n")
logger.flush()


def loginning(users: dict):
    global \
        work_directory, \
        user_home, \
        user_name, \
        user_passwd, \
        user_id, \
        user_color_bg, \
        user_color_fg, \
        user_root
    print("Вход в RoltonVenv")
    name = input("Введите имя пользователя (для регистрации нового введите CREATE): ")
    if name == "CREATE":
        os.system("cls" if os.name == "nt" else "clear")
        registrate(0)
        return
    logger.write(f"[{datetime.datetime.now()}] Loginning\n")
    logger.flush()
    try:
        id_user, _, passwd, workdir, color_fg, color_bg, root = users[name]
    except KeyError:
        print("USER_NOT_EXISTS_ERROR (0x00000012): Пользователь не существует!")
        input("Нажмите ENTER для выхода...")
        logger.write(
            f"[{datetime.datetime.now()}] RoltonVenv crashed with code 0x00000012\n"
        )
        logger.flush()
        logger.close()
        exit(0x00000012)
    try:
        os.listdir(workdir)
    except Exception as e:
        print(
            "FILE_SYSTEM_CORRUPTED_ERROR (0x00000013): Файловая система повреждена! Переустановите RoltonVenv"
        )
        print(f"BUILTIN_ERROR: {e}")
        logger.write(
            f"[{datetime.datetime.now()}] RoltonVenv crashed with code 0x00000013 (BUILTIN_ERROR '{e}')\n"
        )
        logger.flush()
        logger.close()
        input("Нажмите ENTER для выхода...")
        exit(0x00000013)
    passwd_check = getpass.getpass("Пароль: ")
    if passwd == passwd_check:
        print("Успешно войдено!")
        user_id = id_user
        user_passwd = passwd
        user_name = name
        work_directory = workdir
        user_home = workdir
        user_color_fg = color_fg
        user_color_bg = color_bg
        user_root = 1 if root else 0


def registrate(root):
    logger.write(f"[{datetime.datetime.now()}] Registration\n")
    logger.flush()
    global \
        work_directory, \
        user_home, \
        user_name, \
        user_passwd, \
        user_id, \
        user_color_fg, \
        user_color_bg, \
        user_root
    print(
        f"Создание аккаунта Rolton Venv {'(аккаунт будет создан с правами администратора)' if root else ''}"
    )
    name = input("Ваше имя: ")
    passwd = getpass.getpass("Пароль: ")
    passwd_check = getpass.getpass("Еще раз пароль: ")
    while passwd != passwd_check:
        print("Пароли не сходятся!")
        passwd = getpass.getpass("Пароль: ")
        passwd_check = getpass.getpass("Еще раз пароль: ")
    while True:
        color_fg = input(
            "Введите цвет фона (используйте таблицу:\n40 - черный\n41 - красный\n42 - зеленый\n43 - желтый\n44 - синий\n45 - марганец\n46 - циановый\n47 - белый)\nЦвет фона: "
        )
        try:
            color_fg_int = int(color_fg)
        except ValueError:
            print("Значение не числовое!")
            continue
        else:
            if color_fg_int > 47 and color_fg_int < 40:
                print("Значение не входит в рамки!")
                continue
            else:
                break
    while True:
        color_bg = input(
            "Введите цвет текста (используйте таблицу:\n30 - черный\n31 - красный\n32 - зеленый\n33 - желтый\n34 - синий\n35 - марганец\n36 - циановый\n37 - белый)\nЦвет текста: "
        )
        try:
            color_bg_int = int(color_bg)
        except ValueError:
            print("Значение не числовое!")
            continue
        else:
            if color_bg_int > 37 and color_bg_int < 30:
                print("Значение не входит в рамки!")
                continue
            else:
                break
    workdir = os.path.join(os.getcwd(), "users", name)
    try:
        os.mkdir(workdir)
    except FileExistsError:
        print(
            "USER_ALREADY_EXISTS_ERROR (0x00000011): Такой пользователь уже существует!"
        )
        input("Нажмите ENTER для выхода...")
        logger.write(
            f"[{datetime.datetime.now()}] RoltonVenv crashed with code 0x00000011\n"
        )
        logger.flush()
        logger.close()
        exit(0x00000011)
    code, error, id_us = bin.sys.users_manager.registr(
        name, passwd, workdir, color_fg, color_bg, root
    )
    if not code:
        print("Успешная регистрация!")
        user_id = id_us
        user_passwd = passwd
        user_name = name
        work_directory = workdir
        user_home = workdir
        user_color_bg = color_bg
        user_color_fg = color_fg
        user_root = 1 if root else 0
    else:
        print(f"Произошла ошибка при регистрации\nBUILTIN_ERROR: {error}")
        logger.write(
            f"[{datetime.datetime.now()}] RoltonVenv crashed with code 0x00000014 (BUILTIN_ERROR '{error}')\n"
        )
        logger.flush()
        input("Нажмите ENTER для выхода...")
        logger.close()
        exit(0x00000014)


def run():
    print(f"\033[{user_color_fg};{user_color_bg}m")
    os.system("cls" if os.name == "nt" else "clear")
    bin.sys.cmd.runner(
        f"run {'RoltonVenv-start.rvs'}", work_directory, user_home, user_name, user_root
    )
    command = ""
    while command != "exit":
        command = input(f"{work_directory[len(os.getcwd()) :]}>> ")
        bin.sys.cmd.runner(command, work_directory, user_home, user_name, user_root)
    logger.write(f"[{datetime.datetime.now()}] RoltonVenv exit\n")
    logger.flush()
    logger.close()


logger.write(f"[{datetime.datetime.now()}] Init functions succsesful\n")
logger.flush()
theme = open(os.path.join(os.getcwd(), "bin", "sys", "data", "selected-logo.txt"), "r")
theme_selected = open(
    os.path.join(
        os.getcwd(), "bin", "sys", "data", "logo", f"{(theme.readline())[:-1]}.txt"
    ),
    "r",
)
print(theme_selected.read())
theme.close()
theme_selected.close()
users = bin.sys.users_manager.checker()
if users == 0:
    registrate(1)
else:
    loginning(users)

logger.write(f"[{datetime.datetime.now()}] Run shell\n")
logger.flush()
run()
