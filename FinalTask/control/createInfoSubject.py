from FinalTask.model.InfoSubject import InfoSubject


def createInfoSubject():
    category = input('Введите категорию: ')
    product = input('Введите название продукта: ')
    cost = input('Введите цену: ')
    dateBuy = input('Введите дату: ')
    return InfoSubject(category, product, cost, dateBuy)
