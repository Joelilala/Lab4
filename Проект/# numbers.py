# numbers.py

def main():
    """Запрашивает четыре числа у пользователя, выполняет вычисления и выводит результат."""

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        num3 = float(input("Введите третье число: "))
        num4 = float(input("Введите четвертое число: "))

        sum1 = num1 + num2
        sum2 = num3 + num4

        if sum2 == 0:
            print("Ошибка: Деление на ноль!")
        else:
            result = sum1 / sum2
            print(f"Результат: {result:.2f}")  # Вывод с двумя знаками после запятой

    except ValueError:
        print("Ошибка: Введите числа.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()
