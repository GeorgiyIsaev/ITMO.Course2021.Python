from FinalTask.model.InfoSubject import InfoSubject
from FinalTask.control.createInfoSubject import createInfoSubject

def main():
    while(True):
        print("")
        print("1-Добавить")
        print("2-Показать все")
        print("3-Показать по дате")
        print("4-Показать по категории")
        print("5-Показать по min->max")
        print("6-Удалить запись")
        print("0-Завершить работу")

        valueMenu = input('Введите номер меню: ')
        if valueMenu == "1":
            print("Выбрано 1-Добавить")
            obj = createInfoSubject()
            print(obj)
        elif valueMenu == "2":
            print("Выбрано 2-Показать все")
        elif valueMenu == "3":
            print("Выбрано 3-Показать по дате")
        elif valueMenu == "4":
            print("Выбрано 4-Показать по категории")
        elif valueMenu == "5":
            print("Выбрано 5-Показать по min->max")
        elif valueMenu == "6":
            print("Выбрано 6-Удалить запись")
        elif valueMenu == "0":
            break
            print("Работа приложения завершена")

main()