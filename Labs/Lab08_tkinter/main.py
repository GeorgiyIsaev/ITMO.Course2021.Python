# Задание на применение tkinter
# Постановка задачи
# Требуется разработать программу для отображения на карте любого
# аэропорта, данные о котором содержатся в базе данныех, согласно указанным ниже требованиям.
# Реализация классов должна быть в отдельных модулях.
# В тексте использовать комментарии, поясняющие ваши действия и
# принятые решения. Также каждый модуль, класс и функция должны
# быть снабжены документационными комментариями.
# Архитектура решения должна соответствовать паттерну MVC.
# Базовые требоваия
# Реализовать интерфейс tkinter, включающий:
# Два выпадающих списка (combobox). Первый список позволяет выбрать
# страну, второй – город и аэропорт (в случае если в городе более чем один аэропорт).
# Кнопку отображения аэропорта на карте.
# Использовать данные из предоставленных файлов JSON.
# Отображение осуществляется при помощи API Google Maps в окне
# (вкладке) браузера.


from Labs.Lab08_tkinter.mainWindow import mainWindow

def main():
    mainWin = mainWindow()

if __name__ == "__main__":
    main()