import os, bin.sys.users_manager, getpass, bin.sys.cmd

work_directory = ""
user_home = ""
user_name = ""
user_passwd = ""
user_id = 0

def loginning(users: dict):
    global work_directory, user_home, user_name, user_passwd, user_id
    print("Вход в RoltonVenv")
    name = input("Введите имя пользователя: ")
    try: id_user, _, passwd, workdir = users[name]
    except KeyError:
        print("USER_NOT_EXISTS_ERROR (0x00000012): Пользователь не существует!")
        input("Нажмите ENTER для выхода...")
        exit(0x00000012)
    try:
        os.listdir(workdir)
    except Exception as e:
        print("FILE_SYSTEM_CORRUPTED_ERROR (0x00000013): Файловая система повреждена! Переустановите RoltonVenv")
        print(f"BUILTIN_ERROR: {e}")
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

def registrate():
    global work_directory, user_home, user_name, user_passwd, user_id
    print("Создание аккаунта Rolton Venv")
    name = input("Ваше имя: ")
    passwd = getpass.getpass("Пароль: ")
    passwd_check = getpass.getpass("Еще раз пароль: ")
    while passwd != passwd_check:
        print("Пароли не сходятся!")
        passwd = getpass.getpass("Пароль: ")
        passwd_check = getpass.getpass("Еще раз пароль: ")
    workdir = os.getcwd() + "\\users\\" + name
    try: os.mkdir(workdir)
    except FileExistsError:
        print("USER_ALREADY_EXISTS_ERROR (0x00000011): Такой пользователь уже существует!")
        input("Нажмите ENTER для выхода...")
        exit(0x00000011)
    code, error, id_us = bin.sys.users_manager.registr(name, passwd, workdir)
    if not code:
        print("Успешная регистрация!")
        user_id = id_us
        user_passwd = passwd
        user_name = name
        work_directory = workdir
        user_home = workdir

def run():
    command = ""
    while command != "exit":
        command = input(f"{work_directory[len(os.getcwd()):]}>> ")
        bin.sys.cmd.runner(command, work_directory, user_home, user_name)

users = bin.sys.users_manager.checker()
if users == 0:
    registrate()
else:
    loginning(users)

run()