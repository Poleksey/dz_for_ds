# ввод
setter = []


def setting_of_setter(setter: list) -> list:
    print("Ваше множество на данный момент:", setter)
    inter = input(
        "    Введите числа, соответствующие синтаксису языка Python, которые вы хотите видеть в множестве.\n\
    Если хотите комплексное число, введите с \n\
    (При работе с комплексными числами ошибки фатальны) \n\
    Для выхода из состояния ввода чисел введите q\n\
    "
    )

    if inter == "q":
        # print("сеттер до выхода",setter)
        return setter

    if inter == "с" or inter == "c":
        real_part = input("Введите действительную часть комплексного числа: ")

        try:
            float_num = float(real_part)
            real_part = float_num

        except ValueError:
             while 0 < 1:
                print(
                    "\n\
                    \n\
                    Уничтожте исполнение программы."
                )
        imag_part = input("Введите мнимую часть комплексного числа, не равную 0:")
        if imag_part == "0":
            while 0 < 1:
                print(
                    "\n\
                    \n\
                    Уничтожте исполнение программы."
                )

        try:
            float_num = float(imag_part)
            imag_part = float_num
        except ValueError:
             while 0 < 1:
                print(
                    "\n\
                    \n\
                    Уничтожте исполнение программы."
                )
        complex_number = complex(real_part, imag_part)
        setter.append(complex_number)
        print(setter)
        setting_of_setter(setter)
    else:
        try:

            int_num = int(inter)
            setter.append(int_num)
            setting_of_setter(setter)
        except ValueError:

            try:
                # Проверяем, можно ли преобразовать введенное число в дробное
                float_num = float(inter)
                setter.append(float_num)
                setting_of_setter(setter)
            except ValueError:
                print(
                    "    Возможно, это не совсем число\n\
        ⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n\
        ⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n\
        ⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n\
        ⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n\
        ⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n\
        ⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n\
        ⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n\
        ⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n\
        ⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n\
        ⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n\
        ⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n\
        ⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n\
        ⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n\
        ⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄\n\
        ⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄. .\n\
       "
                )
            setting_of_setter(setter)

    return setter


setterend = setting_of_setter(setter)

# избавляемся от повторных элементов
settered = set(setterend)
# print(settered)
settered_list = list(settered)
print(settered_list)
# находим мощность множества
sila = len(settered_list)


def subsets(settered_list: list):
    result = [[]]
    for element in settered_list:
        result += [subset + [element] for subset in result]
    return result


bullean = subsets(settered_list)


print("Вот ваш булеан мощности ", sila)
print(bullean)
