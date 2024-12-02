import math

def trapezoid_area(a, b, angle_degrees):
    """
    Вычисляет площадь равнобедренной трапеции.

    Args:
        a: Длина большего основания.
        b: Длина меньшего основания.
        angle_degrees: Угол при большем основании в градусах.

    Returns:
        Площадь трапеции. Возвращает None, если входные данные некорректны.
    """

    if a <= b or a <= 0 or b <= 0 or angle_degrees <= 0 or angle_degrees >= 180:
        return None  # Обработка некорректных входных данных


    angle_radians = math.radians(angle_degrees)
    height = (a - b) / (2 * math.tan(angle_radians / 2))
    area = (a + b) * height / 2
    return area


if __name__ == "__main__":
    try:
        a = float(input("Введите длину большего основания: "))
        b = float(input("Введите длину меньшего основания: "))
        angle_degrees = float(input("Введите угол при большем основании (в градусах): "))

        area = trapezoid_area(a, b, angle_degrees)

        if area is not None:
            print(f"Площадь трапеции: {area:.2f}")
        else:
            print("Некорректные входные данные. Проверьте, что a > b > 0 и 0 < угол < 180 градусов.")

    except ValueError:
        print("Ошибка: Введите числа.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")


