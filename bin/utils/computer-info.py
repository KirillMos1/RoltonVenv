import platform


print(
    'Computer info (утилита для RoltonVenv)\nЗащищено лицензией "Apache License version 2.0"\n'
)

print("Загрузка...")
#     ^^^^^^^^^^^^^ возможно не затрется эта запись
cpu_architecture = platform.machine()
print(f"\rИмя компьютера: {platform.uname()[0]}")
print(f" Архитектура процессора: {cpu_architecture}")
print()
