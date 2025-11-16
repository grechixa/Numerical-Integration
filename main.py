import os
from interface import *
from Source.integration import *
from tabulate import tabulate
from Source.functions import *
from Source.diff_eq import *


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    while True:
        clear_console()
        tasks()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            integration_menu()
        elif choice == "2":
            differential_equations_menu()
        elif choice == "3":
            elementary_functions_menu()
        elif choice == "4":
            nonlinear_equations_menu()
        elif choice == "0":
            print("Завершение работы...")
            break
        else:
            print("Неверный ввод. Нажмите Enter чтобы продолжить...")
            input()


def integration_menu():
    while True:
        clear_console()
        integrationTypes()
        choice = input("Выберите тип интегрирования: ")

        if choice == "1":
            const_step_integration_menu()
        elif choice == "2":
            var_step_integration_menu()
        elif choice == "3":
            multiple_integrals_menu()
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Нажмите Enter чтобы продолжить...")
            input()


def const_step_integration_menu():
    while True:
        clear_console()
        ConstStepMethods()
        choice = input("Выберите метод интегрирования: ")

        if choice == "1":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            print("Результат: ", left(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "2":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            print("Результат: ", right(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "3":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            print("Результат: ", trapezoid(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "4":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            print("Результат: ", simpson(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "5":
            clear_console()
            print("Левых частей: ", left(0.8, 1.6, 10000))
            print("Правых частей: ", right(0.8, 1.6, 10000))
            print("Трапеции: ", trapezoid(0.8, 1.6, 10000))
            print("Симпсон: ", simpson(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Нажмите Enter чтобы продолжить...")
            input()


def var_step_integration_menu():
    while True:
        clear_console()
        VarStepMethods()
        choice = input("Выберите алгоритм: ")

        if choice == "1":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            print("Результат: ", algorithm1(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "2":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            print("Результат: ", algorithm2(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "3":
            clear_console()
            print("Алгоритм 1: ", algorithm1(0.8, 1.6, 10000))
            print("Алгоритм 2: ", algorithm2(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Нажмите Enter чтобы продолжить...")
            input()


def multiple_integrals_menu():
    clear_console()
    print("Вычисляется интеграл:")
    print(
        "I = double integral over x=0..1 and y=0..2 of (x^2 + y) / (1 + x + y^2) dy dx"
    )
    print("Результат: ", double_integral(0.8, 1.6, 0.8, 1.6, 100, 100))
    print("\nЧтобы продолжить нажмите enter ...")
    input()


def differential_equations_menu():

    while True:
        clear_console()
        diff_ur_type()
        choice = input("\nВыберите тип уравнения: ").strip()

        if choice == "0":
            break

        # Настройки по-умолчанию в зависимости от выбора
        if choice == "1":
            func = control_case_1
            y0 = [1.0]
            a, b = 0.0, 1.0
            n = 10
        elif choice == "2":
            func = control_case_2
            y0 = [1.0, 0.0]
            a, b = 1.0, 2.0
            n = 10
        elif choice == "3":
            func = control_case_3
            y0 = [2.0, 1.0, 1.0]
            a, b = 0.0, 0.3
            n = 100
        else:
            print("Некорректный выбор. Нажмите Enter чтобы продолжить...")
            input()
            continue

        # Выбор метода
        while True:
            clear_console()
            diff_ur_method()
            method = input("\nВыберите метод: ").strip()

            if method == "0":
                break

            try:
                if method == "1":
                    xs, ys = euler(func, a, b, y0, n)
                elif method == "2":
                    xs, ys = runge(func, a, b, y0, n)
                else:
                    print("Некорректный ввод. Нажмите Enter чтобы попробовать снова...")
                    input()
                    continue
            except Exception as e:
                print(f"Ошибка при вычислении: {e}")
                print("Нажмите Enter чтобы вернуться...")
                input()
                break

            # Формируем таблицу вывода
            table = []
            for i in range(len(xs)):
                row = [f"{xs[i]:.6f}"] + [f"{val:.6f}" for val in ys[i]]
                table.append(row)

            # Заголовки в зависимости от числа уравнений
            headers = ["x"]
            if len(y0) == 1:
                headers += ["y"]
            elif len(y0) == 2:
                headers += ["u", "v"]
            elif len(y0) == 3:
                headers += ["x(t)", "y(t)", "z(t)"]
            else:
                headers += [f"y{i+1}" for i in range(len(y0))]

            clear_console()
            print("=== РЕЗУЛЬТАТ ===\n")
            print(tabulate(table, headers=headers, tablefmt="grid"))
            print("\nГотово. Нажмите Enter чтобы продолжить...")
            input()
            break


# Запуск программы
if __name__ == "__main__":
    main_menu()
