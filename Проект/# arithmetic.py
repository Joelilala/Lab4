# arithmetic.py

def main():
    """Предлагает пользователю решить пример и сравнивает с правильным ответом."""

    correct_answer = 4 * 100 - 54

    print("Решите пример: 4 * 100 - 54")
    try:
        user_answer_str = input("Ваш ответ: ")
        user_answer = float(user_answer_str) # Преобразуем строку в число

        print(f"Правильный ответ: {correct_answer}")
        print(f"Ваш ответ: {user_answer}")

        if user_answer == correct_answer:
            print("Правильно!")
        else:
            print("Неправильно.")

    except ValueError:
        print("Ошибка: Введите число.")

if __name__ == "__main__":
    main()
