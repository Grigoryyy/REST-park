import importlib

try:
    importlib.import_module('flask')
    print('flask уже установлен!')
except ImportError:
    print("Библиотека Flask не найдена.")
    install = input("Хотите установить Flask? (y/n): ")

    if install.lower() == 'y':
        try:
            import pip
        except ImportError:
            print("Установите pip для установки библиотек.")
            exit()

        pip.main(['install', 'flask'])
        print("Библиотека Flask успешно установлена.")
    else:
        print("Вы отказались от установки библиотеки Flask.")