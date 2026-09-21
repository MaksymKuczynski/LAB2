# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: 13
# ПІБ: Кучинський Максим Володимирович

# 1. Звичайні функції
def calc_average(grades):
    """Обчислює середній бал."""
    return sum(grades) / len(grades)

def get_level(avg):
    """Визначає рівень успішності."""
    return "Високий" if avg >= 75 else "Базовий"

# 2. Параметр за замовчуванням
def check_pass(grade, pass_score=60):
    """Перевіряє, чи складено предмет (поріг 60 балів)."""
    return "Складено" if grade >= pass_score else "Не складено"

# 3. Змінна кількість аргументів (*args)
def total_credits(*credits_list):
    """Рахує суму кредитів."""
    return sum(credits_list)

# 4. Лямбда-функція
to_5_scale = lambda mark: round(mark / 20, 1)

# 5. Рекурсивна функція (пошук максимальної оцінки)
def find_max_recursive(grades, index=0):
    """Рекурсивно шукає найвищу оцінку."""
    if index == len(grades) - 1:  # Базовий випадок (кінець списку)
        return grades[index]
    return max(grades[index], find_max_recursive(grades, index + 1))

# 6. Власна функція вищого порядку
def process_grades(data, transform_func):
    """Застосовує передану функцію до кожного елемента."""
    return [transform_func(x) for x in data]


# --- ГОЛОВНА ПРОГРАМА З МЕНЮ ---
def main():
    # Набір даних з 20 оцінок
    grades = [85, 92, 58, 74, 90, 45, 63, 88, 95, 60, 71, 82, 39, 98, 67, 84, 52, 79, 91, 87]

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показати оцінки та аналіз")
        print("2. Додати нову оцінку")
        print("3. Продемонструвати рекурсію та map/filter")
        print("0. Вийти")

        try:
            choice = input("Ваш вибір (0-3): ")

            if choice == "1":
                avg = calc_average(grades)
                print(f"Усі оцінки ({len(grades)} шт.): {grades}")
                print(f"Середній бал: {avg:.1f} ({get_level(avg)} рівень)")
                print(f"Сума кредитів: {total_credits(3, 4, 5, 2)} ECTS")

            elif choice == "2":
                while True:
                    try:
                        new_grade = float(input("Введіть оцінку (0-100): "))
                        if 0 <= new_grade <= 100:
                            grades.append(new_grade)
                            print(f"Оцінку {new_grade} успішно додано! Статус: {check_pass(new_grade)}")
                            break
                        else:
                            print("Некоректна оцінка! Число має бути від 0 до 100. Спробуйте ще раз.")
                    except ValueError:
                        print("Помилка! Введіть саме числове значення (наприклад, 85 або 90.5).")

            elif choice == "3":
                max_val = find_max_recursive(grades)
                passed = list(filter(lambda x: x >= 60, grades))
                converted = list(map(to_5_scale, grades))
                # +2 бали бонусу, але не більше 100 балів
                custom = process_grades(grades, lambda x: min(100.0, x + 2))

                print(f"Максимальна оцінка (рекурсія): {max_val}")
                print(f"Складені оцінки (filter >= 60): {passed}")
                print(f"У 5-бальній системі (map): {converted}")
                print(f"Бонус +2 бали (не більше 100): {custom}")

            elif choice == "0":
                print("Завершення роботи.")
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")

        except ValueError:
            print("Помилка! Введіть числове значення.")

if __name__ == "__main__":
    main()
