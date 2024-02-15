import os

def create_note(title, content):
    with open(f"{title}.txt", "w") as note_file:
        note_file.write(content)
    print(f"Заметка '{title}' создана.")

def read_notes():
    notes_list = os.listdir()
    notes = [note for note in notes_list if note.endswith(".txt")]
    if notes:
        print("Список заметок:")
        for note in notes:
            print(note)
    else:
        print("Заметок нет.")

def read_note(title):
    try:
        with open(f"{title}.txt", "r") as note_file:
            content = note_file.read()
            print(content)
    except FileNotFoundError:
        print(f"Заметка с названием '{title}' не найдена.")

def edit_note(title, new_content):
    try:
        with open(f"{title}.txt", "w") as note_file:
            note_file.write(new_content)
        print(f"Заметка '{title}' отредактирована.")
    except FileNotFoundError:
        print(f"Заметка с названием '{title}' не найдена.")

def delete_note(title):
    try:
        os.remove(f"{title}.txt")
        print(f"Заметка '{title}' удалена.")
    except FileNotFoundError:
        print(f"Заметка с названием '{title}' не найдена.")

def main():
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Показать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название заметки: ")
            content = input("Введите содержимое заметки: ")
            create_note(title, content)
        elif choice == "2":
            read_notes()
        elif choice == "3":
            title = input("Введите название заметки: ")
            read_note(title)
        elif choice == "4":
            title = input("Введите название заметки: ")
            new_content = input("Введите новое содержимое заметки: ")
            edit_note(title, new_content)
        elif choice == "5":
            title = input("Введите название заметки: ")
            delete_note(title)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
