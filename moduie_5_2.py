class House:
    def __init__(self, name, floors=0):
        self.name = name              # Имя дома
        self.number_Of_Floors = floors  # Изначальное количество этажей, по умолчанию 0

    def setNewNumber_Of_Floors(self, floors):
        self.number_Of_Floors = floors  # Изменяем количество этажей
        print(self.number_Of_Floors)     # Выводим новое количество этажей в консоль

    def __len__(self):
        return self.number_Of_Floors      # Возвращаем количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_Of_Floors}"  # Возвращаем строку с информацией о доме

# Пример использования класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Использование специального метода __str__
print(h1)  # Вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Вывод: Название: ЖК Акация, кол-во этажей: 20

# Использование специального метода __len__
print(len(h1))  # Вывод: 10
print(len(h2))  # Вывод: 20
