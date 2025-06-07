import os, sys, keyboard

def saving(path, name, content, mode: str = "recont"):
    file_opening = open(os.getcwd(path, name), ("w" if mode == "recont" else "x"))
    file_opening.flush()
    file_opening.close()
    return 0

def exiting(path, name, content, mode = "recont"):
    if content:
        print("\033[24;H\033[a\033[30;47mВы хотите записать изменения?\nY - да | N - нет | C (или др. клавиша) - отмена")
        keyboard.hotkey("y", lambda: saving(path, name, content, mode))
        

def opening(path):
    file_opening = open(path, "r")
    readed = file_opening.read()
    file_opening.close()
    return readed
    
def start():
    print("\033[30;47m    Консольный текстовый редактор RoltonVenv\n\n\033[0m")
    if len(sys.argv) == 1:
        
