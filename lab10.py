import os


# Функція для перевірки, чи файл порожній, і виведення останнього рядка
def check_last_question(filename):
    try:
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                print(f"{lines[-1].strip()}")
    except:
        print("Сталася помилка під час перевірки файлу.")


# Функція для запису питання
def write_question(filename):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            question = input("Введіть питання: ")
            file.write(f"Питання: {question}\n\n")
    except:
        print("Сталася помилка під час запису питання.")


# Функція для запису відповіді
def write_answer(filename):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            surname = input("Введіть ваше прізвище: ")
            answer = input("Введіть вашу відповідь: ")
            file.write(f"Відповідь від {surname}: {answer}\n")
    except:
        print("Сталася помилка під час запису відповіді.")


# Функція для взаємодії з користувачем
def answer_question(filename):
    check_last_question(filename)  # Перевіряємо файл перед початком роботи
    try:
        write_answer(filename)
        write_question(filename)
        print("Роботу завершено.")
    except:
        print("Сталася помилка під час виконання програми.")


# Виклик основної функції
answer_question("collaborative_task.txt")
