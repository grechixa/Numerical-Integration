import os
from interface import *
from Source.integration import *


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

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
            print("I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx")
            print("Результат: ", left(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "2":
            clear_console()
            print("Вычисляется интеграл:")
            print("I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx")
            print("Результат: ", right(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "3":
            clear_console()
            print("Вычисляется интеграл:")
            print("I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx")
            print("Результат: ", trapezoid(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "4":
            clear_console()
            print("Вычисляется интеграл:")
            print("I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx")
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
            print("I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx")
            print("Результат: ", algorithm1(0.8, 1.6, 10000))
            print("\nЧтобы продолжить нажмите enter ...")
            input()
        elif choice == "2":
            clear_console()
            print("Вычисляется интеграл:")
            print("I = integral from 0.8 to 1.6 of sqrt(2*x + 1.6) / (1.8 + sqrt(0.3*x^2 + 2.3)) dx")
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
    print("I = double integral over x=0..1 and y=0..2 of (x^2 + y) / (1 + x + y^2) dy dx")
    print("Результат: ", double_integral(0.8, 1.6, 10000))
    print("\nЧтобы продолжить нажмите enter ...")
    input()

def differential_equations_menu():
    while True:
        clear_console()
        diff_ur()
        print()
        
        choice = input("Выберите метод: ")
        
        if choice == "1":
            clear_console()
            print("Метод Эйлера - реализация в разработке")
            input()
        elif choice == "2":
            clear_console()
            print("Метод Рунге-Кутты - реализация в разработке")
            input()
        elif choice == "3":
            clear_console()
            print("Метод Адамса - реализация в разработке") 
            input()
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Нажмите Enter чтобы продолжить...")
            input()

def elementary_functions_menu():
    while True:
        clear_console()
        diff_ur()
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            clear_console()
            print("Вычисление значений функций - реализация в разработке")
            input()
        elif choice == "2":
            clear_console()
            print("Построение графиков - реализация в разработке")
            input()
        elif choice == "3":
            clear_console()
            print("Табулирование функций - реализация в разработке")
            input()
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Нажмите Enter чтобы продолжить...")
            input()

def nonlinear_equations_menu():
    while True:
        clear_console()
        nonlinear()
        print()
        
        choice = input("Выберите метод: ")
        
        if choice == "1":
            clear_console()
            print("Метод половинного деления - реализация в разработке")
            input()
        elif choice == "2":
            clear_console()
            print("Метод Ньютона - реализация в разработке")
            input()
        elif choice == "3":
            clear_console()
            print("Метод секущих - реализация в разработке")
            input()
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Нажмите Enter чтобы продолжить...")
            input()

# Запуск программы
if __name__ == "__main__":
    main_menu()