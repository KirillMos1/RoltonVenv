import os, bin.sys.users_manager, getpass, bin.sys.cmd, datetime

logger = open(os.path.join(os.getcwd(), "bin", "sys", "data", "log.txt"), "a")
work_directory = ""
user_home = ""
user_name = ""
user_passwd = ""
user_id = 0
user_color_bg = ""
user_color_fg = ""

logger.write(f"[{datetime.datetime.now()}] Init functions\n")
logger.flush()

def loginning(users: dict):
    global work_directory, user_home, user_name, user_passwd, user_id, user_color_bg, user_color_fg
    print("Вход в RoltonVenv")
    name = input("Введите имя пользователя (для регистрации нового введите CREATE): ")
    if name == "CREATE":
        print("\033[2J")
        registrate()
        return
    logger.write(f"[{datetime.datetime.now()}] Loginning\n")
    logger.flush()
    try: id_user, _, passwd, workdir, color_fg, color_bg = users[name]
    except KeyError:
        print("USER_NOT_EXISTS_ERROR (0x00000012): Пользователь не существует!")
        input("Нажмите ENTER для выхода...")
        logger.write(f"[{datetime.datetime.now()}] RoltonVenv crashed with code 0x00000012\n")
        logger.flush()
        logger.close()
        exit(0x00000012)
    try:
        os.listdir(workdir)
    except Exception as e:
        print("FILE_SYSTEM_CORRUPTED_ERROR (0x00000013): Файловая система повреждена! Переустановите RoltonVenv")
        print(f"BUILTIN_ERROR: {e}")
        logger.write(f"[{datetime.datetime.now()}] RoltonVenv crashed with code 0x00000013 (BUILTIN_ERROR '{e}')\n")
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

def registrate():
    logger.write(f"[{datetime.datetime.now()}] Registration\n")
    logger.flush()
    global work_directory, user_home, user_name, user_passwd, user_id, user_color_fg, user_color_bg
    print("Создание аккаунта Rolton Venv")
    name = input("Ваше имя: ")
    passwd = getpass.getpass("Пароль: ")
    passwd_check = getpass.getpass("Еще раз пароль: ")
    while passwd != passwd_check:
        print("Пароли не сходятся!")
        passwd = getpass.getpass("Пароль: ")
        passwd_check = getpass.getpass("Еще раз пароль: ")
    while True:
        color_fg = input("Введите цвет фона (используйте таблицу:\n40 - черный\n41 - красный\n42 - зеленый\n43 - желтый\n44 - синий\n45 - марганец\n46 - циановый\n47 - белый)\nЦвет фона: ")
        try: 
            color_fg_int = int(color_fg)
        except ValueError:
            print("Значение не числовое!")
            continue
        else:
            if color_fg_int > 47 and color_fg_int < 40:
                print("Значение не входит в рамки!")
                continue
            else: break
    while True:
        color_bg = input("Введите цвет текста (используйте таблицу:\n30 - черный\n31 - красный\n32 - зеленый\n33 - желтый\n34 - синий\n35 - марганец\n36 - циановый\n37 - белый)\nЦвет текста: ")
        try:
            color_bg_int = int(color_bg)
        except ValueError:
            print("Значение не числовое!")
            continue
        else:
            if color_bg_int > 37 and color_bg_int < 30:
                print("Значение не входит в рамки!")
                continue
            else: break
    workdir = os.path.join(os.getcwd(), "users", name)
    try: os.mkdir(workdir)
    except FileExistsError:
        print("USER_ALREADY_EXISTS_ERROR (0x00000011): Такой пользователь уже существует!")
        input("Нажмите ENTER для выхода...")
        logger.write(f"[{datetime.datetime.now()}] RoltonVenv crashed with code 0x00000011\n")
        logger.flush()
        logger.close()
        exit(0x00000011)
    code, error, id_us = bin.sys.users_manager.registr(name, passwd, workdir, color_fg, color_bg)
    if not code:
        print("Успешная регистрация!")
        user_id = id_us
        user_passwd = passwd
        user_name = name
        work_directory = workdir
        user_home = workdir
        user_color_bg = color_bg
        user_color_fg = color_fg

def run():
    print(f"\033[{user_color_fg};{user_color_bg}m")
    print("\033[2J")
    command = ""
    while command != "exit":
        command = input(f"{work_directory[len(os.getcwd()):]}>> ")
        bin.sys.cmd.runner(command, work_directory, user_home, user_name)
    logger.write(f"[{datetime.datetime.now()}] RoltonVenv exit\n")
    logger.flush()
    logger.close()

logger.write(f"[{datetime.datetime.now()}] Init functions succsesful\n")
logger.flush()
theme = open(os.path.join(os.getcwd(), "bin", "sys", "data", "selected-logo.txt"), "r")
theme_selected = open(os.path.join(os.getcwd(), "bin", "sys", "data", "logo", f"{theme.read()[:-1]}.txt"), "r")
print(theme_selected.read())
theme.close()
theme_selected.close()
users = bin.sys.users_manager.checker()
if users == 0:
    registrate()
else:
    loginning(users)

logger.write(f"[{datetime.datetime.now()}] Run shell\n")
logger.flush()
run()
