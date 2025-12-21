import os
from interface import *
from Source.integration import *
from tabulate import tabulate
from Source.functions import *
from Source.diff_eq import *
from Source.el_func import *
from Source.nonlinear_eq import *
import numpy as np

try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None


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


def prompt_yes_no(msg, default="n"):
    ans = input(f"{msg} ({'Y/n' if default.lower()=='y' else 'y/N'}): ").strip().lower()
    if ans == "":
        ans = default.lower()
    return ans in ("y", "yes")


def plot_solution(xs, ys, headers):
    if plt is None:
        print("matplotlib не установлен. Невозможно построить график.")
        return
    xs = np.array(xs)
    ys = np.array(ys)
    plt.figure(figsize=(8, 5))
    # Если одномерная (одна компонента), ys имеет форму (N,1) — приводим к (N,)
    if ys.ndim == 1 or ys.shape[1] == 1:
        plt.plot(xs, ys.reshape(-1), label=headers[1] if len(headers) > 1 else "y")
    else:
        for i in range(ys.shape[1]):
            plt.plot(
                xs,
                ys[:, i],
                label=headers[i + 1] if len(headers) > i + 1 else f"y{i+1}",
            )
    plt.xlabel("x")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_integral_curve(a, b, num_points=1000):
    if plt is None:
        print("matplotlib не установлен. Невозможно построить график.")
        return
    xs = np.linspace(a, b, num_points)
    # используем функцию f из Source.functions
    ys = f(xs)
    # накопленный интеграл методом трапеций
    dx = xs[1:] - xs[:-1]
    avg = 0.5 * (ys[:-1] + ys[1:])
    cum = np.zeros_like(xs)
    cum[1:] = np.cumsum(avg * dx)
    plt.figure(figsize=(8, 5))
    plt.plot(xs, cum, label="I(x) = ∫_a^x f(t) dt")
    plt.xlabel("x")
    plt.ylabel("I(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


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
            res = left(0.8, 1.6, 10000)
            print("Результат: ", res)
            if prompt_yes_no("Построить интегральную кривую?", default="n"):
                plot_integral_curve(0.8, 1.6, num_points=2000)
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "2":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            res = right(0.8, 1.6, 10000)
            print("Результат: ", res)
            if prompt_yes_no("Построить интегральную кривую?", default="n"):
                plot_integral_curve(0.8, 1.6, num_points=2000)
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "3":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            res = trapezoid(0.8, 1.6, 10000)
            print("Результат: ", res)
            if prompt_yes_no("Построить интегральную кривую?", default="n"):
                plot_integral_curve(0.8, 1.6, num_points=2000)
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "4":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            res = simpson(0.8, 1.6, 10000)
            print("Результат: ", res)
            if prompt_yes_no("Построить интегральную кривую?", default="n"):
                plot_integral_curve(0.8, 1.6, num_points=2000)
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "5":
            clear_console()
            print("Левых частей: ", left(0.8, 1.6, 10000))
            print("Правых частей: ", right(0.8, 1.6, 10000))
            print("Трапеции: ", trapezoid(0.8, 1.6, 10000))
            print("Симпсон: ", simpson(0.8, 1.6, 10000))
            if prompt_yes_no("Построить интегральную кривую?", default="n"):
                plot_integral_curve(0.8, 1.6, num_points=2000)
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
            res = algorithm1(0.8, 1.6, 10000)
            print("Результат: ", res)
            if prompt_yes_no("Построить интегральную кривую?", default="n"):
                plot_integral_curve(0.8, 1.6, num_points=2000)
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "2":
            clear_console()
            print("Вычисляется интеграл:")
            print(
                "I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx"
            )
            res = algorithm2(0.8, 1.6, 10000)
            print("Результат: ", res)
            if prompt_yes_no("Построить интегральную кривую?", default="n"):
                plot_integral_curve(0.8, 1.6, num_points=2000)
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "3":
            clear_console()
            print("Алгоритм 1: ", algorithm1(0.8, 1.6, 10000))
            print("Алгоритм 2: ", algorithm2(0.8, 1.6, 10000))
            if prompt_yes_no("Построить интегральную кривую?", default="n"):
                plot_integral_curve(0.8, 1.6, num_points=2000)
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
    if prompt_yes_no(
        "Построить интегральную кривую для однопеременной функции f(x)?", default="n"
    ):
        plot_integral_curve(0.8, 1.6, num_points=2000)
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
            default_n = 10
        elif choice == "2":
            func = control_case_2
            y0 = [0.77, -0.44]
            a, b = 1.0, 1.5
            default_n = 10
        elif choice == "3":
            func = control_case_3
            y0 = [2.0, 1.0, 1.0]
            a, b = 0.0, 0.3
            default_n = 100
        else:
            print("Некорректный выбор. Нажмите Enter чтобы продолжить...")
            input()
            continue

        # выбор числа шагов
        while True:
            try:
                n_input = input(
                    f"Введите число шагов n (по умолчанию {default_n}): "
                ).strip()
                n = int(n_input) if n_input != "" else default_n
                if n <= 0:
                    raise ValueError()
                break
            except ValueError:
                print("Неверное значение n. Введите положительное целое число.")

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

            # Формируем таблицу вывода
            table = []
            for i in range(len(xs)):
                row = [f"{xs[i]:.6f}"] + [f"{val:.6f}" for val in ys[i]]
                table.append(row)

            clear_console()
            print("=== РЕЗУЛЬТАТ ===\n")
            # если шагов немного — показываем всю таблицу, иначе только последнее значение
            SHOW_THRESHOLD = 100
            if n <= SHOW_THRESHOLD:
                print(tabulate(table, headers=headers, tablefmt="grid"))
            else:
                last_row = table[-1]
                print("Слишком много шагов. Показано только последнее значение:")
                print(tabulate([last_row], headers=headers, tablefmt="grid"))

            # График решения
            if prompt_yes_no(
                "Построить график решения? (покажутся все компоненты)", default="n"
            ):
                try:
                    plot_solution(xs, ys, headers)
                except Exception as e:
                    print(f"Ошибка при построении графика: {e}")
                    if plt is None:
                        print("Установите matplotlib для отображения графиков.")
            print("\nГотово. Нажмите Enter чтобы продолжить...")
            input()
            break


def elementary_functions_menu():
    clear_console()
    elementary_func()
    var = input("Выберите функцию: ")
    if var == "1":
        clear_console()
        x = int(input("Введите x: ").strip())
        s1, k = exp_row(x)
        s2 = exp_Cheb(x)
        print(f"Вычисляемая функция: e^{x}")
        print(f"Результат методом разложения в ряд: {s1}, шаг {k}")
        print(f"Результат методом чебышева: {s2}")
        input()
    elif var == "2":
        clear_console()
        x = int(input("Введите x: ").strip())
        s1, k = sin_row(x)
        s2 = sin_Cheb(x)
        print(f"Вычисляемая функция: sin({x})")
        print(f"Результат методом разложения в ряд: {s1}, шаг {k}")
        print(f"Результат методом чебышева: {s2}")
        input()
    elif var == "3":
        clear_console()
        x = int(input("Введите x: ").strip())
        y0 = input("Введите y0 (Enter чтобы оставить значение пол умолчанию): ").strip()
        if y0 == "":
            y0 = None
        else:
            y0 = int(y0)

        y, k = sqrt_iter(x)

        print(f"Вычисляемая функция: sqrt({x})")
        print(f"Результат методом итераций: {y}, шаг: {k}")
        input()
    elif var == "4":
        clear_console()
        x = int(input("Введите x: ").strip())
        y0 = input("Введите y0 (Enter чтобы оставить значение пол умолчанию): ").strip()
        if y0 == "":
            y0 = None
        else:
            y0 = int(y0)

        y, k = reverse_sqrt_iter(x)

        print(f"Вычисляемая функция: 1/sqrt({x})")
        print(f"Результат методом итераций: {y}, шаг: {k}")
        input()
    elif var == "0":
        main_menu()


def nonlinear_equations_menu():

    clear_console()
    nonlinear_equations()
    equation = input("Выберите уравнение: ")

    if equation == "1":
        clear_console()
        print("Результаты вычислений: ")

        res_tangent = tangent_method(f1, -1, 1)
        print(f"Метод кастельных: {res_tangent:.6f}")
        res_bisec = bisec_method(f1, -1, 1)
        print(f"Метод бисекции: {res_bisec:.6f}")
        res_chrod = chord_method(f1, -1, 1)
        print(f"Метод хорд: {res_chrod:.6f}")

        input("\nЧтобы продолжить нажмите enter ...")
    if equation == "2":
        clear_console()
        print("Результаты вычислений: ")

        res_tangent = tangent_method(f2, -0.1, 1.2)
        print(f"Метод кастельных: {res_tangent:.6f}")
        res_bisec = bisec_method(f2, -0.1, 1.2)
        print(f"Метод бисекции: {res_bisec:.6f}")
        res_chrod = chord_method(f2, -0.1, 1.2)
        print(f"Метод хорд: {res_chrod:.6f}")

        input("\nЧтобы продолжить нажмите enter ...")
    if equation == "0":
        return


# Запуск программы
if __name__ == "__main__":
    main_menu()
