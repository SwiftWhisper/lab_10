# Функція для запису питання
def write_question(filename):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            question = input("Введіть питання: ")
            file.write(f"Питання: {question}\n")
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
    try:
        write_answer(filename)
        write_question(filename)
        print("Роботу завершено.")
    except:
        print("Сталася помилка під час виконання програми.")


# Виклик основної функції
answer_question("collaborative_task.txt")
